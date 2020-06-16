import bs4 , requests ,pyperclip ,webbrowser ,sys

if len(sys.argv) >1 :
    query = '+'.join(sys.argv[1:])
else:
    query = pyperclip.paste()

query = query.replace(' ', '+')
URL = f"https://google.com/search?q={query}"


# desktop user-agent

headers = {"user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"}

#get html
res = requests.get(URL, headers=headers)
res.raise_for_status()

# beautifulsoup
soup = bs4.BeautifulSoup(res.text,'html.parser')
elem = soup.select('div[class="r"]')

for sub_elem in elem:
    print(sub_elem.find('a')['href'])
    webbrowser.open(sub_elem.find('a')['href'])
