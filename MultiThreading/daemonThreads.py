import logging
import threading
import time


def thread_function(name):
    print("Thread {}: starting".format(name))
    time.sleep(2)
    print("Thread {}: finishing".format(name))


# main
print("Main    : before creating thread")
x = threading.Thread(target=thread_function, args=(1, ), daemon=True)
# x = threading.Thread(target=thread_function, args=(1, ), daemon=False)
print("Main    : before running thread")
x.start()
print("Main    : wait for the thread to finish")
print("Main    : all done")



# since x is daemon thread, program ends just after main is over, not waiting for the thread to complete