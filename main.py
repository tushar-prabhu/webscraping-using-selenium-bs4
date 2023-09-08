from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Edge() #"C:/Users/tusha/Downloads/chromedriver_win32(1)/chromedriver.exe"

products = []
prices = []
ratings = []
driver.get('https://www.flipkart.com/6bo/b5g/~cs-hbtuge4qub/pr?sid=6bo%2Cb5g&collection-tab-name=Gaming&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkdhbWluZyBMYXB0b3BzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&wid=26.productCard.PMU_V2_5')
#driver.get('https://www.flipkart.com/laptops/~cs-g5q3mw47a4/pr?sid=6bo%2Cb5g&collection-tab-name=Browsing&wid=15.productCard.PMU_V2_4')

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
for a in soup.findAll('a', href=True,attrs={'class':'_1fQZEK'}):
    name = a.find('div',attrs={'class':'_4rR01T'})
    price = a.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
    rating = a.find('div',attrs={'class':'_3LWZlK'})
    products.append(name.text)
    prices.append(price.text)
    if(rating):
        ratings.append(rating.text)
    else:
        ratings.append("N/A")
    df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
    df.to_csv('product1.csv', index=False, encoding='utf-8')