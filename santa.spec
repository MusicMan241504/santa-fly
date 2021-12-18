# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['santa.py'],
             pathex=['C:\\Users\\Isaac\\Documents\\Coding\\Pygame\\santa-fly'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += [('img\\sleigh.png',"C:\\Users\\Isaac\\Documents\\Coding\\Pygame\\santa-fly\\img\\sleigh.png","DATA")]
a.datas += [('img\\snowman.png',"C:\\Users\\Isaac\\Documents\\Coding\\Pygame\\santa-fly\\img\\snowman.png","DATA")]
a.datas += [('img\\tree.png',"C:\\Users\\Isaac\\Documents\\Coding\\Pygame\\santa-fly\\img\\tree.png","DATA")]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='santa',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Santa Fly')
