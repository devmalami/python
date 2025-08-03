# Currency Converter | Dollar to Naira

print('Select what to convert (type A or B)\n(A)Naira to Dollar\n(B)Dollar to Naira')
currency = (input().upper())
amount = float(input('Enter amount you want to convert: '))

# Convert Naira to Dollar
if currency == 'A':
    converted_amount = amount / 1600
    print(f'N{amount} = ${converted_amount}')  # Dollar to Naira
elif currency == 'B':
    converted_amount = amount * 1600
    print(f'${amount} = N{converted_amount}')  # Naira to Dollar
else:
    print('Please select A or B')
