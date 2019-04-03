import csv


import csv
with open("new_names.csv",'r') as csvf:
    read_csv=csv.reader(csvf)
    next(read_csv)
    for x in read_csv:
        print(x[2])
 '''
 OUTPUT:>>>
 john-doe@bogusemail.com
maryjacobs@bogusemail.com
davesmith@bogusemail.com
janestuart@bogusemail.com
tomwright@bogusemail.com'
 
 '''
   
    
with open("new_names.csv",'r') as csvf:
    read_csv=csv.reader(csvf)
    with open("my_newcsvfile.csv",'w') as ncsvf:
        write_csv=csv.writer(ncsvf,delimiter='-')
        for x in read_csv:
            write_csv.writerow(x)

            
   #then new file will bw as follows            
'''

first_name-last_name-email

John-Doe-"john-doe@bogusemail.com"

Mary-"Smith-Robinson"-maryjacobs@bogusemail.com

Dave-Smith-davesmith@bogusemail.com

Jane-Stuart-janestuart@bogusemail.com

Tom-Wright-tomwright@bogusemail.com

Steve-Robinson-steverobinson@bogusemail.com

Nicole-Jacobs-nicolejacobs@bogusemail.com

'''




        

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
