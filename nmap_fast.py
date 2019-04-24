import threading
from IPy import IP 
import queue
import nmap

ip_list=[]
ips='''
172.29.90.207
172.29.90.207
172.29.90.207
172.29.90.207
172.29.90.207
172.29.90.207
'''

def make_list(ips):
    ip_list=ips.splitlines()
    del ip_list[0]
    #print(ip_list)
    return ip_list

def makeip(ip_list):
    for ip in ip_list:
        print(ip)
        if "/" in ip:
            #print("yes")
            ipx=IP(ip)
            for x in ipx:
                all_ip.put(str(x))

        if "-" in ip:
            #print("no")
            list_ip=[]
            list_ip=ip.split(".")
            print(list_ip)
            where=1
            for i in list_ip:
                if "-" not in i:
                    where=where+1
                else:
                    break
            print(where)
            a,b=list_ip[where-1].split("-")
            print(a,b)
            
            ip_result=[[],[],[],[]]
            flag=0
            for con in list_ip:
                if "-" in con:
                    for i in range(int(a),int(b)+1):
                        ip_result[flag].append(int(i))
                else:
                    ip_result[flag].append(int(con))
                flag=flag+1
            print(ip_result)
            for a in ip_result[0]:
                for b in ip_result[1]:
                    for c in ip_result[2]:
                        for d in ip_result[3]:
                            all_ip.put(str(a)+"."+str(b)+"."+str(c)+"."+str(d))

        else:
            all_ip.put(ip)
'''
    while True:
        print(all_ip.get())
'''
class myThread(threading.Thread):
    def __init__(self,all_ip):
        threading.Thread.__init__(self)
        self.list_queue=all_ip

    def run(self):
        while True:
            try:
               ip=self.list_queue.get(block=False)
               print("[+]"+ip)
               result=nm.scan(ip,'1-65535',arguments='-Pn')
               print(result)
            except:
                break

def run():
    ip_list=make_list(ips)
    print(ip_list)
    makeip(ip_list)
    thread_list=[]
    for a in range(0,20):
        thread=myThread(all_ip)
        thread_list.append(thread)
        thread.start()
    for thread in thread_list:
        thread.join()


if __name__=="__main__":
    nm=nmap.PortScanner()
    all_ip=queue.Queue()
    run()