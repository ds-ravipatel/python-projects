
from FileHandling.FileHandle import write_data2file,ReadDataFromFile
import os

cust_file = 'CustomerDetails.csv'
cust_cols = ['Cust_id','AccountNo','FirstName','LastName','Age','Address','Balance','StartDate','EndDate']

def take_input():
    d = {}
    l = []
    for i in cust_cols:
        usr_input = input(f"{i}:")
        d[i] = usr_input
    l.append(d)
    return l

def search_cust(data):
    ReadDataFromFile(cust_file,cust_cols,data)

def add_cust(data):
    write_data2file(cust_file,cust_cols, data, 'a')
    print('Customer Added..!!!')

def upd_cust(data):
    pass




'''below code - use to go into data folder and save file there . This is not working
current_dir = os.getcwd()
data_folder = 'data'

file_with_path = os.path.join(current_dir,data_folder,file)
#print(file_with_path)
file_with_path = "D:\PyCharmProjects\PythonBankProject\data\CustomerDetails.csv"


#data sample to create and add record to file
data = [['Cust_id','AccountNo','FName','LName','Age','Address','Balance','StartDate','EndDate'],
        [1,'BANK00000001','Ravi','Patel',30,'Ravet',20000,'1-JAN-2019','']]

#data sample to append data to file
data = [[2,'BANK00000101','Shashank','Nigade',30,'Katraj',40000,'1-SEP-2019','']
       ,[3,'BANK00000021','Manoj','Bangad',30,'Rahatani',200000,'1-JAN-2010','']]

'''
