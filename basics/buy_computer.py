available_parts = ["computer","monitor","keyboard","mouse","mouse pad","Hdmi cable"]

current_choice ="-"
computer_parts=[] #empty list

while current_choice != '0':
    if current_choice in "123456":
        print("Adding {}".format(current_choice))
        if current_choice=='1':
            computer_parts.append("Computer")
        elif current_choice == '2':
            computer_parts.append("Monitor")
        elif current_choice == '3':
            computer_parts.append("Keyboard")
        elif current_choice == '4':
            computer_parts.append("Mouse")
        elif current_choice == '5':
            computer_parts.append("Mouse pad")
        elif current_choice == '6':
            computer_parts.append("Hdmi cable")

    else:
        print("Please add option from the list below")
        #Inefficient for long lists
        """for parts in available_parts:
            print("{0}:{1}".format(available_parts.index(parts)+1,parts))"""
        
        #Using Enumeration
        for number , parts in enumerate(available_parts):
            print("{0}:{1}".format(number+1,parts))

    current_choice = input()

print(computer_parts)