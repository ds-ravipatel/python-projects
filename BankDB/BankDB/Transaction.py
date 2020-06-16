import sqlite3
import datetime

def create_tables():
    conn = sqlite3.connect('BankDB.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS xxtransactions (tran_id number, AccountNo text, tran_type text, amount real, tran_date text)")
    conn.commit()
    conn.close()

class Transactions:
    def __init__(self):
        self.tran_id = 0
        self.AccountNo = ''
        self.tran_type = ''
        self.amount = 0
        self.tran_date = '2020-01-01'

    def new_tran(self):
        conn = sqlite3.connect('BankDB.db')
        c = conn.cursor()
        c.execute("SELECT max(tran_id)+1 FROM xxtransactions")
        tran_id = c.fetchone()[0]
        conn.commit()
        conn.close()
        self.tran_id = tran_id
        print('Enter Transaction Details :')
        while True:
            self.AccountNo = input("Enter Account No -")
            if self.AccountNo != '':
                break
        while True:
            self.tran_type = input("Enter Transaction Type (D/C) -")
            if self.tran_type == 'D' or self.tran_type == 'C':
                break
        while True:
            self.amount = input("Enter Transaction amount -")
            if int(self.amount) > 0:
                break
        self.tran_date = datetime.datetime.now()
        #self.print_transaction()

    def commit_tran(self):
        conn = sqlite3.connect('BankDB.db')
        c = conn.cursor()
        if self.tran_type == 'D' and self.account_bal()-int(self.amount) < 0:
            print('Insufficient Funds for this Debit Entry...!!!!')
            print('This Transaction is discarded')
        else:
            c.execute(
            """INSERT INTO xxtransactions VALUES(:tran_id,:AccountNo,:tran_type,:amount,:tran_date)""",
                #{'tran_id': self.tran_id, 'AccountNo': self.AccountNo, 'tran_type': self.tran_type, 'amount': self.amount})
            {'tran_id': self.tran_id, 'AccountNo': self.AccountNo, 'tran_type': self.tran_type,'amount': self.amount,'tran_date':self.tran_date})
            print("************ Transaction Added Successfully ***************")
            self.print_transaction()
        conn.commit()
        conn.close()

    def print_transaction(self):
        print('------- Transaction Details --------')
        print(f'Transaction ID   : {self.tran_id}')
        print(f'Account No.      : {self.AccountNo}')
        print(f'Transaction Type : {self.tran_type}')
        print(f'Amount           : {self.amount}')
        print(f'Transaction Date : {self.tran_date}')

    def account_bal(self):
        conn = sqlite3.connect('BankDB.db')
        c = conn.cursor()
        tot_credit = 0
        for row in c.execute("SELECT SUM(amount) FROM xxtransactions WHERE AccountNo = :AccountNo AND tran_type = :tran_type",
                  {'AccountNo':self.AccountNo,'tran_type':'C'}):
            if row[0] is not None:
                tot_credit = row[0]
        tot_debit = 0
        for row in c.execute("SELECT SUM(amount) FROM xxtransactions WHERE AccountNo = :AccountNo AND tran_type = :tran_type",
                  {'AccountNo': self.AccountNo, 'tran_type': 'D'}):
            if row[0] is not None:
                tot_debit = row[0]
        #print(tot_debit)
        #print(tot_credit)
        balance = tot_credit - tot_debit
        conn.commit()
        conn.close()
        return balance

    def upd_balance(self,balance):
        conn = sqlite3.connect('BankDB.db')
        c = conn.cursor()
        c.execute("UPDATE xxcustomers SET balance = :balance WHERE AccountNo = :AccountNo",
                  {'AccountNo': self.AccountNo, 'balance': balance})
        conn.commit()
        conn.close()

    def upd_tran(self, tran_id, AccountNo):
        self.tran_id = tran_id
        self.AccountNo = AccountNo
        l_tran_id = 0
        conn = sqlite3.connect('BankDB.db')
        c = conn.cursor()
        for row in c.execute("SELECT * FROM xxtransactions WHERE AccountNo = :AccountNo AND tran_id = :tran_id",
                  {'AccountNo': self.AccountNo, 'tran_id': self.tran_id}):
            self.tran_type, self.amount,self.tran_date = row[2], row[3], row[4]
        if self.amount != 0:
            self.print_transaction()
            while True:
                self.tran_type = input("Enter New Transaction Type (D/C) -")
                if self.tran_type == 'D' or self.tran_type == 'C':
                    break
            while True:
                self.amount = input("Enter New Transaction amount -")
                if int(self.amount) > 0:
                    break
            if self.tran_type == 'D' and self.account_bal() - int(self.amount) < 0:
                print('Insufficient Funds for this Debit Entry...!!!!')
                print('This Transaction is discarded')
            else:
                c.execute("UPDATE xxtransactions SET tran_type = :tran_type, amount = :amount WHERE AccountNo = :AccountNo AND tran_id = :tran_id",
                      {'AccountNo': self.AccountNo, 'tran_id': self.tran_id, 'tran_type':self.tran_type, 'amount':self.amount})
                print("Transaction Updated Successfully..!!!")
        else:
            print('No Transaction with Given Combination..!!')
        conn.commit()
        conn.close()

    def del_tran(self, tran_id, AccountNo):
        self.tran_id = tran_id
        self.AccountNo = AccountNo
        l_tran_id = 0
        conn = sqlite3.connect('BankDB.db')
        c = conn.cursor()
        for row in c.execute("SELECT * FROM xxtransactions WHERE AccountNo = :AccountNo AND tran_id = :tran_id",
                  {'AccountNo': self.AccountNo, 'tran_id': self.tran_id}):
            self.tran_type, self.amount, self.tran_date = row[2], row[3], row[4]
        if self.amount != 0:
            self.print_transaction()
            l_del = 'N'
            while True:
                l_del = input("Delete this Transaction ? (Y/N) -")
                if l_del == 'Y' or l_del == 'N':
                    break
            if l_del == 'Y':
                conn.commit()
                c.execute("DELETE FROM xxtransactions WHERE AccountNo = :AccountNo AND tran_id = :tran_id",
                          {'AccountNo': self.AccountNo, 'tran_id': self.tran_id})
                conn.commit()
                print(f'Transaction with transaction id {self.tran_id} deleted.')
                ''' this is not working, we have to calculate balance in same session to get correct value
                print(self.account_bal())
                if self.account_bal() < 0:
                    conn.rollback()
                    print('Balance going to negative. Rolling back the transaction..!!')
                else:
                    conn.commit()
                '''
            else:
                print("Transaction Cancelled..!!!")
        else:
            print('No Transaction with Given Combination..!!')
        conn.commit()
        conn.close()



