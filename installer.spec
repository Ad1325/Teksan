# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    [r"H:\Teksan-main\front\main.py"],
    pathex=[r"H:\Teksan-main\front"],
    binaries=[],
    datas=[
        (r"H:\Teksan-main\icons", "icons"),
        (r"H:\Teksan-main\fonts", "fonts"),
        (r"H:\TekSan-main\front\dns_changer.py", "front"),
        (r"H:\TekSan-main\front\conversation.py", "front"),
        (r"H:\Teksan-main\front\option_files.py", "front"),
        (r"H:\Teksan-main\front\sidebar.py", "front"),
        (r"H:\Teksan-main\front\user_input.py.", "front"),
        (r"H:\Teksan-main\.env", "."),
        (r"H:\Teksan-main\front\teksan.ico", "front")

    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="TekSan",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon=r"H:\TekSan-main\front\teksan.ico",
    uac_admin=True
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="TekSan"
)
