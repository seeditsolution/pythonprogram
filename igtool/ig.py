import requests
from bs4 import BeautifulSoup
import webbrowser as wb

username = input("Enter a username ")
try:
    result = requests.get("https://www.instagram.com/" + username)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    imglink = soup.find_all('meta', property='og:image')
    desc = soup.find_all('meta', property='og:description')

    imglink = (str(imglink[0])[15:])
    imglink = imglink[:len(imglink) - 23]
    imglink = imglink.replace("&lt;", "<")
    imglink = imglink.replace("&gt;", ">")
    imglink = imglink.replace("&amp;", "&")

    desc = (str(desc[0])[15:])
    desc = desc.replace('" property="og:description"/>', '')
    desc = desc.replace('- See Instagram photos and videos from ', '\n')
    print(desc)

    ip = input("Do you want to view profile picture? y/n ")
    if ip == "y" or ip == "Y":
        wb.open_new_tab(imglink)
    elif ip == "n" or ip == "N":
        wb.open_new_tab("rb.gy/7dt4n7")
except:
     print("Invalid username!")
