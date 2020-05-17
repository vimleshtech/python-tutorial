import requests
from bs4 import BeautifulSoup
import pandas as pd

#0: Category: Hotels and travel,1: Category: Restaurants
categories = ['hotels_travel_list.html','restaurants_list.html']


url ='http://mlg.ucd.ie/modules/yalp/'

#positive rating
pos = ['4-star','5-star']
#negative rating
neg = ['1-star','2-star','3-star']

for cat in categories:
     print('Getting data for category ',cat.replace('.html',''),'. please wait...')
     page = requests.get(url+cat)

     #print(page.text)
     soup = BeautifulSoup(page.text,"html.parser" ) # lxml is just the parser for reading the html
     all_a = soup.find_all('a')
     l = len(all_a)

          
     cat_list = []
     sub_text_list = []
     sub_href_list = []
     rating_list = []
     rating_num_list = []
     rating_text_list = []
     rating_href_list = []
     
     for a in all_a: 
          #print(a.text)
          #print(a.get('href'))
          #print(url+a.get('href'))
          
          review_page = requests.get(url+a.get('href'))
          review_list = BeautifulSoup(review_page.text,"html.parser" )
          all_img = review_list.find_all('img')
          all_text = review_list.find_all("p", {"class": "text"})
          ind =0          
          #print(review_page)
          #print(review_list )
          all_img.remove(all_img[0]) #remove first element which is not rating
          for img in all_img:
               #print(img)
               #print(img.get('alt'))
               cat_list.append(cat)
               sub_text_list.append(a.text)
               sub_href_list.append(url+a.get('href'))
               rating_href_list.append(img.get('src'))
               #print(all_text[ind].text)
               rating_text_list.append(all_text[ind].text)
               ind +=1
               #break
               
               if img.get('alt') in pos:
                    #print('positive')
                    rating_list.append('positive')
                    rating_num_list.append(1)
               elif img.get('alt') in neg:
                    #print('negative')
                    rating_list.append('negative')
                    rating_num_list.append(0)
               else:
                    rating_list.append('none')
                    rating_num_list.append('none')
                    
          
          
     #print('--------',cat,'------------count :',l)
     df = pd.DataFrame(data={'Category_Name':cat_list ,'Category_Item':sub_text_list,'Category_Item_Href':sub_href_list,'Rating':rating_list,'Rating_Score':rating_num_list,'Rating_Text':rating_text_list,'Rating_Img':rating_href_list})
     
     #print(df)
     df.to_csv(cat.replace('.html','.csv'), index=False)
     print(cat.replace('.html','.csv'),' dataset is saved ')
     
     
