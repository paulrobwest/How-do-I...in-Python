from bs4 import BeautifulSoup as bs
import requests

my_git_profile = "https://github.com/paulrobwest"
req = requests.get(my_git_profile)
scraper = bs(req.content, "html.parser")
pro_pic = scraper.find("img", {"alt": "Avatar"})["src"]
print(pro_pic)

