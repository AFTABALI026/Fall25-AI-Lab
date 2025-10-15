def luhn_check(card_number):
    digits = [int(d) for d in str(card_number)]
    for i in range(len(digits) - 2, -1, -2):
        doubled = digits[i] * 2
        if doubled > 9:
            doubled -= 9
        digits[i] = doubled
    total = sum(digits)
    return total % 10 == 0


card_number = input("Enter a card number to check: ")

if luhn_check(card_number):
    print("The number is VALID according to the Luhn Algorithm.")
else:
    print("The number is NOT valid according to the Luhn Algorithm.")
