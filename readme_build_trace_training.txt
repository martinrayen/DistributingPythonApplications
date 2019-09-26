(train) C:\Users\HP\DevEnv\Projects\VirtualEnvironment\Projects\VR\train>pyinstaller training.spec
93 INFO: PyInstaller: 3.5
93 INFO: Python: 3.7.3
109 INFO: Platform: Windows-10-10.0.17134-SP0
109 INFO: UPX is not available.
109 INFO: Extending PYTHONPATH with paths
['C:\\Users\\HP\\DevEnv\\Projects\\VirtualEnvironment\\Projects\\VR\\train',
 'C:\\Users\\HP\\DevEnv\\Projects\\VirtualEnvironment\\Projects\\VR\\train',
 'C:\\Users\\HP\\DevEnv\\Projects\\VirtualEnvironment\\Projects\\VR\\train']
109 INFO: checking Analysis
109 INFO: Building Analysis because Analysis-00.toc is non existent
109 INFO: Initializing module dependency graph...
109 INFO: Initializing module graph hooks...
124 INFO: Analyzing base_library.zip ...
2998 INFO: Analyzing hidden import 'sklearn.neighbors.typedefs'
3466 INFO: Processing pre-find module path hook   distutils
3466 INFO: distutils: retargeting to non-venv dir 'c:\\users\\hp\\anaconda3\\Lib\\distutils'
4451 INFO: Processing pre-find module path hook   site
4451 INFO: site: retargeting to fake-dir 'c:\\users\\hp\\devenv\\projects\\virtualenvironment\\projects\\VR\\train\\lib\\site-packages\\PyInstaller\\fake-modules'
5591 INFO: Processing pre-safe import module hook   setuptools.extern.six.moves
12044 INFO: Processing pre-safe import module hook   six.moves
16903 INFO: Analyzing hidden import 'sklearn.utils.sparsetools._graph_validation'
16903 ERROR: Hidden import 'sklearn.utils.sparsetools._graph_validation' not found
16903 INFO: Analyzing hidden import 'sklearn.utils.sparsetools._graph_tools'
16919 ERROR: Hidden import 'sklearn.utils.sparsetools._graph_tools' not found
16919 INFO: Analyzing hidden import 'sklearn.utils._cython_blas'
16919 INFO: Analyzing hidden import 'sklearn.neighbors.quad_tree'
16919 INFO: Analyzing hidden import 'sklearn.tree._utils'
16982 INFO: running Analysis Analysis-00.toc
16982 INFO: Adding Microsoft.Windows.Common-Controls to dependent assemblies of final executable
  required by c:\users\hp\devenv\projects\virtualenvironment\projects\VR\train\scripts\python.exe
17310 INFO: Caching module hooks...
17325 INFO: Analyzing training.py
30073 INFO: Analyzing classMLModelingPipeline.py
30089 INFO: Loading module hooks...
30089 INFO: Loading module hook "hook-distutils.py"...
30089 INFO: Loading module hook "hook-encodings.py"...
30247 INFO: Loading module hook "hook-lib2to3.py"...
30247 INFO: Loading module hook "hook-matplotlib.backends.py"...
31472 INFO:   Matplotlib backend "GTK3Agg": ignored
    cairo backend requires that pycairo>=1.11.0 or cairocffiis installed
32082 INFO:   Matplotlib backend "GTK3Cairo": ignored
    cairo backend requires that pycairo>=1.11.0 or cairocffiis installed
32845 INFO:   Matplotlib backend "MacOSX": ignored
    cannot import name '_macosx' from 'matplotlib.backends' (c:\users\hp\devenv\projects\virtualenvironment\projects\VR\train\lib\site-packages\matplotlib\backends\__init__.py)
33380 INFO:   Matplotlib backend "nbAgg": ignored
    No module named 'IPython'
33960 INFO:   Matplotlib backend "Qt4Agg": ignored
    Failed to import any qt binding
34481 INFO:   Matplotlib backend "Qt4Cairo": ignored
    cairo backend requires that pycairo>=1.11.0 or cairocffiis installed
35027 INFO:   Matplotlib backend "Qt5Agg": ignored
    Failed to import any qt binding
35534 INFO:   Matplotlib backend "Qt5Cairo": ignored
    cairo backend requires that pycairo>=1.11.0 or cairocffiis installed
36226 INFO:   Matplotlib backend "TkAgg": added
36920 INFO:   Matplotlib backend "TkCairo": ignored
    cairo backend requires that pycairo>=1.11.0 or cairocffiis installed
