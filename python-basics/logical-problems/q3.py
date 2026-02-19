import time

s = input("press Enter to start the stopwatch: ")
start_time = time.time()
e = input("press Enter to stop the stopwatch: ")
end_time = time.time()

elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time} seconds")
