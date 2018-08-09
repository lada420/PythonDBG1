from ctypes import *
from defines import *

import sys
import time
kernel32 = windll.kernel32

class debugger():
    def __init__(self):
        pass
    def load(self, path_to_exe):
        creation_flags = DEBUG_PROCESS
        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()

        startupinfo.dwFlags = 0x1
        startupinfo.wShowWIndow = 0x0

        startupinfo.cb = sizeof(startupinfo)
        if kernel32.CreateProcessA(path_to_exe,
                                    None,
                                    None,
                                    None,
                                    None,
                                    creation_flags,
                                    None,
                                    None,
                                    byref(startupinfo),
                                    byref(process_information)):
            print("[*] We have succsefully launched your process!")
            print("[*] The Process ID I have is: %d" %process_information.dwProcessID)
        else:
            print("[*] Error with error code %d" %kernel32.GetLastError())
