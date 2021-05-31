from flask import Flask
from bs4 import BeautifulSoup
import requests
from flask import request
import re

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
    
    if tagname == "email":
        emails = soup.get_text()
        emails = emails.split("\n")
        emails1 = []
        emails2 = []
        finalemails = []
        for i in emails:
            if i != '':
                emails1.append(i)

        for i in emails1:
            i = i.replace(" ", "")
            k.append(i)

        for i in k:
            # print(i)
            if i != "" or i != "\n":
                emails2.append(i.strip("\r"))
        for i in emails2:
            if re.match('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', i):
                finalemails.append(i)

        for i in finalemails:
            s = s + i + "\n"
        if s != "":
            return s
        else :
            return tagname + " : Data not found"
    if tagname != "a" or tagname != "email":
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