37578 INFO:   Matplotlib backend "WebAgg": added
38289 INFO:   Matplotlib backend "WX": added
39015 INFO:   Matplotlib backend "WXAgg": added
39552 INFO:   Matplotlib backend "WXCairo": ignored
    cairo backend requires that pycairo>=1.11.0 or cairocffiis installed
40065 INFO:   Matplotlib backend "agg": added
40575 INFO:   Matplotlib backend "cairo": ignored
    cairo backend requires that pycairo>=1.11.0 or cairocffiis installed
41249 INFO:   Matplotlib backend "pdf": added
41922 INFO:   Matplotlib backend "pgf": added
42427 INFO:   Matplotlib backend "ps": added
42944 INFO:   Matplotlib backend "svg": added
43597 INFO:   Matplotlib backend "template": added
44128 INFO: Loading module hook "hook-matplotlib.py"...
44574 INFO: Loading module hook "hook-numpy.core.py"...
44777 INFO: MKL libraries found when importing numpy. Adding MKL to binaries
44777 INFO: Loading module hook "hook-numpy.py"...
44793 INFO: Loading module hook "hook-pandas.py"...
46373 INFO: Loading module hook "hook-PIL.Image.py"...
46765 INFO: Loading module hook "hook-PIL.py"...
46781 INFO: Excluding import 'tkinter'
46781 INFO:   Removing import of tkinter from module PIL.ImageTk
46781 INFO: Excluding import 'PyQt5'
46781 INFO:   Removing import of PyQt5 from module PIL.ImageQt
46781 INFO: Import to be excluded not found: 'FixTk'
46781 INFO: Excluding import 'PySide'
46797 INFO:   Removing import of PySide from module PIL.ImageQt
46797 INFO: Excluding import 'PyQt4'
46797 INFO:   Removing import of PyQt4 from module PIL.ImageQt
46797 INFO: Loading module hook "hook-PIL.SpiderImagePlugin.py"...
46812 INFO: Excluding import 'tkinter'
46812 INFO: Import to be excluded not found: 'FixTk'
46812 INFO: Loading module hook "hook-pkg_resources.py"...
47124 INFO: Processing pre-safe import module hook   win32com
47483 INFO: Loading module hook "hook-pydoc.py"...
47483 INFO: Loading module hook "hook-pythoncom.py"...
47796 INFO: Loading module hook "hook-pytz.py"...
47895 INFO: Loading module hook "hook-pywintypes.py"...
48197 INFO: Loading module hook "hook-scipy.io.matlab.py"...
48197 INFO: Loading module hook "hook-scipy.linalg.py"...
48197 INFO: Loading module hook "hook-scipy.py"...
48212 INFO: Loading module hook "hook-scipy.sparse.csgraph.py"...
48212 INFO: Loading module hook "hook-scipy.special._ellip_harm_2.py"...
48212 INFO: Loading module hook "hook-scipy.special._ufuncs.py"...
48212 INFO: Loading module hook "hook-setuptools.py"...
48862 INFO: Loading module hook "hook-sklearn.metrics.cluster.py"...
48862 WARNING: Hidden import "sklearn.utils.sparsetools._graph_validation" not found!
48878 WARNING: Hidden import "sklearn.utils.sparsetools._graph_tools" not found!
48878 INFO: Loading module hook "hook-sklearn.py"...
c:\users\hp\devenv\projects\virtualenvironment\projects\VR\train\lib\site-packages\sklearn\externals\joblib\__init__.py:15: DeprecationWarning: sklearn.externals.joblib is deprecated in 0.21 and will be removed in 0.23. Please import this functionality directly from joblib, which can be installed with: pip install joblib. If this warning is raised when loading pickled models, you may need to re-serialize those models with scikit-learn 0.21+.
  warnings.warn(msg, category=DeprecationWarning)
