
from datetime import datetime

file_path = "file/path.py"
h = 4 # Witch hour
m = 0 # Witch minute
s = 0 # Witch second
# ex: at 4:30:00 am 

once = 0 # don't change that
def executer():
    exec(open(file_path).read())   
while True:
    if h == datetime.now().hour:
        if m == datetime.now().minute:
            if s == datetime.now().second:
                if once==0:
                    once = 1
                    executer()
                else:
                    once = 0