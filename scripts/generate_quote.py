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

def write_to_readme(static_readme , quote):
    lines  = open(static_readme , 'r').readlines()
    lines +='\nquote of the day :\n'
    lines += quote+'\n'
    open('./README.md' , 'w').writelines(lines)

def main():
    url_eng = "https://programming-quotes-api.herokuapp.com/quotes/random/lang/en/"
    quote_response = getResponse(url_eng)
    context = quote_response['en']
    author = quote_response['author']
    quote = context + " -" + author
    # print(quote)
    static_readme = './static_readme.md'
    write_to_readme(static_readme , quote)

if __name__ == '__main__':
    main()
