#step 0 - Set the Environment
#install requests,bs4,html5lib
import requests
from bs4 import BeautifulSoup

#####  Step 1 - Bring the HTML Content #####
def scraping_func(url):
    r=requests.get(url)
    htmlContent=r.content
    #print(htmlContent)
    #print("******************************")
    #print("******************************")
    #print("******************************")
    #print(type(htmlContent))
    #print("******************************")
    #print("******************************")
    #print("******************************")  
    
    ###### Step 2 -Pasring/fetching the HTML #######
    
    soup=BeautifulSoup(htmlContent,'html.parser')
    #print(soup)

    ######### Step 3 - HTML Tree traversal #########
    
    title=soup.title 
    paras=soup.find_all('p')  #returns all the paras
    anchors=soup.find_all('a')  #returns all the anchors
    para=soup.find('p')
    para_class=soup.find('p')['class'][0]
    text=soup.find('p').get_text()
    return soup.title.string
       