import pandas as pd
import requests
import json
import time

# ~

pd.options.mode.chained_assignment = None

f = open('../books_05042022.json')
books = json.load(f)

# response = requests.post(
#     "http://localhost:8050/api/book")
# if (response.status_code != 200):
#     print(response.status_code)
#     print("Connection error")
#     raise Exception("Connection Error")

# books = response.json()
for book in books:
    response = requests.post(
        "http://localhost:8050/api/book", book)
    # print(response)
    if (response.status_code != 200):
        print(response.status_code)
        print("Connection error")
        raise Exception("Connection Error")
    print(book["title"])
    time.sleep(2)
