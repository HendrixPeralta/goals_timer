import time


def stopwatch():

    value = ""

    start_time = time.time()
    print("Time running //")
    print("Press enter to finish the stopwatch")
    value = input()
    total_time = round((time.time() - start_time), 2)

    print("total time " + str(total_time) + "s")
    print("*" * 20)
    # finish_time = time.time()
    print("exercise complete")

    return total_time

class button:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Button Name: {self.name}"

