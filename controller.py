import time
import random
import subprocess
import likes

while True:
    print(f'Start process')
    likes.main()
    workedTime = int(open('time.txt', 'r').read())
    print(f'Worked time {workedTime} sec / {workedTime / 3600} hrs')

    delayTime = random.randint(86400 - workedTime, 86400)
    print(f"Delay {str(int(delayTime / 3600))} hrs")
    time.sleep(delayTime)
