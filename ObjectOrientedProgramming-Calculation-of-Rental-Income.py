# Here we assume that we have a client coming to us asking for an automated 
# Rental Property Calculator. Our client's name is Brandon from a company 
# called "Bigger Pockets".

# Using Object Oriented Programming create a program that will calculate the 
# Return on Investment(ROI) for a rental property.

# To calculate the ROI on a rental property:
#   1. INCOME:
#       - Rental Income
#       - Allow for any extra income
#   2. EXPENSES:
#       - Allow to list all expenses
#   3. CASHFLOW:
#       - cashflow = total_income - total_expenses
#   4. ROI:
#       - INITIAL COSTS: (total_investment)
#           - Down Payment
#           - Closing Costs
#           - Reno Budget
#           - Allow to list any misc initial costs
#       - annual_cashflow = cashflow * 12
#       - roi_percentage = (annual_cashflow / total_investment) * 100

class ROICalculator():
    def __init__(self, income = 0, expenses = 0, initial_investment = 0):
        self.rental_income = income
        self.expenses = expenses
        self.initial_investment = initial_investment
        self.cashflow = self.rental_income - self.expenses

    def calculateROI(self):
        annual_cashflow = self.cashflow * 12
        roi_percentage = (annual_cashflow / self.initial_investment) * 100
        print(f'Your return of investment is {roi_percentage}%')

def run():
    rental_income = 0
    expenses = 0
    initial_investment = 0
    print("Hello! Let's get started calculating the return of investment on your rental property.")
    entering_information = True
    while entering_information:
        response = input('We need a little information to run the calculation. What would you like to enter? income/expenses/investment/quit : ')
        if response.lower() == 'quit':
            print('Goodbye. Please come back soon.')
            break
        if response.lower() == 'income':
            if rental_income == 0:
                rental_income = input('What is the total rental income of this property, before expenses? ')
            else:
                response = input(f'You previously entered {rental_income} as the rental income. Is this correct? Y/N : ')
                if response.lower() == 'n':
                    rental_income = 0
                    
        if response.lower() == 'expenses':
            if expenses == 0:
                expenses = input('What is the total expenses of this property? ')
            else:
                response = input(f'You previously entered {expenses} as the expenses. Is this correct? Y/N : ')
                if response.lower() == 'n':
                    expenses = 0
        if response.lower() == 'investment':
            if initial_investment == 0:
                initial_investment = input('What is the initial investment of the property, including any renovations, down payment, closing costs, and misc fees? ')
            else:
                response = input(f'You previously entered {initial_investment} as the initial investment. Is this correct? Y/N : ')
                if response.lower() == 'n':
                    initial_investment = 0
        if int(rental_income) > 0 and int(expenses) > 0 and int(initial_investment) > 0:
            entering_information = False
    ROI = ROICalculator(int(rental_income), int(expenses), int(initial_investment))
    ROI.calculateROI()
    print('Thank you for using our services!')

run()