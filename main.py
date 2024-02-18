import time
import button
import menu

value = ""
topic = ""
time_list = []
time_spent = 0

while value != "q":
    print("Press any key to count / press q to exit")
    value = input()

    if value != "q":
        time_spent = button.stopwatch()

        print("Do you want to save this time   y/n")
        save_time = input().lower()

        if save_time == "n":
            print("Time not saved")
            print(time_list)

        else:
            time_list.append(time_spent)
            print("Time Saved !!!")
            print(time_list)
