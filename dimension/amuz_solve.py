from zlib import decompress
from base64 import b64decode
import sys
sys.tracebacklimit = 0
sys.setrecursionlimit(65000)
getch = lambda: sys.stdin.read(1)
#================================
getch = lambda: ' '
_exec = exec
def exec(x):
    print(x.split("\n")[1:])
    _exec(x)
class Probe():
    def __init__(self):
        self.buffer = ''
    def __eq__(self, c):
        self.buffer += chr(c)
        return True
    def __del__(self):
        print(probe.buffer)
probe = Probe()
ord = lambda _: probe
#================================
exec(decompress(b64decode(s)).decode())
