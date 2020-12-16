import  threading
import time


def fun1(a):
    for i in range(65, 95):
        print(threading.current_thread().getName(),i)
        #threading.current_thread()获取当前线程对象，getName()获取房钱对象的名字。
        time.sleep(a)
def fun2(b):
    for i in range(65, 85):
        print(threading.current_thread().getName(),chr(i))
        time.sleep(b)
thread1 = threading.Thread(target = fun1(0.02),name = '线程1：')#创建线程对象
thread2 = threading.Thread(target = fun2(0.02),name = '线程2：')#创建线程对象
thread1.start()
thread2.start()
#MainThread代表主线程,只要是fun1()这种形式的，不管fun1()里面有没有参数，都是
#显示MainThread。

print()



thread1 = threading.Thread(target = fun1,args=(0.01,),name = '线程1：')#创建线程对象
thread2 = threading.Thread(target = fun2,args=(0.01,),name = '线程2：')#创建线程对象
thread1.start()
thread2.start()
