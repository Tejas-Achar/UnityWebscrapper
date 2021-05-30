from flask import Flask
from bs4 import BeautifulSoup
import requests
from flask import request

app = Flask(__name__)

@app.route("/",methods = ["POST"])
def scrapeData():
    content = request.json
    url = content["url"]
    tagname = content["tagname"]
    k = []
    s = ""
    if "https://" or  "http://" not in url:
        url = "https://" + url
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    if tagname != "a":
        y = soup.find_all(tagname)
        for i in y:
            # print(i.text)
            k.append(i.text)

        for i in k:
            s = s + i + "\n"

        return s
    else:
        y = y = soup.find_all(tagname, href=True)
        for i in y:
            # print(i.text)
            k.append(i['href'])

        for i in k:
            s = s + i + "\n"
        return s


# y = scrapeData("https://www.kleverme.com","p")
# print(y)
if _name_ == '_main_':
    app.run()
