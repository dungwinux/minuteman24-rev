
from zlib import compress
import base64

prog_list = []

# for x in range(1, 4):
#     name = f"amuz_stage{x}.py"
#     with open(name, "r") as fd:
#         prog_list.append(fd.read())

flag = """The consistency paradox or grandfather paradox occurs when the past is changed in any way, thus creating a contradiction. A common example given is traveling to the past and intervening with the conception of one's ancestors (such as causing the death of the parent beforehand), thus affecting the conception of oneself. If the time traveler were not born, then it would not be possible for the traveler to undertake such an act in the first place. Therefore, the ancestor lives to offspring the time traveler's next-generation ancestor, and eventually the time traveler. There is thus no predicted outcome to this.


STAY


MINUTEMAN{38.8355556,-104.6975000}"""

# flag = "test"

final_prog = "print('Congrats')"

gen_prog = lambda c, x = 0: f'''exit({x}) if len(ch:=getch())!=1 or ord(ch)!={c} else '''

main_prog = [gen_prog(ord(c), i) for i, c in enumerate(flag)]

pre_prog = '''
from zlib import decompress
from base64 import b64decode
import sys
sys.tracebacklimit = 0
sys.setrecursionlimit(65000)
getch = lambda: sys.stdin.read(1)
'''

prog_list = [pre_prog] + main_prog

prog = final_prog
for x, outer_prog in enumerate(reversed(prog_list)):
    print(x/len(prog_list))
    prog = f"s=" + str(base64.b64encode(compress(prog.encode(), 6))) + '\n' + outer_prog + f"exec(decompress(b64decode(s)).decode())"

with open("dimension.py", "w") as fd:
    fd.write(prog)
