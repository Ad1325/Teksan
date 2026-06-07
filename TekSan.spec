# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['H:\\Teksan-main\\front\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('H:\\Project\\Teksan\\icons', 'icons/'), ('H:\\Project\\Teksan\\fonts', 'fonts/'), ('H:\\Teksan-main\\front\\conversation.py', 'front/'), ('H:\\Teksan-main\\front\\option_files.py', 'front/'), ('H:\\Teksan-main\\front\\sidebar.py', 'front/'), ('H:\\Teksan-main\\front\\user_input.py', 'front/'), ('H:\\Teksan-main\\.env', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='TekSan',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    uac_admin=True,
    icon=['H:\\Project\\Teksan\\icons\\teksan.ico'],
)
