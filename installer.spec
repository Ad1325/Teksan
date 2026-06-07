# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    [r"H:\Project\Teksan\front\main.py"],
    pathex=[r"H:\Project\Teksan\front"],
    binaries=[],
    datas=[
        (r"H:\Project\Teksan\icons", "icons"),
        (r"H:\Project\Teksan\fonts", "fonts"),
        (r"H:\TekSan-main\front\dns_changer.py", "."),
        (r"H:\TekSan-main\front\conversation.py", "."),
        (r"H:\Project\Teksan\front\option_files.py", "."),
        (r"H:\Project\Teksan\front\sidebar.py", "."),
        (r"H:\Project\Teksan\front\user_input.py.", "."),
        (r"H:\Project\Teksan\front\.env", "."),
        (r"H:\Project\Teksan\front\teksan.ico", ".")

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
    manifest=r"manifest.xml",
    runtime_tmpdir=None,
    console=False,
    icon=r"H:\Project\Teksan\icons\teksan.ico",
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
