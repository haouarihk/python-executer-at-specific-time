import os
import time
from datetime import datetime


file_path = "file/path.py"
h = 4 # Witch hour
m = 30 # Witch minute
s = 0 # Witch second
# ex: at 4:30:00 am 


def main():
    while True:
        local_time = datetime.now()

        if h == local_time.hour:
            if m == local_time.minute:
                if s == local_time.second:
                    # Execute file with python command
                    # Note: Maybe you need to change "python"
                    # to "python3"
                    os.system(f"python {file_path}")

        time.sleep(1)

if __name__ == "__main__":
    main()
