"""
Author by : p4mbud1
17 Juli 2021
"""
import requests


def Shopee_connection():
    url     = "https://shopee.co.id/"
    session = requests.session()
    request = session.get(url)
    with open ("cek.html", "w") as e:
        e.write(request.text)
if __name__ == ("__main__"):
    intro   = "Script To Buy Shopee FlashSale"
    Shopee_connection()
