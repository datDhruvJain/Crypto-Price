'''
Overview:
    1. Get the list of all fiat currencies (govt backed and recognized currencies)
        and save it to a list
    2. Do the same for the crypto by substracting the list of fiats from ALL currencies
    3. Get data on the price of each crypto with respect to the fiat
    4. Colorise and print!
'''
from sys import exit
import requests
from colorama import init as color_init, Fore
color_init()

def handle_net_error():
    # Small utility to handle network related errors
    print(Fore.RED + "Error connecting to the API!" + Fore.RESET)
    exit(1)

# First get the non cypto-currencies from the website
try:
    fiat = requests.get("https://api.coinbase.com/v2/currencies").json()

except:
    handle_net_error()

# Use list comprehension to generate a list of all the non-cryptos
fiat = [i["id"] for i in fiat["data"]]
# fiat -> list

try:
    # Here we get the list of all Currencies
    exchange_rates = requests.get(
        "https://api.coinbase.com/v2/exchange-rates").json()

except:
    handle_net_error()

# Then we need to make a list for the same
crypto_currencies = list(exchange_rates["data"]["rates"].keys())

# Finally we compare the the two above lists to get the crypto currencies
crypto_currencies = [val for val in crypto_currencies if val not in fiat]
# crypt-=0_currencies -> list

#r = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/buy")




def get_price(crypto, base):
    ''' Get the current price of the [crypto-currencies] \
        in terms of the physical currency specified '''

    # some string handling required for the GET command at the API side
    curr_conv_code = crypto + "-" + base
    
    try:
        get_url = "https://api.coinbase.com/v2/prices/" + curr_conv_code + "/buy"
        r = requests.get(get_url).json()
    except:
        print(Fore.RED + "Error connecting to the API!" + Fore.RESET)
        return
    
    output_str = ("1 {red}{base}{rst} costs {blue}{amount}{rst} {green}{currency}{rst}"
        .format(rst=Fore.RESET, red=Fore.LIGHTRED_EX, blue=Fore.LIGHTCYAN_EX, green=Fore.LIGHTGREEN_EX,
                base=r["data"]["base"], amount=r["data"]["amount"], currency=r["data"]["currency"]))

    return output_str

def check_currency(crypto :list, base: list) -> bool:
    """ Simple check to see if the given crypto and fiat in correct and in the given list of currencies
        Created in case this file is used by another file which is no src.__main__
    """
    
    if crypto not in crypto_currencies:
        return False
    
    if base not in fiat:
        return False

if __name__ == "__main__":
    print(get_price("ETH", "USD"))