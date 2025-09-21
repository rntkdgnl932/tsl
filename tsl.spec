# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=['C:\\Users\\1_S_3\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\cv2'],
    binaries=[],
    datas=[('C:\\my_games\\tsl\\data_tsl', 'data_tsl'), ('C:\\my_games\\tsl\\mysettings', 'mysettings'), ('C:\\my_games\\tsl\\tsl_macro.ico', '.')],
    hiddenimports=['PyQt5', 'pyserial', 'requests', 'chardet'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='tsl',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\my_games\\tsl\\tsl_macro.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='tsl',
)
