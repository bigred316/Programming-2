import time
import threading as th
def print_nums(start, end, delay):
    for i in range(start, end):
        time.sleep(delay)
        print(i, "")

def print_letters(delay):
    for letter in "abcdefghijklmnopqrtuvwxyz":
        time.sleep(delay)
        print(letter)

t1 = th.Thread(target=print_nums, args=(1,11, 0.5))
t2 = th.Thread(target=print_nums, args=(11,21, 0.5))

#t2 = th.Thread(target=print_letters, args=(0.25,)).start()
t1.start()
t2.start()
#wait for threads to finish

t1.join()
t2.join()
