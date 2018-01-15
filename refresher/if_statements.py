# know_people = ['Jon', 'Alex', 'Jen', 'Shiloh', 'Luna']
# person = input('Who do you know: ')
# 
# if person in know_people:
#     print('You know {}!'.format(person))
# else:
#     print('You do not know {}'.format(person))


def who_do_you_know():
    people = input('What are the names of the people you know, sepatated by commas:  ')
    people_list = people.split(',')
    return people_list

print(who_do_you_know())

def ask_user():
    pass



