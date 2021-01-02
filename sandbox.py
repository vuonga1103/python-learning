import requests
import bs4

result = requests.get('http://www.example.com')

print(type(result))  # <class 'requests.models.Response'>
print(result.text)  # returns html document (page source) as string

# pass into .BeautifulSoup() text and string code for what engine to use to parse through the string text
soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup)  # raw string converted to soup OBJECT like the below

# <!DOCTYPE html>
# <html>
# <head>
# ...

# selecting for tag, returns a list
print(soup.select('title'))
# => [<title>Example Domain</title>]

# getting just the text
print(soup.select('title')[0].getText())
# => Example Domain
