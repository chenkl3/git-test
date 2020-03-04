import requests
import threading
import re
import time
import os

all_urls=[]
all_img_urls=[]
pic_links =[]
g_lock = threading.Lock()

class Spider:
    def __init__(self,target_url,headers):
        self.target_url = target_url
        self.headers = headers

    #获取所有的想要抓取的URL
    def getUrls(self,start_page,page_num):
        for i in range(start_page,page_num+1):
            url = self.target_url %i
            all_urls.append(url)
class Producer(threading.Thread):
    def run(self):
        headers = {}
        global all_urls
        while len(all_urls)>0:
            g_lock.acquire()
            page_url = all_urls.pop()
            g_lock.release()
            try:
                response = requests.get(page_url,headers)
                all_pic_url = re.findall()
                global all_img_urls
                g_lock.acquire()
                all_img_urls += all_pic_url
                g_lock.release()
            except:
                pass
            time.sleep()
class Consumer(threading.Thread):
    def run(self):
        headers = {}
        global all_img_urls
        while len(all_img_urls) >0:
            g_lock.acquire()
            img_url = all_img_urls.pop()
            g_lock.release()
            try:
                response = requests.get(img_url,headers=headers,timeout=3)
                response.encoding = 'gb2312'
                title = re.search()
                all_pic_src = re.findall()
                pic_dict = {title:all_pic_src}
                global pic_links
                pic_links.append(pic_dict)
                g_lock.release()
            except:
                pass
            time.sleep()
class DownPic(threading.Thread):
    headers ={}
    while True:
        global pic_links
        g_lock.acquire()
        if len(pic_links)==0:
            g_lock.release()
            continue
        else:
            pic = pic_links.pop()
            g_lock.release()
            for key,values in pic.items():
                path = key.rstrip("\\")
                is_exists = os.path.exists(path)
                if  not is_exists:
                    os.makedirs(path)
                    print()
                else:
                    print("7779")
                for pic in values:
                    filename = path +"/"+pic.split('/')[-1]
                    if os.path.exists(filename):
                        continue
                    else:
                        try:
                            response = response.get(pic,headers=headers)
                            with open(filename,'wb') as f:
                                f.write(response.content)
                                f.close()
                        except Exception as e:
                            print(e)
                            pass
