__author__ = 'Monique Tucker'
import time

"""
WHO OWES WHO??:
This program reconciles finances for two people to determine who owes who at the end of a month.

Future enhancements:
* Allow user to access Expense methods
* Allow more than 2 people to reconcile finances
* Ability to determine % of split (i.e. not automatically an even split)
* Ability to display entire expenses for the month in a user friendly format
* Ability to export file of expenses
* Ability to add category and due date information
* Compare trends from month to month
"""


# class object Expense that requires the name, amount, and who pays the expense
class Expense():
    def __init__(self):
        self.name = (raw_input("Tell me the expense name: ")).lower()
        self.amount = float(input("Tell me the amount of the " + self.name + " expense: "))
        self.who_pays = raw_input("Tell me who paid the " + self.name + " expense: ").lower()

    category = None
    due_date = None

    def update_name(self, expense):
        """
        This function allows the user to make changes to the name of the expense.
        :param expense: defined instance of Expense.
        :return: Updates the Expense object with its new name.
        """
        expense.name = raw_input('Change the current expense' + expense.name + ' to: ')
        return expense

    def update_amount(self, expense):
        """
        This function allows the user to make changes to the amount of the expense.
        :param expense: defined instance of Expense.
        :return: Updates the Expense object with its new amount.
        """
        expense.amount = input('Change the expense amount for ' + expense.name + ' to: ')
        return expense

    def update_who_pays(self, expense):
        """
        This function allows the user to make changes to who paid the expense.
        :param expense: defined instance of Expense.
        :return: Updates the Expense object with the new person who paid.
        """
        expense.who_pays = raw_input('Change who pays for the ' + expense.name + ' expense to: ')
        return expense

    def get_name(self, expense):
        """
        This function allows access to the Expense by name.
        :param expense: defined instance of Expense.
        :return: The name of the Expense instance.
        """
        return expense.name

    def get_who_pays(self, expense):
        """
        This function allows access to the Expense by who paid it.
        :param expense: defined instance of Expense.
        :return: who paid the Expense instance.
        """
        return expense.who_pays

    #can display entire Expense
    def show_expense(self, expense):
        """
        This function displays the expense name, amount, and who paid in a user friendly format.
        :param expense: defined instance of Expense.
        :return: Displays instance of Expense attributes.
        """
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

    #TO DO: double star expenses so it can take keyword arguments for expenses
    def add_expense(self, expense):
        """
        This function compiles all expenses for the month into a retrievable format.
        :param expense: Comes from the Expense class.
        :return: A dictionary of all expenses entered for the particular month with the month as the key.
        """
        new_expense = [expense.name, expense.amount, expense.who_pays, expense.category, expense.due_date]
        self.monthly_expenses.setdefault(self.month_name, [])
        self.monthly_expenses[self.month_name].append(new_expense)
        return self.monthly_expenses

    def get_total_expenses(self):
        """
        This function sums up total expenses for the month using items from the monthly_expenses dictionary.
        :return: A sum of total expenses as a float.
        """
        self.total = 0
        for k, v in self.monthly_expenses.items():
            for j in v:
                self.total += j[1]
        return self.total

    #to do: fix to work more than two people
    def total_paid(self):
        """
        This function sums up how much money was paid for the month for each person.
        :return: A dictionary with 2 elements. Each key is equal to a person and the
        value is equal to the person's total expense amount for the month.
        """
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

    def all_persons(self):
        """
        This function tells you all the people who paid expenses for the month.
        :return: A list of the persons who paid for expenses that month.
        """
        self.names_of_persons = []
        for k, v in self.monthly_expenses.items():
            for j in v:
                if j[2] not in self.names_of_persons:
                    self.names_of_persons.append(j[2])
        return self.names_of_persons

    #to do: fix for what happens if they are both equal. right now takes the first person in list
    #to do: what if there is more than one person involved
    def calc_who_owes_who(self):
        """
        This function calculates who owes who at the end of the month by taking an even split of
        all finances paid.
        :return: Statement displaying who owes who what dollar amount.
        """
        paid_most = max(self.total_matched_to_person, key=self.total_matched_to_person.get)
        paid_least = min(self.total_matched_to_person, key=self.total_matched_to_person.get)
        total_amount_owed = (self.total_matched_to_person[paid_most] / 2) \
                                                  - (self.total_matched_to_person[paid_least] / 2)
        self.who_owes_who = [paid_least.capitalize()+" owes " + paid_most.capitalize(), "$" + str(total_amount_owed)]
        print '>>>>>', self.who_owes_who[0] + " " + self.who_owes_who[1], '<<<<<'


#class for people who pay household bills
class Person():
    def __init__(self):
        self.person_name = raw_input('What is the name of the person you share expenses with? ')

    def reconcile_expenses(self):
        """
        This function reconciles expenses for a given month by taking user input of expense information,
        creating a Month class to compile the expenses and then calculate who owes who.
        :return: Statement displaying who owes who what dollar amount.
        """
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

#main program
print '\n'
print '==================================================================================='
print '                                   WHO OWES WHO??:                                   '
print '                     A financial reconciler for couples, roommates,                '
print '                          and anyone who shares finances!                          '
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

# #test combining person, expense and month
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