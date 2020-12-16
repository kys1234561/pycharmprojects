import threading

def fun1():
    for i in range(10):
        if i == 5:
            thread2 = threading.Thread(target=fun2,name='线程2')
            thread2.start()
            thread2.join()
        print(threading.current_thread().getName(), i)

def fun2():
    for i in range(65,68):
        print(threading.current_thread().getName(),chr(i))


thread1 = threading.Thread(target=fun1,name='线程1 ')
thread1.start()