__author__ = 'Monique Tucker'
import time


# class object Expense that requires the name, amount, and who pays the expense
class Expense():
    def __init__(self):
        self.name = (raw_input("Tell me the expense name: ")).lower()
        self.amount = float(input("Tell me the amount of the " + self.name + " expense: "))
        self.who_pays = raw_input("Tell me who paid the " + self.name + " expense: ").lower()

    category = None
    due_date = None

    #can make changes to the name of the expense
    def update_name(self, expense):
        expense.name = raw_input('Change the current expense' + expense.name + ' to: ')
        return expense

    #can make changes to the amount of the expense
    def update_amount(self, expense):
        expense.amount = input('Change the expense amount for ' + expense.name + ' to: ')
        return expense

    #can make changes to who pays the expense
    def update_who_pays(self, expense):
        expense.who_pays = raw_input('Change who pays for the ' + expense.name + ' expense to: ')
        return expense

    #can access the expense by name
    def get_name(self, expense):
        return expense.name

    #can access the expense by who pays
    def get_who_pays(self, expense):
        return expense.who_pays

    #can display entire Expense
    def show_expense(self, expense):
        print "Expense: ", expense.name.capitalize(), "\n", \
            "Amount: $", expense.amount, "\n", \
            "Who pays: ", expense.who_pays.capitalize(), "\n"


# g = Expense()
#g.show_expense(g)
#g.update_who_pays(g)
#print g.who_pays
#print g.get_who_pays(g)

#class object for time period month that calculates
class Month():
    def __init__(self):
        self.month_name = raw_input('Which month are your expenses for? ')

    monthly_expenses = {}
    total = None
    names_of_persons = None
    total_matched_to_person = {}
    who_owes_who = None

    #adds an expense to the dictionary of monthly expenses (total month)
    #TO DO: double star expenses so it can take keyword arguments for expenses
    def add_expense(self, expense):
        new_expense = [expense.name, expense.amount, expense.who_pays, expense.category, expense.due_date]
        self.monthly_expenses.setdefault(self.month_name, [])
        self.monthly_expenses[self.month_name].append(new_expense)
        return self.monthly_expenses

    #sums up total expenses for the month
    def get_total_expenses(self):
        self.total = 0
        for k, v in self.monthly_expenses.items():
            for j in v:
                self.total += j[1]
        return self.total

    #sums up how much was paid for the month for a particular person
    #to do: fix to work more than two people
    def total_paid(self):
        person1_total = 0
        person2_total = 0
        for k, v in self.monthly_expenses.items():
            for j in v:
                if j[2] in self.names_of_persons[0]:
                    person1_total += j[1]
                    self.total_matched_to_person[j[2]] = person1_total
                if j[2] in self.names_of_persons[1]:
                    person2_total += j[1]
                    self.total_matched_to_person[j[2]] = person2_total
        return self.total_matched_to_person

    #tells you all the people who paid for the month
    def all_persons(self):
        self.names_of_persons = []
        for k, v in self.monthly_expenses.items():
            for j in v:
                if j[2] not in self.names_of_persons:
                    self.names_of_persons.append(j[2])
        return self.names_of_persons

    #calculates who owes who
    #to do: fix for what happens if they are both equal. right now takes the first person in list
    #to do: what if there is more than one person involved
    def calc_who_owes_who(self):
        paid_most = max(self.total_matched_to_person, key=self.total_matched_to_person.get)
        paid_least = min(self.total_matched_to_person, key=self.total_matched_to_person.get)
        total_amount_owed = (self.total_matched_to_person[paid_most] / 2) \
                                                  - (self.total_matched_to_person[paid_least] / 2)
        self.who_owes_who = [paid_least.capitalize()+" owes " + paid_most.capitalize(), "$" + str(total_amount_owed)]
        print self.who_owes_who[0] + " " + self.who_owes_who[1]


#class for people who pay household bills
class Person():
    def __init__(self):
        self.person_name = raw_input('What is the name of the person you share expenses with? ')

    #allow person to reconcile expenses for a particular month
    def reconcile_expenses(self):
        reconciled_month = Month()
        add_more_prompt = 'y'
        while add_more_prompt == 'y':
            new_reconcile_expenses = Expense()
            reconciled_month.add_expense(new_reconcile_expenses)
            add_more_prompt = (raw_input("\nWould you like to add another expense for " +
                                         reconciled_month.month_name.capitalize() + "? y/n ")).lower()
        else:
            print('\nNow I will calculate how much is owed...')
            time.sleep(1)
            reconciled_month.get_total_expenses()
            reconciled_month.all_persons()
            reconciled_month.total_paid()
            reconciled_month.calc_who_owes_who()

#testing Person methods
print '\n'
print '==================================================================================='
print '                     This is the financial reconciler '
print '             for couples, roommates, and anyone who shares finances!'
print '===================================================================================', '\n'
time.sleep(1)
p = Person()
p.reconcile_expenses()

##tests of Month class
# g = Expense()
# h = Expense()
# i = Expense()
# f = Month()
# print f.add_expense(g)
# print f.add_expense(h)
# print f.add_expense(i)
# f.get_total_expenses()
# print f.total
# f.total_paid('mo')
# print f.person_total
# print f.monthly_expenses
# print f.get_total_expenses()

##tests of Person class
#m = Person()
#print m.__dict__

# ##test combining person, expense and month
# m = Person()
# j = Person()
# g = Expense()
# h = Expense()
# i = Expense()
# f = Month()
# f.add_expense(g)
# f.add_expense(h)
# f.add_expense(i)
# f.get_total_expenses()
# # print f.total
# f.all_persons()
# f.total_paid(m.person_name)
# f.total_paid(j.person_name)
# # print f.total_matched_to_person
# # print f.names_of_persons
# f.calc_who_owes_who()
# #print f.who_owes_who

#tests of Expense class
# g.due_date = '09/16/14'
# g.category = 'test'
# print(g.due_date)
# print(g.category)
# print(g.name)
# print(g.amount)
# print(g.who_pays)
# g = Expense()
# g.update_who_pays()
#print g.get_name(g)