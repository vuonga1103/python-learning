import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res.text, 'lxml')

print(soup.select('.thumbimage'))
# prints all images with class thumbimage

computer = soup.select('.thumbimage')[0]
print(computer)
# <img alt="" class="thumbimage" data-file-height="600" data-file-width="800" decoding="async" height="165" src="//upload....

# making request for the image
image_link = requests.get('https:' + computer['src'])
image_link.content  # binary file for image that can be saved to computer

# pass into open() file name you want to call the image, mode: wb (write binary)
f = open('my_computer_image.jpg', 'wb')
# write to the file
f.write(image_link.content)
f.close()

# the above saves the image to current working directory. but to save it somewhere else you can specify the full path, ex. C://Users...
