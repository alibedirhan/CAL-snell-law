# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['SnellLaw.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'numpy',
        'numpy.core',
        'numpy.core._methods',
        'numpy.lib.format',
        'numpy.random',
        'matplotlib',
        'matplotlib.backends',
        'matplotlib.backends.backend_tkagg',
        'matplotlib.figure',
        'matplotlib.pyplot',
        'tkinter',
        'tkinter.messagebox',
        'pkg_resources.py2_warn'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['scipy', 'pandas', 'IPython'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='SnellKanuluSimulatoru',
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
)
