import urllib.request
import json

def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
    return jsonData

def main():
    url_eng = "https://programming-quotes-api.herokuapp.com/quotes/random/lang/en/"
    quote = getResponse(url_eng)
    print(quote['en']+" -"+quote['author'])

if __name__ == '__main__':
    main()
