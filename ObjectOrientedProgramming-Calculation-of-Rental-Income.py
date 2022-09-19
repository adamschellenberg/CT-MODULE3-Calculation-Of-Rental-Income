# CODING TEMPLE - MODULE 3 - ADVANCED PYTHON - CALCULATION OF RENTAL INCOME

class ROICalculator():
    def __init__(self):
        self.rental_income = 0
        self.expenses = 0
        self.initial_investment = 0
        self.cashflow = 0

    def getIncome(self):
        entering_income = True
        while entering_income:
            if self.rental_income == 0:
                    response = input('What is the total monthly rental income of this property, before expenses? ')
                    self.rental_income = int(response)
                    entering_income = False
            else:
                response = input(f'You previously entered {self.rental_income} as the monthly rental income. Is this correct? Y/N : ')
                if response.lower() == 'n':
                    self.rental_income = 0
                elif response.lower() == 'y':
                    entering_income = False
    
    def getExpenses(self):
        entering_expenses = True
        while entering_expenses:
            if self.expenses == 0:
                response = input('What is the total monthly expenses of this property? ')
                self.expenses = int(response)
                entering_expenses = False
            else:
                response = input(f'You previously entered {self.expenses} as the expenses. Is this correct? Y/N : ')
                if response.lower() == 'n':
                    self.expenses = 0
                elif response.lower() == 'y':
                    entering_expenses = False

    def getInvestment(self):
        entering_investments = True
        while entering_investments:
            if self.initial_investment == 0:
                response = input('What is the initial investment of the property, including any renovations, down payment, closing costs, and misc fees? ')
                self.initial_investment = int(response)
                entering_investments = False
            else:
                response = input(f'You previously entered {self.initial_investment} as the initial investment. Is this correct? Y/N : ')
                if response.lower() == 'n':
                    self.initial_investment = 0
                elif response.lower() == 'y':
                    entering_investments = False

    def calculateROI(self):
        self.cashflow = self.rental_income - self.expenses
        annual_cashflow = self.cashflow * 12
        roi_percentage = (annual_cashflow / self.initial_investment) * 100
        print(f'Your return of investment is {roi_percentage}%')


ROI = ROICalculator()

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
            ROI.getIncome()
        if response.lower() == 'expenses':
            ROI.getExpenses()
        if response.lower() == 'investment':
            ROI.getInvestment()
        if ROI.rental_income != 0 and ROI.expenses != 0 and ROI.initial_investment != 0:
            entering_information = False
    ROI.calculateROI()
    print('Thank you for using our services!')

run()