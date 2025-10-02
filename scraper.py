# Product Scraper Program
# Author: Mohamed Sallam

import requests
from bs4 import BeautifulSoup
import pandas as pd

# List of URLs to scrape
url_list = [
    "https://webscraper.io/test-sites/e-commerce/allinone",
    "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops",
    "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets",
    "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"
]

# Dictionary to store scraped data
dic = {
    "product_name": [],
    "product_price": [],
    "product_description": [],
    "product_rating": [],
    "number_of_reviews": []
}

# Loop through each page and scrape
for url in url_list:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("div", class_="thumbnail")

    for result in results:
        product_name = result.find("a", class_="title")
        product_price = result.find("h4", class_="price")
        product_description = result.find("p", class_="description")
        product_rating = result.find("p", {"data-rating": True})
        review_count = result.find("p", class_="review-count")

        dic["product_name"].append(product_name.text.strip())
        dic["product_price"].append(product_price.text.strip())
        dic["product_description"].append(product_description.text.strip())
        dic["product_rating"].append(product_rating.get("data-rating") if product_rating else None)
        dic["number_of_reviews"].append(review_count.text.strip() if review_count else None)

# Convert to DataFrame
df = pd.DataFrame(dic)

# Print DataFrame
print(df)

# Save to CSV
df.to_csv("products.csv", index=False)
print("✅ Data saved to products.csv")
