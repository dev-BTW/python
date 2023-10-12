"""Write a program to print a number of options and alo user to select option from list 
The options should be numbered from 1-9 of minimum 4 options should be there
The program should conyinue looping allowing user to choose one option each time around
and only terminate when user chooses 0 
If user makes a valid choice the program should print a short message
The message should include the value they typed
If choice is not in menu nothing should be printed (Optional: menu should be printed again)"""

option_list =["Exit","Learn Python","Learn Java","Learn SQL","Learn PHP"]
#print(len(option_list))
while True:
    for i in range(len(option_list)):
        print("{0}:- {1}".format(i,option_list[i]))
    user_input = int(input("Select a number to confirm that option: "))
    if 0 < user_input <= len(option_list)-1:
        print("Great you've selected option {0} which is {1}\n".format(user_input,option_list[user_input]))
    elif user_input==0:
        print("You selected option {0} which means to {1}\n".format(user_input,option_list[user_input]))
        break
    else:
        print("Select a valid option or select 0 to exit: ")
        continue
