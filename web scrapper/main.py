
import requests
from bs4 import BeautifulSoup as bs

github_user=input('Input Github User: ')
url = 'https://github.com/'+github_user+'?tab=repositories'

# this is gonna collect all the html data of the user input 
r=requests.get(url)
# content will give the data of the page
# function to parse the html
soup = bs(r.content, 'html.parser') 
#describing what to find and what to include in []
profile_image=soup.find('img',{'alt': 'Avatar'})['src'] 
print(profile_image)



