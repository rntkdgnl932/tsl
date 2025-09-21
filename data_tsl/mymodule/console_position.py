# -*- coding: utf-8 -*-
"""
콘솔 창을 지정 모니터에 정확히 배치하고,
'보이는 검은 콘솔 영역(클라이언트 영역)'을 정확히 W×H로 맞춘다.
- Per-Monitor v2 DPI 인식
- DPI 스케일 보정(논리→물리)
- 프레임 보정(AdjustWindowRectExForDpi)
- 실제 적용 결과를 콘솔에 출력(검증용)
"""

import ctypes
from ctypes import wintypes

user32   = ctypes.WinDLL("user32", use_last_error=True)
kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
gdi32    = ctypes.WinDLL("gdi32",  use_last_error=True)

# ------------------------
# DPI Awareness 설정
# ------------------------
def _enable_per_monitor_v2():
    DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2 = ctypes.c_void_p(-4)
    try:
        # Win10 1703+ 권장
        user32.SetProcessDpiAwarenessContext(DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2)
        return
    except Exception:
        pass
    try:
        # 구버전 호환: 시스템 DPI
        ctypes.windll.user32.SetProcessDPIAware()
    except Exception:
        pass

# ------------------------
# 유틸 함수
# ------------------------
def _get_dpi_for_window(hwnd):
    try:
        # Win10 1607+
        return user32.GetDpiForWindow(hwnd)
    except Exception:
        # Fallback: DC 기반
        hdc = user32.GetDC(hwnd)
        LOGPIXELSX = 88
        dpi = gdi32.GetDeviceCaps(hdc, LOGPIXELSX)
        user32.ReleaseDC(hwnd, hdc)
        return dpi or 96

def _enum_monitors_sorted():
    """[(hmon, (L,T,R,B)), ...]  좌->우, 상->하 정렬"""
    MONITORENUMPROC = ctypes.WINFUNCTYPE(
        wintypes.BOOL, wintypes.HMONITOR, wintypes.HDC, ctypes.POINTER(wintypes.RECT), wintypes.LPARAM
    )
    class MONITORINFOEXW(ctypes.Structure):
        _fields_ = [
            ("cbSize", wintypes.DWORD),
            ("rcMonitor", wintypes.RECT),
            ("rcWork",    wintypes.RECT),
            ("dwFlags",   wintypes.DWORD),
            ("szDevice",  wintypes.WCHAR * 32),
        ]
    items = []
    def cb(hMon, hDC, lprc, lparam):
        info = MONITORINFOEXW()
        info.cbSize = ctypes.sizeof(info)
        user32.GetMonitorInfoW(hMon, ctypes.byref(info))
        r = info.rcMonitor
        items.append((hMon, (r.left, r.top, r.right, r.bottom)))
        return True
    user32.EnumDisplayMonitors(0, 0, MONITORENUMPROC(cb), 0)
    items.sort(key=lambda it: (it[1][1], it[1][0]))
    return items

def _adjust_size_for_frame(client_w, client_h, style, exstyle, dpi):
    """
    클라이언트 영역(client) W,H 를 주면
    프레임 포함 외곽(창 전체) W,H 로 변환.
    DPI 보정 포함.
    """
    # 논리→물리 픽셀 변환
    W = int(client_w * dpi / 96)
    H = int(client_h * dpi / 96)

    rect = wintypes.RECT(0, 0, W, H)
    # AdjustWindowRectExForDpi 가 있으면 사용
    _AdjustForDpi = getattr(user32, "AdjustWindowRectExForDpi", None)
    if _AdjustForDpi:
        _AdjustForDpi(ctypes.byref(rect), style, False, exstyle, dpi)
    else:
        user32.AdjustWindowRectEx(ctypes.byref(rect), style, False, exstyle)
    return rect.right - rect.left, rect.bottom - rect.top

def _get_window_client_rect(hwnd):
    """클라이언트 영역 좌표 (0,0)-(W,H) 반환"""
    rc = wintypes.RECT()
    user32.GetClientRect(hwnd, ctypes.byref(rc))
    return rc.right - rc.left, rc.bottom - rc.top

def _get_window_rect(hwnd):
    rc = wintypes.RECT()
    user32.GetWindowRect(hwnd, ctypes.byref(rc))
    return rc.left, rc.top, rc.right, rc.bottom

