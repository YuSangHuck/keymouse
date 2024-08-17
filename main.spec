# -*- mode: python ; coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath('.'))  # 현재 디렉토리를 PYTHONPATH에 추가

from PyInstaller.utils.hooks import collect_data_files
from config import PROGRAM_NAME

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=collect_data_files('win10toast'),
    hiddenimports=['win10toast', 'pkg_resources', 'pkg_resources.py2_warn'],
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
    name=PROGRAM_NAME,
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
