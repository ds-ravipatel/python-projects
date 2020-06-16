import sqlite3,re

def display_tran_details(*args):
    whr_clause = "select * from xxtransactions where AccountNo IN ("
    for i in range(len(args)):
        if i == len(args)-1:
            whr_clause = whr_clause + "'" + str(args[i]) + "'"
        else:
            whr_clause = whr_clause + "'" + str(args[i]) + "',"
    whr_clause = whr_clause + ") order by AccountNo, tran_id"
    #print(whr_clause)
    conn = sqlite3.connect('BankDB.db')
    c = conn.cursor()
    c.execute(whr_clause)
    print("****************** ACCOUNT WISE TRANSACTION REPORT ***********************")
    print("TranID   AccountNo   TranType   Amount           TranDate                 ")
    for row in c.fetchall():
        i, j, k, l, m = row[0], row[1], row[2], row[3], row[4]
        print(f'{i:<8} {j:<11} {k:<10} {l:<16} {m[:19]:<20}')

def re_start_with(col_name,text,opt):
    sql_stm = "select "+ col_name + " FROM xxcustomers"
    conn = sqlite3.connect('BankDB.db')
    c = conn.cursor()
    c.execute(sql_stm)
    all_out = []
    for row in c.fetchall():
        all_out.append(row[0])
    #print(all_out)
    if opt == '1':
        text = text + "?"
    elif opt == '2':
        text = text + "+"
    elif opt == '3':
        text = text + "*"
    out = []
    for i in all_out:
        if re.search(text, i):
            out.append(i)
    #print(out)
    return out


