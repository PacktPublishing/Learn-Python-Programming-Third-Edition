# vat.py
price = 100  # GBP, no VAT
final_price1 = price * 1.2
final_price2 = price + price / 5.0
final_price3 = price * (100 + 20) / 100.0
final_price4 = price + price * 0.2


if __name__ == "__main__":
    for var, value in sorted(vars().items()):
        if 'price' in var:
            print(var, value)
