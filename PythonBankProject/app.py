from CustomerMgmt.Customer import add_cust,take_input,search_cust

print('Please select options from below')
print('1. Customer Management')
usr_input = input()
if usr_input == '1':
    print('Chose one of below')
    print('A. Add New Customer')
    print('B. Update existing Customer')
    usr_sub_input = input()
    if usr_sub_input == 'A':
        print("Enter Below Details for New Customer - ")
        l_data = take_input()
        add_cust(l_data)
    if usr_sub_input == 'B':
        print('Enter Customer Id to be updated - ')
        l_data = input()
        search_cust(l_data)
else:
    print('Incorrect Option Selected')
