import requests
import bs4

# base_url = "http://books.toscrape.com/catalogue/page-{}.html"

# res = requests.get(base_url.format(1))
# soup = bs4.BeautifulSoup(res.text, 'lxml')

# products = soup.select('.product_pod')

# example = products[0]

# # print('star-rating Two' in str(example))
# # => False, quick and dirty way to check if rating is 3 star

# # better way...
# print(example.select('.star-rating.Two'))
# # will return a list that has selection or an empty list
# # [] == example.select('.star-rating.Two')

# print(example.select('a')[1]['title']) # A Light in the Attic

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

book_titles = []

for page_num in range(0, 51):
    res = requests.get(base_url.format(page_num))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    products = soup.select('.product_pod')

    for product in products:
        has_two_star_rating = ([] == product.select('.star-rating.Two'))

        if has_two_star_rating:
            title = product.select('a')[1]['title']
            book_titles.append(title)

print(book_titles)
