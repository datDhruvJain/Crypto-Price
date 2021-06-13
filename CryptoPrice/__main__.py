import argparse
from . import GetData
from art import tprint

#GetData.get_price("ETH", "USD")
parser = argparse.ArgumentParser(
    prog="crypto-price",
    description= "crypto-price - A simple crypto price tool."
)
parser.add_argument("Crypto", choices=GetData.crypto_currencies, metavar="Crypto", type=str.upper)
parser.add_argument("Fiat", default="USD", choices=GetData.fiat, metavar="Fiat", type=str.upper)

# will maybe work on later
# parser.add_argument("-l", "--list", required=False, action="store_true")

parsed_args = parser.parse_args()

def main():
    #GetData.get_price(parsed_args.Crpyto, parsed_args.Fiat_Currency)
    print()
    tprint(parsed_args.Crypto, font="rand")
    print(GetData.get_price(parsed_args.Crypto, parsed_args.Fiat))
    print()

if __name__=="__main__":
    main()