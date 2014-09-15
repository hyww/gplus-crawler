import configure
from cx_Freeze import setup, Executable

# base = None
# if sys.platform == "win32":
    # base = "Win32GUI"

copyDependentFiles=True
silent = True

# includes = ["lxml", "lxml._elementpath", "lxml.etree",
#             "gzip", "encodings.utf_8", "encodings.ascii"]
includes = ["encodings.utf_8", "encodings.ascii",
            "os", "re", "sys", "urllib", "urllib2",
            "threading", "contextlib", "logging", "wx"]

setup(name='gplus_crawler',
     version = configure.VERSION,
     options = {
       "build_exe" : {
           "includes": includes,
           "include_msvcr": True,
           },
       },
     executables=[Executable('start_ui.py')],
 )