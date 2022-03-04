import csv
##READING CSV FILES
f = open('csv_file.csv')
f_csv = csv.reader(f)
print(type(f_csv))
for row in f_csv:
    name, phoneno, rltn = row
    print('Name:{}, PhoneNo:{}, Relation:{}'.format(name,phoneno,rltn))
f.close()

 ### WRITING TO CSV FILES
hosts = [['workstation.local','192.168.9.1'],['webserver.cloud', '10.2.4.3']]
with open('hosts.csv','w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

## DICT READER
with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print("{} has {} users".format(row['name'], row['users']))


##dict writer
users = [{'name':'Adil Imran','username':'emraanadil', 'department':'IT Infrastructure'},
        {'name':'Irfan Iqbal','username':'pintooirfan','department':'Football'},
        {'name':'Tasleema Iqbal','username':'reenu','department':'Physics'}

]

keys = ['name', 'username', 'department']
with open('employees.csv','w') as file:
    writer = csv.DictWriter(file,fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)


