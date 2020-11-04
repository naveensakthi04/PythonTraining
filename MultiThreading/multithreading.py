from threading import *
from time import sleep


# extending the thread class
class Hello(Thread):
    # can only override run(self) or init(self)
    def run(self):
        for i in range(5):
            print(current_thread().getName(), "Hello")
            sleep(0.5)

    def __init__(self):
        super().__init__()
        print("Init of Hello")


# thread without extending thread class
class Hi:
    def run(self):
        for i in range(5):
            print(current_thread().getName(), "Hi")
            sleep(1)


# no class
def some_method():
    for i in range(5):
        print(current_thread().getName(), "Something")
        sleep(0.5)


# main()
thread_without_class = Thread(target=some_method)
thread_extending_thread_class = Hello()
thread_without_extending_thread_class = Thread(target=Hi().run)

thread_without_class.start()
thread_extending_thread_class.start()
thread_without_extending_thread_class.start()


thread_extending_thread_class.join()
thread_without_extending_thread_class.join()
thread_without_class.join()


print(current_thread().getName(), "Bye")
