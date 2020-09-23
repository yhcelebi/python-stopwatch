import time
import datetime


class Stopwatch:
    @staticmethod
    def stopwatch():

        global stopwatch_format
        stopwatch_format = "stopwatch format yy:mm:dd:hh:mm:ss"

        global times_up
        times_up = "Time's Up!"

        print("")
        print(f"Today's Date: {time.ctime()}")
        print(stopwatch_format)

        while (True):

            stopwatch = input(">>> ")
            split_stopwatch = stopwatch.split(":")

            if len(stopwatch) == 1 or len(stopwatch) == 2:
                for q in range(int(stopwatch), 0, -1):
                    print(q)
                    time.sleep(1)
                    continue
                    print(times_up)
                    print("")
                    print(stopwatch_format)

            elif len(stopwatch) == 4 or len(stopwatch) == 5 or len(stopwatch) == 6:
                for q in range(int((split_stopwatch[0] * 60) + split_stopwatch[1]), 0, -1):
                    step = []
                    step.append(q)
                    print(f"{q[0]}:{q[1]}{q[2]}")
                    time.sleep(1)
                    continue
                    print(times_up)
                    print("")
                    print(stopwatch_format)

            elif stopwatch == "quit":
                quit()

            else:
                print("")
                print(stopwatch_format)
                continue



Stopwatch.stopwatch()