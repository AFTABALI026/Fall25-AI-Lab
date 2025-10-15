# Luhn Algorithm in Python
# This program verifies whether a given number is valid using Luhn's rule.

def verify_luhn(number):
    # Step 1: Convert the number into individual digits
    num_list = [int(n) for n in str(number)]
    
    # Step 2: Double every second digit from the right (ignoring the last one)
    for index in range(len(num_list) - 2, -1, -2):
        temp = num_list[index] * 2
        # Step 3: Subtract 9 if the result is greater than 9
        if temp > 9:
            temp -= 9
        num_list[index] = temp
    
    # Step 4: Calculate the sum of all digits
    total_sum = sum(num_list)
    
    # Step 5: Check divisibility by 10
    return total_sum % 10 == 0


# ---------- MAIN PROGRAM ----------
card_input = input("Enter a card number to check: ")

if verify_luhn(card_input):
    print("The number is VALID according to the Luhn Algorithm.")
else:
    print("The number is NOT valid according to the Luhn Algorithm.")
