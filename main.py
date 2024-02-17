import time

value = ""
topic = ""
print("Press enter when you start studying")

# while value.lower() != "q":
#     value = input()
#
#     total_time = round((time.time() - start_time), 2)
#
#     print("You Finished !")
#     print("total time " + str(total_time))
#
#     print("*"*20)
#     #finish_time = time.time()
#
#
# print("exercise complete")

value = input()
start_time = time.time()
print("Time running //")


value = input()
total_time = round((time.time() - start_time), 2)

print("This is the total time for:" + str(topic))
print("total time " + str(total_time) + "s")

print("*" * 20)
# finish_time = time.time()

print("exercise complete")
