import csv
import datetime

with open('All Transactions - Bankkonto CoBa.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('postgres_bk_final.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)

        next(csv_reader)

        for line in csv_reader:
            line[29] = line[7].replace("€", '').replace(",", '')
            line[10] = 0
            line[4]  = datetime.datetime.strptime(line[4], '%d.%m.%Y').strftime('%Y-%m-%d')
            line[5]  = datetime.datetime.strptime(line[5], '%d.%m.%Y').strftime('%Y-%m-%d')
            line[6]  = datetime.datetime.strptime(line[6], '%d.%m.%Y').strftime('%Y-%m-%d')
            
            csv_writer.writerow( (line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[8],
            line[9], line[10], line[11], line[12], line[13], line[14], line[16],
            line[17], line[18], line[19], line[20], line[21], line[22], line[23] , line[24], line[25], line[26], line[27], line[31], line[29]) )

            


           
 
