import csv,os

def write_data2file(file_name,csv_cols=[], data = [], mode ='a'):
    #print(file_name)
    with open(file_name,mode,newline='') as f:
        writer = csv.DictWriter(f,fieldnames=csv_cols)
        if mode == 'w':
            writer.writeheader()
        writer.writerows(data)
    ''' below is to write list data
    with open(file_name,mode,newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    '''
def ReadDataFromFile(file_name,csv_cols=[], data = ''):
    #print(file_name)
    with open(file_name,'r',newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            #print(f'data is {data}')
            #print(f'Cust id  is {row["Cust_id"]}')
            if row["Cust_id"] == data:
                #print(row)
                #print(type(row))
                d = dict(row)
                #print(d)
                #print(type(d))
                for k,v in d.items():
                    print(f'{k}:{v}')
                    #OverWriteRow(file_name,csv_cols,data)

def OverWriteRow(file_name,csv_cols=[], data = ''):
    with open(file_name, 'r') as csvfile, open(file_name, 'w') as output:
        reader = csv.DictReader(csvfile, fieldnames=csv_cols)
        writer = csv.DictWriter(output, fieldnames=csv_cols)

        for row in reader:
            if data == row['Cust_id']:
                FirstName=''
                row['FirstName'] = input(f"enter new name for {FirstName}")
            # write the row either way
            writer.writerow({'Cust_id':row['Cust_id'],'AccountNo':row['AccountNo'],'FirstName':row['FirstName'],'LastName':row['LastName'],'Age':row['Age'],'Address':row['Address'],'Balance':row['Balance'],'StartDate':row['StartDate'],'EndDate':row['EndDate']})