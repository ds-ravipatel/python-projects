from BankDB import Customer,Transaction, Reports

#this is bank project
print('*********** WELCOME TO OUR BANK ***************')
while True:
    print('''Choose one of the option Below - 
    1. Customer Management
    2. Transaction Management
    3. Reports''')
    usr_ip = input()
    if usr_ip == '1' or usr_ip == '2' or usr_ip == '3':
        break

if usr_ip == '1':
    cust_id = input("Enter Customer ID -")
    cust_obj = Customer.Customers(cust_id)
    print('--------------------------------------------------------')
    while True:
        print('Select one of the options below :')
        print('1. View Customer Details')
        print('2. Update Customer Record')
        print('3. Delete Customer Record')
        usr_ip = input()
        if usr_ip == '1' or usr_ip == '2' or usr_ip == '3':
            break
    if usr_ip == '1':
        cust_obj.print_cust()
    elif usr_ip == '2':
        cust_obj.upd_cust()
    elif usr_ip == '3':
        cust_obj.del_cust()

elif usr_ip == '2':
    tran_obj = Transaction.Transactions()
    print('--------------------------------------------------------')
    while True:
        print('Select one of the options below :')
        print('1. Add New Transaction ')
        print('2. Update Transaction Record')
        print('3. Delete Transaction Record')
        usr_ip = input()
        if usr_ip == '1' or usr_ip == '2' or usr_ip == '3':
            break
    if usr_ip == '1':
        tran_obj.new_tran()
        tran_obj.commit_tran()
        balance = tran_obj.account_bal()
        tran_obj.upd_balance(balance)
    elif usr_ip == '2':
        tran_id = input("Enter Transaction ID : ")
        AccountNo = input("Enter Account No : ")
        tran_obj.upd_tran(tran_id,AccountNo)
        balance = tran_obj.account_bal()
        tran_obj.upd_balance(balance)
    elif usr_ip == '3':
        tran_id = input("Enter Transaction ID : ")
        AccountNo = input("Enter Account No : ")
        tran_obj.del_tran(tran_id, AccountNo)
        balance = tran_obj.account_bal()
        tran_obj.upd_balance(balance)
elif usr_ip == '3':
    print('--------------------------------------------------------')
    while True:
        print('Select one of the Reports below :')
        print('1. Get Transactions Details by Account Number ')
        print('2. Get Customer Details by Name ')
        print('3. Search by given field and text ')
        usr_ip = input()
        if usr_ip == '1' or usr_ip == '2' or usr_ip == '3':
            break
    if usr_ip == '1':
        print('--------------------------------------------------------')
        inputs = []
        while True:
            inp = input('Enter Account Number : ')
            if inp == '':
                break
            inputs.append(str(inp))
        Reports.display_tran_details(*inputs)
    if usr_ip == '3':
        col_name = input("Enter Field to be searched - ")
        print('Select one of the option below :')
        print(f"1 : 'sd?'  : all {col_name} starting with s and followed by 0 or 1 number of d")
        print(f"2 : 'sd+'  : all {col_name} starting with s and followed by atleast 1 number of d")
        print(f"3 : 'sd*'  : all {col_name} starting with s and followed by 0 or any number of d")
        opt = input()
        text = input("Enter text - ")
        print('--------------------------------------------------------')
        out = Reports.re_start_with(col_name, text, opt)
        print(out)





