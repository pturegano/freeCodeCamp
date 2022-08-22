import math

class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self,amount,description):
        self.ledger.append({"amount":amount,"description":description})
        
    def withdraw(self,amount,description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount,"description":description})
            return True
        
    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i["amount"]
        return balance
        
    def transfer(self,amount,category):
        self.withdraw(amount,"Transfer to " + category.category)
        category.deposit(amount,"Transfer from " + self.category)    

    def check_funds(self,amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        line1,line2,line3 = "","",""
        line1 = self.category.center(30,"*") + "\n"
        for i in self.ledger:
            line2 += i["description"][:23].ljust(23) + str("{:.2f}".format(i["amount"])).rjust(7)
            line2 += "\n"
        line3 = "Total: " + str(self.get_balance())
        return line1 + line2 + line3

def create_spend_chart(categories):
    category_spending = []
    
    for category in categories:
        spending = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spending += item["amount"] * -1
        category_spending.append(spending)
    totalSpending = sum(category_spending)
    for i in range(len(category_spending)):
        category_spending[i] = round(category_spending[i]/totalSpending*10)    

    line1 = "Percentage spent by category\n"
    chart = ""
    for index in reversed(range(11)):
        col1 = str(index*10).zfill(3)+"|"
        if index == 0:
            col1 = col1.replace("0"," ",2)
        elif index < 10:
            col1 = col1.replace("0"," ",1)
        
        for i in range(len(category_spending)):
            if category_spending[i] > index:
                col1 += " o "
            else:
                col1 += "   "
        chart += col1 + "\n"
    
    line2 = "    -" + "---"*len(categories) + "-\n"
    line3 = ""
    repeat = True
    index = 0
    while repeat:
        line3 += "     "
        repeat = False
        for cat in categories:
            catName = cat.category
            if len(catName) > index:
                line3 += catName[index] + "  "
                repeat = True
            else:
                line3 += "   " 
        line3 += "\n"
        index += 1

            
    result = line1 + chart + line2 + line3
    return result
