# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['typo/lang/__main__.py'],
             pathex=['/mnt/c/Users/josia/MEGA/Projects/Other/Typo'],
             binaries=[],
             datas=[('./typo/lang/_quits.py', './typo/lang'), ('./typo/lang/_built_in_cmds.py', './typo/lang')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Typo Script',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
