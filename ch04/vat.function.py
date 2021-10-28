# vat.function.py
def calculate_price_with_vat(price, vat):
    return price * (100 + vat) / 100


if __name__ == "__main__":
    print(calculate_price_with_vat(100, 20))