57293 INFO: Loading module hook "hook-sqlite3.py"...
57404 INFO: Loading module hook "hook-sysconfig.py"...
57404 INFO: Loading module hook "hook-win32com.py"...
57826 INFO: Loading module hook "hook-xml.dom.domreg.py"...
57826 INFO: Loading module hook "hook-xml.etree.cElementTree.py"...
57826 INFO: Loading module hook "hook-xml.py"...
57826 INFO: Loading module hook "hook-_tkinter.py"...
58045 INFO: checking Tree
58048 INFO: Building Tree because Tree-00.toc is non existent
58048 INFO: Building Tree Tree-00.toc
58134 INFO: checking Tree
58134 INFO: Building Tree because Tree-01.toc is non existent
58138 INFO: Building Tree Tree-01.toc
58372 INFO: Looking for ctypes DLLs
58435 INFO: Analyzing run-time hooks ...
58466 INFO: Including run-time hook 'pyi_rth_mplconfig.py'
58466 INFO: Including run-time hook 'pyi_rth_mpldata.py'
58466 INFO: Including run-time hook 'pyi_rth__tkinter.py'
58466 INFO: Including run-time hook 'pyi_rth_multiprocessing.py'
58482 INFO: Including run-time hook 'pyi_rth_pkgres.py'
58482 INFO: Including run-time hook 'pyi_rth_win32comgenpy.py'
58544 INFO: Looking for dynamic libraries
58654 WARNING: lib not found: tbb.dll dependency of c:\users\hp\anaconda3\Library\bin\mkl_tbb_thread.dll
58732 WARNING: lib not found: msmpi.dll dependency of c:\users\hp\anaconda3\Library\bin\mkl_blacs_msmpi_lp64.dll
58888 WARNING: lib not found: mpich2mpi.dll dependency of c:\users\hp\anaconda3\Library\bin\mkl_blacs_mpich2_ilp64.dll
59638 WARNING: lib not found: mpich2mpi.dll dependency of c:\users\hp\anaconda3\Library\bin\mkl_blacs_mpich2_lp64.dll
59982 WARNING: lib not found: msmpi.dll dependency of c:\users\hp\anaconda3\Library\bin\mkl_blacs_msmpi_ilp64.dll
60325 WARNING: lib not found: impi.dll dependency of c:\users\hp\anaconda3\Library\bin\mkl_blacs_intelmpi_lp64.dll
60403 WARNING: lib not found: impi.dll dependency of c:\users\hp\anaconda3\Library\bin\mkl_blacs_intelmpi_ilp64.dll
60528 WARNING: lib not found: pgf90rtl.dll dependency of c:\users\hp\anaconda3\Library\bin\mkl_pgi_thread.dll
60606 WARNING: lib not found: pgf90.dll dependency of c:\users\hp\anaconda3\Library\bin\mkl_pgi_thread.dll
60653 WARNING: lib not found: pgc14.dll dependency of c:\users\hp\anaconda3\Library\bin\mkl_pgi_thread.dll
62606 INFO: Looking for eggs
62606 INFO: Using Python library c:\users\hp\devenv\projects\virtualenvironment\projects\VR\train\scripts\python37.dll
62606 INFO: Found binding redirects:
[]
62716 INFO: Warnings written to C:\Users\HP\DevEnv\Projects\VirtualEnvironment\Projects\VR\train\build\training\warn-training.txt
63216 INFO: Graph cross-reference written to C:\Users\HP\DevEnv\Projects\VirtualEnvironment\Projects\VR\train\build\training\xref-training.html
63481 INFO: checking PYZ
63481 INFO: Building PYZ because PYZ-00.toc is non existent
63481 INFO: Building PYZ (ZlibArchive) C:\Users\HP\DevEnv\Projects\VirtualEnvironment\Projects\VR\train\build\training\PYZ-00.pyz
69842 INFO: Building PYZ (ZlibArchive) C:\Users\HP\DevEnv\Projects\VirtualEnvironment\Projects\VR\train\build\training\PYZ-00.pyz completed successfully.
69951 INFO: checking PKG
69951 INFO: Building PKG because PKG-00.toc is non existent
69951 INFO: Building PKG (CArchive) PKG-00.pkg
70029 INFO: Building PKG (CArchive) PKG-00.pkg completed successfully.
70029 INFO: Bootloader c:\users\hp\devenv\projects\virtualenvironment\projects\VR\train\lib\site-packages\PyInstaller\bootloader\Windows-64bit\run.exe
70045 INFO: checking EXE
70045 INFO: Building EXE because EXE-00.toc is non existent
70045 INFO: Building EXE from EXE-00.toc
70045 INFO: Appending archive to EXE C:\Users\HP\DevEnv\Projects\VirtualEnvironment\Projects\VR\train\build\training\training.exe
70232 INFO: Building EXE from EXE-00.toc completed successfully.
70263 INFO: checking COLLECT
70263 INFO: Building COLLECT because COLLECT-00.toc is non existent
70263 INFO: Building COLLECT COLLECT-00.toc
92006 INFO: Building COLLECT COLLECT-00.toc completed successfully.
