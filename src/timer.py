import time

# TODO-1: ask the scope outside to for loop

print("")
print(f"Today's Date: {time.ctime()}")
print("stopwatch format yy:mm:ww:dd:hh:mm:ss")

while True:

    timer = input(">>> ")
    split_timer = timer.split(":")
    int_list = []
    for e in split_timer:
        a = int(e)
        int_list.append(a)

    if len(timer) == 1 or len(timer) == 2:
        for q in range(int(timer), 0, -1):
            print(q)
            time.sleep(1)
        print("Time's Up!")
        print("")
        print("stopwatch format yy:mm:ww:dd:hh:mm:ss")

    elif len(timer) == 4 or len(timer) == 5:
        for q in range(int_list[0] * 60 + int_list[1], 0, -1):
            print(q)
            time.sleep(1)
        print("Time's Up!")
        print("")
        print("stopwatch format yy:mm:ww:dd:hh:mm:ss")

    elif len(timer) == 7 or len(timer) == 8:
        for q in range(int_list[0] * 60 + int_list[1] * 60 + int_list[2], 0, -1):
            print(q)
            time.sleep(1)
        print("Time's Up!")
        print("")
        print("stopwatch format yy:mm:ww:dd:hh:mm:ss")

    elif len(timer) == 10 or len(timer) == 11:
        for q in range(int_list[0] * 24 + int_list[1] * 60 + int_list[2] * 60 + int_list[3], 0, -1):
            print(q)
            time.sleep(1)
        print("Time's Up!")
        print("")
        print("stopwatch format yy:mm:ww:dd:hh:mm:ss")

    elif len(timer) == 13 or len(timer) == 14:
        for q in range(int_list[0] * 7 + int_list[1] * 24 + int_list[2] * 60 + int_list[3] * 60 + int_list[4], 0, -1):
            print(q)
            time.sleep(1)
        print("Time's Up!")
        print("")
        print("stopwatch format yy:mm:ww:dd:hh:mm:ss")

    elif len(timer) == 16 or len(timer) == 17:
        for q in range(int_list[0] * 4 + int_list[1] * 7 + int_list[2] * 24 + int_list[3] * 60 + int_list[4] * 60 + int_list[5], 0, -1):
            print(q)
            time.sleep(1)
        print("Time's Up!")
        print("")
        print("stopwatch format yy:mm:ww:dd:hh:mm:ss")

    elif len(timer) == 19 or len(timer) == 20:
        for q in range(int_list[0] * 365 + 6 + int_list[3] * 24 + int_list[4] * 60 + int_list[5] * 60 + int_list[6], 0, -1):
            print(q)
            time.sleep(1)
        print("Time's Up!")
        print("")
        print("stopwatch format yy:mm:ww:dd:hh:mm:ss")

    elif timer == "help":
        print("type it don't be scared")

    elif timer == "quit":
        quit()

    else:
        print("")
        print("stopwatch format yy:mm:ww:dd:hh:mm:ss")
        print("please enter a valid value")
        continue
