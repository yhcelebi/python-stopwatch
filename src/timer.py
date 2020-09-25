import time
from datetime import datetime

# TODO-1: ask the scope outside to for loop

now = datetime.now()
ctime = now.strftime("%H:%M:%S")

print("")
print(f"Time: {ctime}")
print("stopwatch format hh:mm:ss")

while True:

    timer = input(">>> ")
    split_timer = timer.split(":")
    int_list = []
    for e in split_timer:
        a = int(e)
        int_list.append(a)

    if len(timer) == 1 or len(timer) == 2:
        for q in range(int(timer), 0, -1):
            print(time.strftime('%H:%M:%S', time.gmtime(q)))
            time.sleep(1)
        print("Time's Up!")
        print("")
        print("stopwatch format hh:mm:ss")

    elif len(timer) == 4 or len(timer) == 5:
        for q in range(int_list[0] * 60 + int_list[1], 0, -1):
            print(time.strftime('%H:%M:%S', time.gmtime(q)))
            time.sleep(1)
        print("Time's Up!")
        print("")
        print("stopwatch format hh:mm:ss")

    elif len(timer) == 7 or len(timer) == 8:
        for q in range((((int_list[0] * 60) + int_list[1]) * 60) + int_list[2], 0, -1):
            print(time.strftime('%H:%M:%S', time.gmtime(q)))
            time.sleep(1)
        print("Time's Up!")
        print("")
        print("stopwatch format hh:mm:ss")

    elif timer == "help":
        print("type it don't be scared")

    elif timer == "quit":
        quit()

    else:
        print("")
        print("stopwatch format hh:mm:ss")
        print("please enter a valid value")
        continue
