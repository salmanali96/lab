import csv
import math
def find_element_in_list(element, list_element):
    try:
        index_element = list_element.index(element)
        return index_element
    except ValueError:
        return None
#print ('The nearby cities area assumed to be in the range of 150km from the queried city.');
#print('Enter the name of the city you wish to search.');

#cityName = input();
list1 = []
priority = []

with open('Academic _Schedule.csv') as csvfile:  # Loading geo-locaion.csv file.
     reader = csv.DictReader(csvfile)
     for row in reader:
         #print('StartDate',row['StartDate'],'EndDate',row['EndDate'],'Activity',row['Activity'])
         #print (row['Activity'])

          
                   
              

          if row['Activity'] not in list1:
             list1.append(row['Activity'])

     list1[0] = list1[0] + '(9am)'
     list1[3] = list1[3] + '(9am)'
     list1[2] = list1[2] + '(9am)'
     list1[5] = list1[5] + '(9am)'
     list1[12] = list1[12] + '(9am)'
     list1[8] = list1[8] + '(9am)'
     list1[9] = list1[9] + '(9am)'
     list1[10] = list1[10] + '(9am)'
     list1[11] = list1[11] + '(9am)'
     list1[6] = list1[6] + '(9am)'
     list1[14] = list1[14] + '(9am)'
     list1[15] = list1[15] + '(9am)'
     list1[16] = list1[16] + '(9am)'
     list1[17] = list1[17] + '(9am)'
     list1[18] = list1[18] + '(9am)'




     priority.append(list1[0])
     priority.append(list1[2])
     priority.append(list1[5])
     priority.append(list1[1])
     priority.append(list1[7])
     priority.append(list1[13])
     priority.append(list1[15])
     priority.append(list1[16])
     priority.append(list1[3])
     priority.append(list1[4])
     priority.append(list1[6])
     priority.append(list1[8])
     priority.append(list1[9])
     priority.append(list1[10])
     priority.append(list1[11])
     priority.append(list1[12])
     priority.append(list1[14])
     priority.append(list1[17])
     priority.append(list1[18])
     priority.append(list1[19])

     print(list1)
     count = 0;
     dict2 = []


with open('names.csv', 'w') as csvfile1:
          fieldnames = ['Start Date', 'Last Date','Activity']
          writer = csv.DictWriter(csvfile1, fieldnames=fieldnames)
          writer.writeheader()
         # priority = find_element_in_list(row['Activity'], list_element)
          with open('Academic _Schedule.csv') as csvfile:  # Loading geo-locaion.csv file.
               reader = csv.DictReader(csvfile)
               for row in reader:
                    writer.writerow({'Start Date':row['StartDate'], 'Last Date':row['EndDate'], 'Activity':row['Activity']})

              

          


          
               
                     
               
               
               
                              
                    
          
     



#print (len(priority))

              
        
