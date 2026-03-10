def convert_to_valid_price(text: str):
    try:
        text = text.replace(',', '.')
        return round(float(text), 2)

    except Exception as e:
        return None


if __name__ == '__main__':
    a = '2,123213'
    b = '32.479213'

    print(convert_to_valid_price(a), convert_to_valid_price(b))