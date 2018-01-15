# my_variable = 'hello'
# 
# for character in my_variable:
#     print(character)
# 
# my_list = [1, 4, 6, 7]
# 
# for num in my_list:
#     print(num ** 2)
# 

user_wants_number = True
while user_wants_number:
    print(10)
    user_input = input('Should we pring again? (y/n)')
    if user_input == 'n':
        user_wants_number = False
