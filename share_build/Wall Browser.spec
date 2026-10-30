# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['../wall_browser.py'],
    pathex=[],
    binaries=[],
    datas=[('wall_icon.png', '.')],
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
    [],
    exclude_binaries=True,
    name='Wall Browser',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['/var/folders/l9/ngcjd5wn0sg_mpx8msb7snq00000gn/T/tmp.NQzueTzM/WallIcon.icns'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Wall Browser',
)
app = BUNDLE(
    coll,
    name='Wall Browser.app',
    icon='/var/folders/l9/ngcjd5wn0sg_mpx8msb7snq00000gn/T/tmp.NQzueTzM/WallIcon.icns',
    bundle_identifier='com.wallbrowser.app',
)
