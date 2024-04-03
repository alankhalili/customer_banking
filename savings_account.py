"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    
    savings_account = Account(balance, 0)
    
  
    # Calculate interest earned
    """the sav_deposit is an input on the customer banking script"""
     # ADD YOUR CODE HERE
    
    interest_earned = balance * (interest_rate/100) * months/12


    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE

    end_bal = balance + interest_earned
    
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings_account.set_balance(end_bal)
    
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings_account.set_interest(interest_earned)
    
    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE
    return end_bal, interest_earned

