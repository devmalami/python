# User's stored PIN
user_pin = 4321
attempts = 0

# Ask user for PIN
entered_pin = int(input('Enter PIN: '))

# Check if entered PIN is correct
while attempts < 3:
    if entered_pin == user_pin:
        # Access granted if PIN is correct
        print('PIN correct! Access granted.')
        break
    else:
        attempts += 1
        # Display error message if PIN is incorrect
        print('Wrong PIN. Try again.')
else:
    # Account locked if PIN is incorrect 3 times
    print('Too many failed attempts. Your account is locked')
