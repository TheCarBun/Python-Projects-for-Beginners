import requests

API_KEY = "fca_live_hg8Q257RSTX6SP3ZoSAkZVRQsQKpnPUTGaPCYNiw"
BASE_URL = f"https://api.freecurrencyapi.com/v1/"

def currency_list():
    url = f"{BASE_URL}currencies?apikey={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        return data['data']
    except:
        print("Something went wrong while fetching currencies")
        return None

def convert_currency(base, currency, amount):

    url = f"{BASE_URL}latest?apikey={API_KEY}&base_currency={base}&currencies={currency}"
    try:
        response = requests.get(url)
        data = response.json()
        amount = float(amount)
        exchange_amt =  float(data["data"][f"{currency}"])
        conv_amount = amount * exchange_amt
        return conv_amount
    except:
        print("Invalid inputs. Try again.")
        return None

while True:    
    base = input("Enter the base currency (Q for quit) (L for currency list) : ").upper()

    if base == "Q":
        break

    elif base == "L":
        list = currency_list()
        for item, value in list.items():
            print(f'{item} : {value["name_plural"]}')
        continue

    currency = input("Enter the currency to be exchanged to : ").upper()

    amount = input("Enter amount : ")

    data = convert_currency(base, currency, amount)
    if not data:
        continue
    print("Exchanged Amount = ", data)