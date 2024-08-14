#The moment a person starts programing in python.

This_is_a_list = [2,3,5,6,63,4,34,344]
        #####This is the next step, because this is the start of an application.
try:
    user_input1= int(input("Enter numbers to the list: "))
    This_is_a_list.append(user_input1)
except ValueError:
    print("Enter only numbers")

This_is_a_list.extend([4334,234,346,5665])

Una_summatory = sum(This_is_a_list)
print("Result of the summatory from the data =",Una_summatory)
print(Una_summatory)