# ------------------------
# 메인 함수
# ------------------------
# === 새로 추가: 콘솔 폰트 셀 크기(px) ===
def _get_console_font_cell_px():
    # HANDLE for STD_OUTPUT
    STD_OUTPUT_HANDLE = -11
    hOut = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

    class COORD(ctypes.Structure):
        _fields_ = [("X", wintypes.SHORT), ("Y", wintypes.SHORT)]

    class CONSOLE_FONT_INFOEX(ctypes.Structure):
        _fields_ = [
            ("cbSize", wintypes.ULONG),
            ("nFont", wintypes.DWORD),
            ("dwFontSize", COORD),
            ("FontFamily", wintypes.UINT),
            ("FontWeight", wintypes.UINT),
            ("FaceName", wintypes.WCHAR * 32),
        ]

    GetCurrentConsoleFontEx = kernel32.GetCurrentConsoleFontEx
    GetCurrentConsoleFontEx.argtypes = [wintypes.HANDLE, wintypes.BOOL,
                                        ctypes.POINTER(CONSOLE_FONT_INFOEX)]
    GetCurrentConsoleFontEx.restype  = wintypes.BOOL

    info = CONSOLE_FONT_INFOEX()
    info.cbSize = ctypes.sizeof(info)
    if not GetCurrentConsoleFontEx(hOut, False, ctypes.byref(info)):
        # 실패 시 대략 8x16 가정
        return 8, 16
    # 셀 크기(px)
    return int(info.dwFontSize.X), int(info.dwFontSize.Y)

def _set_console_cols_lines(cols, lines):
    import os
    # 줄 수는 최소 1, 열 최소 1 보장
    cols = max(1, int(cols))
    lines = max(1, int(lines))
    os.system(f"mode con: cols={cols} lines={lines}")
def set_console_on_monitor(
    monitor_index=1,
    client_w=800, client_h=800,
    anchor="center",
    margin=(20, 20),
    cols=None, lines=None     # ← 이제 자동 계산 기본
):
    _enable_per_monitor_v2()

    hwnd = kernel32.GetConsoleWindow()
    if not hwnd:
        return False

    mons = _enum_monitors_sorted()
    if not mons:
        return False

    monitor_index = max(0, min(monitor_index, len(mons) - 1))
    hMon, (L, T, R, B) = mons[monitor_index]
    mw, mh = R - L, B - T

    dpi = _get_dpi_for_window(hwnd)
    GWL_STYLE, GWL_EXSTYLE = -16, -20
    style   = user32.GetWindowLongW(hwnd, GWL_STYLE)
    exstyle = user32.GetWindowLongW(hwnd, GWL_EXSTYLE)

    # 1) 현재 콘솔 폰트 셀(px) 가져오기
    cell_w, cell_h = _get_console_font_cell_px()

    # 2) 목표 client 800x800을 충족하는 cols/lines 산출 (반올림)
    #    (최소 20x5 같은 말도 안 되는 값 방지로 적당히 하한)
    if cols is None or lines is None:
        cols = max(40, round(client_w / max(1, cell_w)))
        lines = max(15, round(client_h / max(1, cell_h)))

    # 3) 먼저 격자 크기 적용(이게 '실제 client'를 결정)
    _set_console_cols_lines(cols, lines)

    # 4) 실제 client 픽셀 크기 재계산 (= cols*cell_w, lines*cell_h)
    actual_client_w = cols * cell_w
    actual_client_h = lines * cell_h

    # 5) 프레임 포함 외곽 크기 계산 후 위치 결정
    W, H = _adjust_size_for_frame(actual_client_w, actual_client_h, style, exstyle, dpi)

    mx, my = margin
    if anchor == "center":
        x = L + (mw - W) // 2;  y = T + (mh - H) // 2
    elif anchor == "topleft":
        x = L + mx;             y = T + my
    elif anchor == "topright":
        x = R - W - mx;         y = T + my
    elif anchor == "bottomright":
        x = R - W - mx;         y = B - H - my
    elif anchor == "bottomleft":
        x = L + mx;             y = B - H - my
    else:
        x = L + mx;             y = T + my

    user32.MoveWindow(hwnd, int(x), int(y), int(W), int(H), True)

    # --- 검증 출력 ---
    cx, cy = _get_window_client_rect(hwnd)
    wx0, wy0, wx1, wy1 = _get_window_rect(hwnd)
    applied_w, applied_h = wx1 - wx0, wy1 - wy0
    print(f"[DPI] {dpi} (96=100%) | cell={cell_w}x{cell_h}px | cols={cols}, lines={lines}")
    print(f"[요청 client] ~{client_w}x{client_h} -> [적용 client] {cx}x{cy}")
    print(f"[적용 window] {applied_w}x{applied_h}")
    print(f"[모니터#{monitor_index}] ({L},{T})-({R},{B}) = {mw}x{mh}")
    print(f"[배치 좌표] x={x}, y={y}, anchor={anchor}, margin={margin}")

    # client 오차 ±cell크기 이내면 OK(셀 격자 단위로만 변함)
    return abs(cx - actual_client_w) <= cell_w and abs(cy - actual_client_h) <= cell_h


# if __name__ == "__main__":
#     # 예시: 2번째 모니터 오른쪽 아래, 여백 40, '보이는 영역' 800×800
#     ok = set_console_on_monitor(
#         monitor_index=1,
#         client_w=800, client_h=800,
#         anchor="bottomright", margin=(40, 40),
#         cols=140, lines=40
#     )
#     print("정확 적용:", ok)
