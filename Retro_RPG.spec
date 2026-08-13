# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# 收集项目中的所有资源文件
a = Analysis(
    ['Retro_RPG.pyw'],
    pathex=[],
    binaries=[],
    datas=[
        ('icon.ico', '.'),   # Windows 图标
        ('icon.icns', '.'),  # macOS 图标 ← 新增
    ],
    hiddenimports=[
        'tkinter',
        'tkinter.ttk',
        'tkinter.messagebox',
        'tkinter.simpledialog',
        'tkinter.scrolledtext',
        'json',
        'zlib',
        'base64',
        'hashlib',
        'random',
        'threading',
        'datetime',
        'time',
        'os',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyd = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyd,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Retro_RPG',
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
    icon='icon.ico'         # Windows 可执行文件的图标
)

app = BUNDLE(
    exe,
    name='Retro_RPG.app',
    icon='icon.icns',        # ← 改这里：.app 的图标用 .icns
    bundle_identifier='com.xiaoyu.retrorpg',
    info_plist={
        'CFBundleName': 'Retro_RPG',
        'CFBundleDisplayName': 'Retro_RPG',
        'CFBundleVersion': '2.2.6',
        'CFBundleShortVersionString': '2.2.6',
        'CFBundleIdentifier': 'com.xiaoyu.retrorpg',
        'NSHighResolutionCapable': True,
    }
)