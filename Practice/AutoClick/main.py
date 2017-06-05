import webbrowser as web
import re
import urllib
import time
import os

def spider(url,urlpattern):
    urls = getURLs(url,urlpattern)
    for url in urls:
        visitURL(url)
        
def visitURL(url):
    url=url[:-1] #remove the " at the end of the string
    print(url)
    #print("\n")    
    web.open(url,1,False)
    time.sleep(5)
    
def getURLs(url,urlpattern):
    urls=[]

    response=urllib.urlopen(url)
    html=response.read()
    pattern=re.compile(urlpattern)
    urls=pattern.findall(html)
    urls=list(set(urls))
    return urls

'''
if __name__=="__main__":
    urls={
        "http://www.jianshu.com/p/baeae8cdfb94"
        }
        
    for i in range(1,10):
        for url,urlpattern in urls.items():
            spider(url,urlpattern)
        print("Blogs has been refreshed for ", i, " times")
        os.system("taskkill /F /IM chrome.exe")
'''

if __name__=="__main__":
    url="http://www.jianshu.com/p/baeae8cdfb94"
    
    for i in range(0, 10):
        print(i)
        #co = urllib.urlopen(url).read()
        
        web.open(url, 1, False)
        time.sleep(1)