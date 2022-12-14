# import matplotlib.pyplot as plt
# labels = 'Groceries', 'Bar', 'Pharmacies', 'Pet', 'Transport'
# sizes = [300, 80, 20, 60, 30]
# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, labels = labels, autopct = '%1.1f%%',
#         shadow = True, startangle = 90)
# ax1.axis('equal')
# plt.show()


import sys
import datetime
import csv
import os
import pandas

# from matplotlib import pyplot as plt

# Categories: Groceries, Entertainment, Transport, Eating out, Shopping, Presents
class BudgetCalculator1:
 
    def __init__(self, Category, Date, Value):
        self.Category = Category
        self.Date = Date
        self.Value = 1
 
    def display_info(self):
        print(f"Category: {self.Category}  Date: {self.Date}  Value: {self.Value}")
 
 
groceries.Category = Category("Groceries")
groceries.Date = Date("14.12.2022")
groceries.Value = 100
groceries.display_info()      # Name: Tom  Age: 37
 
entertaiment = Entertainment("Groceries")
entertaiment.Date = Date("13.12.2022")
entertaiment.Value = 150
entertaiment.display_info() 


with open('Categories.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])


"""_______________________________________________________________________________"""

class BudgetCalculator:
        def __init__(self, args):
                self.filename = "storage.csv"
                self.args = args

        def process_arguments(self):
                """OPredeliaem tip deystviya po argumentam iz komandnoi stroki"""
                self.args.cat
                self.args.value
                self.args.a

                if self.args.a:
                        self.add_expence(self.cat, self)
                pass

def _create_file_if_not_exist(self):
        if not os.path.isfile("self.filename"):
                with open(self.filename, "w") as file:
                        file.write("CAtegory , Date, Value")

def _add_expense(self, cat, data, amount, date=datetime.date.today()):
        """Add expense"""

        str_date = to_str

        with open(file) as file:
                file.write("")

def _get_expenses():
        """Get expense"""

        str_date = to_str

        with open(file) as file:
                lines = file.readlines()[1:]

def _get_expenses_by_category(self, data, categories):
        data = self.get_expenses()
        output
        return output

def _get_expenses_by_date(self, data, categories):
        data = self.get_expenses()
        # proveriaem if na datu
        output
        return output



FILENAME = "users.csv"
 
users = [
    {"Category": "Groceries", "Date": "14.12.2022", "Value": 100},
    {"Category": "Entartaiment", "Date": "13.12.2022", "Value": 150},
    {"Category": "Transport", "Date": "12.12.2022", "Value": 15},
]
 
with open(FILENAME, "w") as file:
    columns = ["Category", "Date", "Value"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
     

    writer.writerows(users)
     
    user = {"Category" : "Groceries", "Date": "14.12.2022", "Value": 100}

    writer.writerow(user)
 
with open(FILENAME, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Category"], "-", row["Date"], "-", row["Value"])



def plot_data(data): 

        fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels = labels, autopct = '%1.1f%%',
        shadow = True, startangle = 90)
ax1.axis('equal')
plt.show()

# size - po kazdoi category prosumiruem nashi znachenia
# iz leiblov berem vse unicalnie znachenia(categotrii)