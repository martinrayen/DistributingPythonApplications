1. Install virtualenv module in python.
   C:\Users\JM> pip install virtualenv
2. Navigate to the virtual environment folder using cmd prompt.
   C:\Users\JM> cd \Users\JM\VirtualEnvironment\Projects\TestApp\
3. Create the virtual environment.
   C:\Users\JM\VirtualEnvironment\Projects\TestApp>virtualenv testApp
4. Activate the virtual environment.
   C:\Users\JM\VirtualEnvironment\Projects\TestApp\testApp>"C:\Users\JM\VirtualEnvironment\Projects\TestApp\testApp\Scripts\activate.bat"
   (testApp) C:\Users\JM\VirtualEnvironment\Projects\TestApp\testApp>
5. Install pyinstaller module.
   (testApp) C:\Users\JM\VirtualEnvironment\Projects\TestApp\testApp>pip install pyinstaller
6. Place the "classMLModelling.py" and "SampleApp.py" files in this folder "C:\Users\JM\VirtualEnvironment\Projects\TestApp\testApp\"
7. Call the pyinstaller module to convert the Sample.py file into an executable. classMLModelling.py is internally referenced in SampleApp.py file.
   (testApp) C:\Users\JM\VirtualEnvironment\Projects\TestApp\testApp>pyinstaller SampleApp.py
8. Once done, the installer created a spec file named SampleApp.spec in the current working directory.
9. Edit this file and change the following code,
   include class 'classMLModelingPipeline.py'
   include sklearn related modules in hiddenimports   :
   a = Analysis(['SampleApp.py','classMLModelingPipeline.py'],
             pathex=['C:\\Users\\JM\\VirtualEnvironment\\Projects\\TestApp\\testApp'],
             binaries=[],
             datas=[],
             hiddenimports=['cython', 'sklearn', 'sklearn.ensemble', 'sklearn.neighbors.typedefs', 'sklearn.neighbors.quad_tree', 'sklearn.tree._utils'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
10. Call the pyinstaller module to convert the Sample.py file into an executable using the .spec file.
    (testApp) C:\Users\JM\VirtualEnvironment\Projects\TestApp\testApp>pyinstaller SampleApp.spec
11. The executable will be created along with other dependencies in the folder : 
    "C:\Users\JM\VirtualEnvironment\Projects\TestApp\testApp\dist\testApp\testApp.exe".
12. Run the executable and verify, if all good.
    C:\Users\JM\VirtualEnvironment\Projects\TestApp\testApp\dist\testApp>testApp<Press Enter Key>
