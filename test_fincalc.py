__author__ = 'Monique Tucker'

from fincalc_wc import Expense, Person, Month
#tests for fincalc_wc program
#tests of Month class
g = Expense()
h = Expense()
i = Expense()
f = Month()

print f.add_expense(g)
print f.add_expense(h)
print f.add_expense(i)
f.get_total_expenses()
print f.total
f.total_paid()
print f.total_matched_to_person
print f.monthly_expenses
print f.get_total_expenses()

#tests of Person class
m = Person()
print m.__dict__

#test combining person, expense and month
m = Person()
j = Person()
g = Expense()
h = Expense()
i = Expense()
f = Month()

f.add_expense(g)
f.add_expense(h)
f.add_expense(i)
f.get_total_expenses()
print f.total
f.all_persons()
f.total_paid()
f.total_paid()
print f.total_matched_to_person
print f.names_of_persons
f.calc_who_owes_who()
print f.who_owes_who

#tests of Expense class
g.due_date = '09/16/14'
g.category = 'test'
print(g.due_date)
print(g.category)
print(g.name)
print(g.amount)
print(g.who_pays)
g = Expense()
g.update_who_pays(g)
print g.get_name(g)

#test out calculation of who owes who using for loop
total_matched_to_person = {'mo': 130.00, 'jo': 1000.00}
all_persons = ['mo', 'jo']
#take amount paid. split in half. see which amount is bigger. then subtract accordingly
#split each to add
split_mo = (total_matched_to_person['mo']/2)
split_jo = (total_matched_to_person['jo']/2)


for i in total_matched_to_person:
    for j in all_persons:
        if i == j:
            print i, total_matched_to_person[i]


#to do - what happens if they are equal amounts
# test to calculate who owes who using max and min
x = max(total_matched_to_person, key=total_matched_to_person.get)
y = min(total_matched_to_person, key=total_matched_to_person.get)
print y, "owes", x, "$", (total_matched_to_person[x]/2) - (total_matched_to_person[y]/2)

if total_matched_to_person['mo'] != total_matched_to_person['jo']:
    print max(total_matched_to_person, key=total_matched_to_person.get)
else:
    print "Looks like you paid equal amounts this month!"

print len(total_matched_to_person)

#test to calculate who owes who using a split calculation
if split_mo > split_jo:
    print "Jo owes Mo: $", split_mo - split_jo
elif split_jo > split_mo:
    print "Mo owes Jo: $", split_jo - split_mo
else:
    print "Looks like you paid equal amounts this month!"

monthly_expenses = {'may': [['gas', 45, 'jo'], ['phone', 100, 'mo'], ['gym', 80, 'mo'], ['cable', 150, 'jo']]}
names_of_persons = ['mo', 'jo']
person_total = 0


#test to see that sum of personal finances is created
def total_owed():
    #person_total = 0
    for k, v in monthly_expenses.items():
        for j in v:
            print j[2], j[1]
            # if j[2] == p:
            #     person_total += j[1]
#    return person_total

total_owed()


#test to see that a list of persons involved gets updated
def all_persons():
    for k, v in monthly_expenses.items():
        for j in v:
            if j[2] not in names_of_persons:
                names_of_persons.append(j[2])
    return names_of_persons

all_persons()
print names_of_persons


#test to sum with more than one person
def person_sum(**person):
    total = 0
    for k, v in monthly_expenses.items():
        for j in v:
            if j[2] == person:
                total += j[1]
        print total

person_sum(person='mo', person='jo')


#working code to sum expenses according to the particular person
def person_sum(person):
    total = 0
    for k, v in monthly_expenses.items():
        for j in v:
            if j[2] == person:
                total += j[1]
        print total


for k, v in monthly_expenses.items():
    for j in v:
        if j[2] == 'mo':
            print j[1]
