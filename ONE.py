def hello_name(user_name):
    print(f'hello_{user_name}!')

    return

def first_odds():
    for first_number in range(1,100,2):
        print(first_number)
    return

def max_num_in_list(a_list):
   a_list.sort()
   return a_list.pop()

def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 == 0 and a_year % 400 == 0:
        
        
        return True
    elif a_year % 4 == 0 and a_year % 100 != 0 and a_year % 400 != 0:
        
        
        return True
    elif a_year % 4 != 0:
        return False

def is_consecutive(a_list):
   sum_of_list = sum(a_list)
   first_number_in_list = a_list[0]
   length_of_list = len(a_list)
   counter = 0
   while counter < length_of_list:
    number_counter = a_list[0]
    number_counter = number_counter + 1
    counter = counter + 1
    print(counter)
    print(number_counter)

def is_consecutive(a_list):
   sum_of_list = sum(a_list)
   length_of_list = len(a_list)
   number_counter = a_list[0]
   counter = 1
   while counter < length_of_list + 1:
    number_counter = number_counter + (1*counter)
    counter = counter + 1
   if sum_of_list == number_counter -1: 
    print("it might be in ascending order")
    return True
   else:  
    print('not in ascending order')
    return False
    
  
   

hello_name("mason")
first_odds()
max_num_in_list([1,2,3,5,4])
is_leap_year(2024)
is_consecutive([1,2,3,4,5,7])
