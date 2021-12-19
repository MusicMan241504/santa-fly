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

a.datas += [('img_fhd\\sleigh.png',"C:\\Users\\Isaac\\Documents\\Coding\\Pygame\\santa-fly\\img_fhd\\sleigh.png","DATA")]

a.datas += [('img_fhd\\snowman.png',"C:\\Users\\Isaac\\Documents\\Coding\\Pygame\\santa-fly\\img_fhd\\snowman.png","DATA")]

a.datas += [('img_fhd\\tree.png',"C:\\Users\\Isaac\\Documents\\Coding\\Pygame\\santa-fly\\img_fhd\\tree.png","DATA")]
a.datas += [('img_fhd\\tree_s.png',"C:\\Users\\Isaac\\Documents\\Coding\\Pygame\\santa-fly\\img_fhd\\tree_s.png","DATA")]

a.datas += [('img_fhd\\house1.png',"C:\\Users\\Isaac\\Documents\\Coding\\Pygame\\santa-fly\\img_fhd\\house1.png","DATA")]
a.datas += [('img_fhd\\house2.png',"C:\\Users\\Isaac\\Documents\\Coding\\Pygame\\santa-fly\\img_fhd\\house2.png","DATA")]
a.datas += [('img_fhd\\house3.png',"C:\\Users\\Isaac\\Documents\\Coding\\Pygame\\santa-fly\\img_fhd\\house3.png","DATA")]
a.datas += [('img_fhd\\house4.png',"C:\\Users\\Isaac\\Documents\\Coding\\Pygame\\santa-fly\\img_fhd\\house4.png","DATA")]

a.datas += [('img_fhd\\present1.png',"C:\\Users\\Isaac\\Documents\\Coding\\Pygame\\santa-fly\\img_fhd\\present1.png","DATA")]
a.datas += [('img_fhd\\present2.png',"C:\\Users\\Isaac\\Documents\\Coding\\Pygame\\santa-fly\\img_fhd\\present2.png","DATA")]
a.datas += [('img_fhd\\present3.png',"C:\\Users\\Isaac\\Documents\\Coding\\Pygame\\santa-fly\\img_fhd\\present3.png","DATA")]
a.datas += [('img_fhd\\present4.png',"C:\\Users\\Isaac\\Documents\\Coding\\Pygame\\santa-fly\\img_fhd\\present4.png","DATA")]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='Santa Fly',
          icon='img_fhd\\icon.ico',
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
