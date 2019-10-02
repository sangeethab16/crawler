#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sys
l_count = 1 #No of Links count
url = input("Enter seed link")

def q1(url):
    from bs4 import BeautifulSoup 
    import re
    import sys
    import urllib
    import requests
    import os
    import time
    
    l_count = 1 #count of 
    crawled_links = [url] #save the visited links into this list
    all_urls = [url]  #save all the links in the page into this list
    wiki = "https://en.wikipedia.org"
    ir1_text = open("ir1.txt","w+")

 
    
    # Checklink checks for ':' , "#" and returns false or true accordingly
    def CheckLink(urllink):
            if urllink.startswith("/wiki/"):
                if "#" and ":" in urllink:
                    return False
                if "#" in urllink:
                    return False
                if ":" not in urllink:
                    return True
    #This performs the functionality of a crawler
    def crawler1():
        time.sleep(1)
        current_depth = 0
        counter = getLinks(url)
        totalCount = counter
        current_depth += 1
        while current_depth <= 5 and l_count <= 1000:
            counter = 0
            while totalCount > 0 and l_count <= 1000 and all_urls:
                counter += getLinks(all_urls[0])
                totalCount -= 1

                if totalCount == 0:
                    totalCount = counter
                    break
            current_depth += 1
            
    def getLinks(string):
        global l_count
        r = None
        r = requests.get(string)
        data = r.text
        soup = BeautifulSoup(data)
        flag = 1
        for link in soup.find_all("a", attrs={'href': re.compile("^/wiki/")}, href=True):
            link_url = link['href']
            if CheckLink(link_url):
                if link_url not in crawled_links and l_count <= 1000:
                    if "#" in link_url:
                        all_urls.append(link_url[0:link_url.index("#")])
                        crawled_links.append(link_url[0:link_url.index("#")])
                        ir1_text.write(wiki + link_url[0:link_url.index("#")] + '\n')
                    else:
                        all_urls.append(wiki+link_url)
                        ir1_text.write(wiki + link_url + '\n')
                    l_count += 1
                    crawled_links.append(link_url)
                    print(l_count ," ",wiki + link_url)
        all_urls.pop(0)
        return flag
    
    crawler1()
    
q1(url) #Execution starts here


# In[ ]:




