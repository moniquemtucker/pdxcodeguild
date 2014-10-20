print ("Welcome to our basic phone book!")
#create a updateable phonebook with test entry
phonebook = {'joe': ['joe', '123 elm st', '123-456-1234'], 'monique': ['monique', '2626 SW Corbett', '646-123-4567']}

#ask user what they want to do add, search or delete
choice = raw_input ('Would you like to add, search, or delete an entry? ')

#user chooses to add an entry
if choice == 'add':
#create input variables for entry
    new_name = raw_input('What is the first and last name? ')
    new_address = raw_input('What is the current address? ')
    new_phone = raw_input('What is the phone number? ')
#create dictionary for new entry    
    new_entry = {new_name: [new_name, new_address, new_phone]}
#show entry in user friendly format    
    d = {'n': new_entry[new_name][0], 'a': new_entry[new_name][1], 'p': new_entry[new_name][2]}
    template = """
    %(n)s
    %(a)s
    %(p)s
    has been added.
    """
    print (template % d)
    phonebook.update(new_entry)
#test that phonebook has been updated
   # print (phonebook)

#user chooses to search an entry
elif choice == 'search':
#create input variable for what user wants to search 
    find = raw_input('Who do you want to find? ')
#show address entry if found in phonebook in user friendly format
    if phonebook.has_key(find):	
        d = {'n': phonebook[find][0], 'a': phonebook[find][1], 'p': phonebook[find][2]}
        template = """
        %(n)s
        %(a)s
        %(p)s
        """
        print (template % d)
#show UTL message if entry is not found
    else:
        print ('This entry ' + find + ' does not exist.')

#user chooses to delete an entry from phonebook
elif choice == 'delete':
#create variable for user delete choice
    delete = raw_input('Who do you want to delete? ')
#create conditional statement dependent on if entry exists
    if phonebook.has_key(delete):
#puts entry in user friendly format
        d = {'n': phonebook[delete][0], 'a': phonebook[delete][1], 'p': phonebook[delete][2]}
        template = """
            %(n)s
            %(a)s
            %(p)s
            """
        print (template % d)
#confirm user wants to delete entry displayed
        answer = raw_input ('Are you sure you want to delete ' + delete + ' y/n? ')
#delete entry if user confirms y
        if answer == 'y':
            phonebook.pop(delete)
            print(delete + " has been deleted.")
#test that entry has been removed
#	        print(phonebook)
        else:
            print('You changed your mind!')
    else:
        print ('The entry ' + delete + ' does not exist.')
#default if user does not type add, search, or delete 
else:
    print ('Please choose an option.')



