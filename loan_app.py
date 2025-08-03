# A credit score script for a Loan App

user_income = int(input("What is your monthly income? N "))
paid_loan_time = input("Was your last loan overdue before payment? 'Yes/No': ")

high_income = user_income >= 50000
good_credit = paid_loan_time.strip().lower() == 'no'

message = "You are eligible!" if high_income and good_credit else "Sorry. You can't get a loan!"
print(message)
