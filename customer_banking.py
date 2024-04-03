# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
#Import dependencies
import sys
#Import savings functionality
from savings_account import create_savings_account
#Import CD funtionality
from cd_account import create_cd_account
#Inport account information
from Account import Account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_deposit = int(input('\nInput your opening savings deposit. '))
    savings_interest = float(input('Input your desired savings interest rate as a whole number. '))
    savings_months = int(input('How many months do you want to earn interest on your savings accountr? '))
    # Call the create_savings_account function and pass the variables from the user.
    end_bal, interest_earned = create_savings_account(savings_deposit, savings_interest, savings_months)
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    
    print(f'\nThe interest earned for the ${savings_deposit: ,.2f} savings account is ${interest_earned: ,.2f}')
    print(f'At the end of the {savings_months} months period, the savings account balance will be ${end_bal: ,.2f}')
          # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = int(input('\nInput your opening CD deposit. '))
    cd_interest = float(input('Input your desired CD interest rate. '))
    cd_maturity = int(input('How many months do you want to earn interest on your CD?  '))
    # Call the create_cd_account function and pass the variables from the user.
    end_bal_cd, interest_earned_cd = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f'\nThe interest earned for the {cd_maturity} months CD will be ${interest_earned_cd: ,.2f}')
    print(f'At the end of the maturity period, the CD balalnce will increase by the ${interest_earned_cd: ,.2f} of interest to ${end_bal_cd: ,.2f}\n')

if __name__ == "__main__":
    # Call the main function.
    main()