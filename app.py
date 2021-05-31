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
    if url.startswith("https://") or url.startswith("http://"):
        print("Keyword found")
        pass
    else:
        print("Adding keyword")
        url = "https://" + url
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
            
    if tagname != "a":
        y = soup.find_all(tagname)
        for i in y:
            # print(i.text)
            k.append(i.text)

        for i in list(set(k)):
            s = s + i + "\n"
        if s != "":
            return s
        else:
            return tagname + " : Data not found"
    else:
        y = y = soup.find_all(tagname, href=True)
        for i in y:
            # print(i.text)
            k.append(i['href'])

        for i in list(set(k)):
            s = s + i + "\n"
        if s != "":
            return s
        else:
            return tagname + " : Data not found"


# y = scrapeData("https://www.kleverme.com","p")
# print(y)
if __name__ == '_main_':
    app.run()
