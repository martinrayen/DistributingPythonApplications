# -*- mode: python ; coding: utf-8 -*-
'''============================================================================ 
Connect as admin, when peforming the build using virtual environment
and pyinstaller using the command prompt.
Use virtualenv module 16.0.1
Add to the system path : C:\Users\HP\AppData\Roaming\Python\Python37\Scripts
============================================================================'''
          
#===== Installed modules on virtual machine "train" ==========================================================
pip list --local
'''
-------------------------
Package         Version
-------------------------
altgraph        0.16.1
cycler          0.10.0
Cython          0.29.13
future          0.17.1
joblib          0.13.2
kiwisolver      1.1.0
matplotlib      3.1.1
numpy           1.17.2
pandas          0.25.1
pefile          2019.4.18
Pillow          6.1.0
pip             19.2.3
PyInstaller     3.5
pyparsing       2.4.2
pypiwin32       223
python-dateutil 2.8.0
pytz            2019.2
pywin32         225
pywin32-ctypes  0.2.0
scikit-learn    0.21.3
scipy           1.3.1
seaborn         0.9.0
setuptools      41.2.0
six             1.12.0
sklearn         0.0
tornado         6.0.3
wheel           0.33.6
wxPython        4.0.6
xlrd            1.2.0
-------------------------
'''
'===== Batch file to install the required modules ======='''
pip install numpy
pip install pandas
pip install wxpython
pip install sklearn
pip install seaborn
pip install matplotlib
pip install xlrd
pip install tornado
pip install pywin32
pip install pypiwin32
pip install cython
pip install numpy
'========================================================='''

#=============================================================================================================
#===== training.spec file ====================================================================================
block_cipher = None
a = Analysis(['training.py','classMLModelingPipeline.py'],
             pathex=['C:\\Users\\JM\\DevEnv\\Projects\\VirtualEnvironment\\Projects\\vrs\\train'],
             binaries=[],
             datas=[],
             hiddenimports=['sklearn.neighbors.typedefs',
                            'sklearn.utils.sparsetools._graph_validation',
                            'sklearn.utils.sparsetools._graph_tools',
                            'sklearn.utils._cython_blas',
                            'sklearn.neighbors.quad_tree',
                            'sklearn.tree._utils'],
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
#=============================================================================================================
#======= Hook files for pyinstaller ==========================================================================
PATH : C:\Users\JM\DevEnv\Projects\VirtualEnv\Projects\VRS\train\Lib\site-packages\PyInstaller\hooks
'''======= hook-scipy ======================================================'''
# -----------------------------------------------------------------------------
# Copyright (c) 2013-2019, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
# -----------------------------------------------------------------------------

import os
import glob
from PyInstaller.utils.hooks import get_module_file_attribute
from PyInstaller.compat import is_win

binaries = []

# package the DLL bundle that official scipy wheels for Windows ship
if is_win:
    dll_glob = os.path.join(os.path.dirname(
        get_module_file_attribute('scipy')), 'extra-dll', "*.dll")
    if glob.glob(dll_glob):
        binaries.append((dll_glob, "."))

# collect library-wide utility extension modules
hiddenimports = ['scipy._lib.%s' % m for m in [
    'messagestream', "_ccallback_c", "_fpumode"]]
'''========================================================================='''
'''======== hook-sklearn ==================================================='''
from PyInstaller.utils.hooks import collect_submodules
#from hookutils import collect_submodules
hiddenimports = collect_submodules('sklearn')
'''========================================================================='''
'''======== hook-sklearn.metrics.cluster ==================================='''
#-----------------------------------------------------------------------------
# Copyright (c) 2014-2019, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

# Tested on Windows 7 64bit with scikit-learn 0.17 and Python 2.7
hiddenimports = ['sklearn.utils.sparsetools._graph_validation',
                 'sklearn.utils.sparsetools._graph_tools',
                 'sklearn.utils.lgamma',
                 'sklearn.utils.weight_vector']
'''========================================================================='''

#=============================================================================================================