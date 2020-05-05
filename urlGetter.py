from bs4 import BeautifulSoup
import requests



def urlGet(urls):
  for url in urls:

    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'})

    print("########## Status Codes ##########")
    print(page.status_code) # 200 is good

    result = page.content # get all html from page

    soup = BeautifulSoup(result, "html.parser") # create BeautifulSoup object using html.parser builtin module

    img = soup.find("img", {"class": "no-click screenshot-image"}) # get the img tag w the class "no-click screenshot-image"

    noSCimg = img.attrs['src'] # get the src from that img

    noSCimgURL = noSCimg[2:] # remove front 2 slashes from url

    #print(noSCimgURL)

    imgUrlList = []
    imgUrlList.append(noSCimgURL)
  

  print()
  print("##### GETTER #####")
  print(imgUrlList)
  print(url)
  print("################################################")
  print()


  return imgUrlList


  
  

  