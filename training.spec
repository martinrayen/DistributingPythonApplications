# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['training.py','classMLModelingPipeline.py'],
             pathex=['C:\\Users\\HP\\DevEnv\\Projects\\VirtualEnvironment\\Projects\\VendorRanking\\train'],
             binaries=[],
             datas=[],
             hiddenimports=['sklearn.neighbors.typedefs','sklearn.utils.sparsetools._graph_validation','sklearn.utils.sparsetools._graph_tools','sklearn.utils._cython_blas','sklearn.neighbors.quad_tree','sklearn.tree._utils'],
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
          [('W ignore', None, 'OPTION')],
          exclude_binaries=True,
          name='training',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='training')
