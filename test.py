import ctypes.wintypes
from msilib import Directory
import os

CSIDL_PERSONAL = 5       # My Documents
SHGFP_TYPE_CURRENT = 0   # Get current, not default value

dir = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, dir)

docs = str(dir.value)
directory = docs + "\\NEURO INNOVA KIDS"

if not os.path.exists(directory):
    os.makedirs(directory)