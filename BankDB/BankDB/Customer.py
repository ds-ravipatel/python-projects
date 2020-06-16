import sqlite3

def create_tables():
    conn = sqlite3.connect('BankDB.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS xxcustomers (cust_id number,AccountNo text, FirstName text, LastName text, balance real, address text, active text)")
    conn.commit()
    conn.close()

class Customers:

    def __init__(self,cust_id):
        self.cust_id = cust_id
        self.AccountNo=''
        self.get_cust()
        if self.AccountNo == '':
            # below when we want to add new customer
            print('Customer Does not exists with this Customer ID. Please enter below details to add new customer :')
            while True:
                self.AccountNo = input("Enter Account Number -")
                if self.AccountNo != '':
                    break
            while True:
                self.FirstName = input("Enter First Name -")
                if self.FirstName != '':
                    break
            self.LastName = input("Enter Last Name -")
            self.balance = input("Enter Initial Balance -")
            if self.balance == '':
                self.balance = 0
            while True:
                self.address = input("Enter Address -")
                if self.address != '':
                    break
            self.active = 'Y'
            self.add_cust()
        else:
            print('Customer already exists with this Customer ID.')
            self.get_cust()
            self.print_cust()

    def add_cust(self):
        conn = sqlite3.connect('BankDB.db')
        c = conn.cursor()
        c.execute("""INSERT INTO xxcustomers VALUES(:cust_id,:AccountNo,:FirstName,:LastName,:balance,:address,:active)""",{'cust_id':self.cust_id,'AccountNo':self.AccountNo,'FirstName':self.FirstName,'LastName':self.LastName,'balance':self.balance,'address':self.address,'active':self.active})
        conn.commit()
        conn.close()
        print("************ CUSTOMER ADDED ***************")

    def get_cust(self):
        conn = sqlite3.connect('BankDB.db')
        c = conn.cursor()
        for row in c.execute("SELECT * FROM xxcustomers where cust_id=:cust_id",{'cust_id':self.cust_id}):
            self.AccountNo = row[1]
            self.FirstName = row[2]
            self.LastName = row[3]
            self.balance = row[4]
            self.address = row[5]
            self.active = row[6]

    def print_cust(self):
        print('************ CUSTOMER DETAILS *************')
        print(f'Customer ID : {self.cust_id}')
        print(f'Account No  : {self.AccountNo}')
        print(f'First Name  : {self.FirstName}')
        print(f'Last Name   : {self.LastName}')
        print(f'Balance     : {self.balance}')
        print(f'Address     : {self.address}')
        print(f'Active      : {self.active}')

    def upd_cust(self):
        new_fname = input("Enter New First Name :")
        if new_fname != '':
            self.FirstName = new_fname
        new_lname = input("Enter New Last Name :")
        if new_lname != '':
            self.LastName = new_lname
        new_add = input("Enter New Address :")
        if new_add != '':
            self.address = new_add
        new_flag = input("Enter Active Flag :")
        if new_flag != '':
            self.active = new_flag

        if new_fname != '' or new_lname != '' or new_add != '' or new_flag != '':
            conn = sqlite3.connect('BankDB.db')
            c = conn.cursor()
            c.execute("""UPDATE xxcustomers SET FirstName = :FirstName, LastName=:LastName, address=:address, active=:active WHERE cust_id=:cust_id""",{'cust_id': self.cust_id, 'FirstName': self.FirstName,'LastName': self.LastName, 'address': self.address, 'active': self.active})
            conn.commit()
            conn.close()
            print("************ CUSTOMER UPDATED ***************")
            self.get_cust()
            self.print_cust()
        else:
            print("Nothing to update..!!!")
            self.get_cust()

    def del_cust(self):
        self.get_cust()
        if self.AccountNo != '':
            conn = sqlite3.connect('BankDB.db')
            c = conn.cursor()
            c.execute("""DELETE FROM xxcustomers WHERE cust_id=:cust_id""",{'cust_id': self.cust_id})
            conn.commit()
            conn.close()
            print("************ CUSTOMER RECORD DELETED ***************")
        else:
            print("Record not found")
