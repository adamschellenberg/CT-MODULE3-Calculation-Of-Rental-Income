# CODING TEMPLE - MODULE 3 - ADVANCED PYTHON - CALCULATION OF RENTAL INCOME

import math
import time

class ROICalculator():

    def __init__(self):
        self.rental_income_dict = {}
        self.expenses_dict = {}
        self.cashflow = 0
        self.initial_investment_dict = {}

    def getIncome(self):
        entering_information = True
        while entering_information:
            response = input('What is the monthly rental income, from rent only? ')
            self.rental_income_dict['rental'] = int(response)
            response = input('Is there any other income to enter, such as laundry, storage, etc? Y/N ')
            if response.lower() == 'y':
                entering_other_info = True
                while entering_other_info:
                    response_other_name = input('Great. What would you like to call this income? Please give all incomes unique names ')
                    response_other_amount = input('What is the amount? ')
                    self.rental_income_dict[response_other_name] = int(response_other_amount)
                    response = input('Added. Do you have more to enter? Y/N ')
                    if response.lower() == 'n':
                        entering_other_info = False
                        entering_information = False
            else:
                entering_information = False

    def getExpenses(self):
        entering_information = True
        while entering_information:
            taxes = input('What is the amount monthly spent on taxes? ')
            self.expenses_dict["taxes"] = int(taxes)
            insurance = input('What is the amount monthly spent on insurance? ')
            self.expenses_dict['insurance'] = int(insurance)
            utilities = input('What is the amount monthly spent on utilities? ')
            self.expenses_dict['utilities'] = int(utilities)
            mortgage = input('What is the amount monthly spent on mortgage? ')
            self.expenses_dict['mortgage'] = int(mortgage)
            response = input('Is there any other expenses to enter, such as HOA, property management, etc? Y/N ')
            if response.lower() == 'y':
                entering_other_info = True
                while entering_other_info:
                    response_other_name = input('Great. What would you like to call this expense? Please give all expenses unique names ')
                    response_other_amount = input('What is the amount? ')
                    self.expenses_dict[response_other_name] = int(response_other_amount)
                    response = input('Added. Do you have more to enter? Y/N ')
                    if response.lower() == 'n':
                        entering_information = False
                        entering_other_info = False
            else:
                entering_information = False

    def getInvestment(self):
        entering_information = True
        while entering_information:
            down_payment = input('What was the amount spent on the down payment? ')
            self.initial_investment_dict["down payment"] = int(down_payment)
            closing_costs = input('What was the amount spent on the closing costs? ')
            self.initial_investment_dict["closing costs"] = int(closing_costs)
            repairs = input('What was the amount spent on repairs? ')
            self.initial_investment_dict["repairs"] = int(repairs)
            response = input('Is there any other initial investment costs to enter, such as furnishing, etc? Y/N ')
            if response.lower() == 'y':
                entering_other_info = True
                while entering_other_info:
                    response_other_name = input('Great. What would you like to call this cost? Please give all costs unique names ')
                    response_other_amount = input('What is the amount? ')
                    self.initial_investment_dict[response_other_name] = int(response_other_amount)
                    response = input('Added. Do you have more to enter? Y/N ')
                    if response.lower() == 'n':
                        entering_information = False
                        entering_other_info = False
            else:
                entering_information = False

    def calculateCashflow(self):
        income = 0
        expenses = 0
        for x in self.rental_income_dict.values():
            income += x
        for x in self.expenses_dict.values():
            expenses += x
        self.cashflow = income - expenses
        
    
    def calculateROI(self):
        self.calculateCashflow()
        annual_cashflow = self.cashflow * 12
        investment = 0
        for x in self.initial_investment_dict.values():
            investment += x
        roi = math.floor((annual_cashflow / investment) * 100)
        self.printResults(roi)
    
    def printResults(self, roi):
        print('Your income(s) entered were: ')
        for x,y in self.rental_income_dict.items():
            print(x,y)
        print('Your expense(s) entered were: ')
        for x,y in self.expenses_dict.items():
            print(x,y)
        print('Your investment(s) entered were: ')
        for x,y in self.initial_investment_dict.items():
            print(x,y)
        print(f'Based on these, your ROI is: {roi}%')

ROI = ROICalculator()

def run():
    print("Welcome to the Buy n Large ROI Calculator!")
    print("Let's get started with calculating the ROI (Return of Investment) of your property.")
    print("We're going to need some information from you before we are able to accurately calculate your sweet gainz.")
    print("First, we'll start with some questions regarding income. Then, we'll move on to expenses, and complete the c-c-c-combo with investment info.")
    print("Let's a-go!")

    running = True
    while running:
        time.sleep(1)
        print('\nRound One: Income')
        print('====================')
        ROI.getIncome()
        time.sleep(1)
        print('\nRound Two: Expenses')
        print('====================')
        ROI.getExpenses()
        time.sleep(1)
        print('\nFinal Round: Investment')
        print('====================')
        ROI.getInvestment()
        time.sleep(1)
        print('\nFINISH HIs/her ROI calculation!')
        print('====================')
        ROI.calculateROI()
        time.sleep(1)
        print('\nNow go out there and make more investments! Get that cheddar!')
        break

run()
