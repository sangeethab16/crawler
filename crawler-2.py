#!/usr/bin/env python
# coding: utf-8

# In[7]:


from bs4 import BeautifulSoup
import requests
import sys
import re

url = input("Enter the seed link")  # "https://en.wikipedia.org/wiki/Karen_Sparck_Jones"
word = input("Enter the keyphrase") #"retrieval"
l_count2 = 1 #No of Links count
def q2(url,word):
    crawled_links = [url.lower()]
    all_urls = [url.lower()]
    wiki = "https://en.wikipedia.org"
    ir2_text = open("ir2.txt", "w+")
    
    def CheckLink(link):
        if link.startswith("/wiki/"):
            if ":" not in link:
                if "Main_Page" not in link:
                    return True
        else:
            return False

    def getLinks(url_string):
        global l_count2
        req = None
        req = requests.get(url_string)
        data = req.text
        soup = BeautifulSoup(data)
        flag = 1
        for link in soup.find_all("a", attrs={'href': re.compile("^/wiki/")}, href=True):
            urllink = link['href']         
            if CheckLink(urllink):
                if "#" in urllink:
                    urllink = urllink[0:urllink.index("#")]
                if urllink not in crawled_links and l_count2 <= 1000:
                    if wiki + urllink not in all_urls:
                        if(soup.find_all("a", {'href' : re.fullmatch(word,word)}, href=True)):
                            print(l_count2," ", wiki + urllink)
                            l_count2 += 1
                            all_urls.append(wiki + urllink)
                            crawled_links.append(wiki + urllink)
                            flag += 1
                            ir2_text.write(wiki + urllink + '\n')
        all_urls.pop(0)
        return flag
    
    def focused_crawler():
        
        current_depth = 0
        counter = getLinks(all_urls[0])
        totalCount = counter
        current_depth += 1

        while current_depth <= 5 and l_count2 <= 1000:
            counter = 0
            while totalCount > 0 and l_count2 <=1000 and all_urls:
                counter += getLinks(all_urls[0])
                totalCount -= 1
            
                if totalCount == 0:
                    totalCount = counter
                    break    
            current_depth += 1

    focused_crawler()

q2(url,word)


# In[ ]:





# In[ ]:




