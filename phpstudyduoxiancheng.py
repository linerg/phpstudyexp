# -*- coding:utf-8 -*-
# author:f0ngf0ng
import threading
import time
from queue import Queue
import requests

event = threading.Event()
event.set()
q = Queue(0)
s = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
exitFlag = 0

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Charset': 'c3lzdGVtKCduc2xvb2t1cCB3d3cuYmFpZHUuY29tJyk7'
}

class maint():
    def __init__(self,url,num):
        self.url = url
        self.num = num

    def fff(self):
        url = self.url

        try:
            a = requests.get(url, headers=headers, timeout=10)
            b = a.content

            if "shifen" in str(b):
                with open("924.txt","a+") as file:
                    file.writelines(url.strip()+'\n')

        except:
            pass

class myThread (threading.Thread):
    def __init__(self, q, num):
        threading.Thread.__init__(self)
        self.q = q
        self.num = num
        print(num)

    def run(self):
        while event.is_set():
            if self.q.empty():
                break
            else:
                sql_spot = maint(self.q.get(),self.num)
                sql_spot.fff()

def scan_thread(q):
    thread_num = 50
    threads = []
    for num in range(1,thread_num+1):
        t = myThread(q,num)
        threads.append(t)
        t.start()
    for t in threads:
        print(t)
        t.join()

def open_urls():                                                                             #
    url_path = r'phpstudy20190923194911.txt'
    f = open(url_path, 'r',encoding='utf-8')
    for each_line in f:
        q.put(each_line)
    return q

if __name__ == '__main__':
    open_urls()
    scan_thread(q)