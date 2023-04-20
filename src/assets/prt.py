import datetime
from csv import reader
import csv

# read the CSV file
def load_csv():
    # Open file in read mode
    file = open('cvs_test1.csv',"r")
    # Reading file 
    lines = reader(file)
    
    # Converting into a list 
    data = list(lines)
    process(data)
    return data

def date(data):
    split = data.split("/")
    month = int(split[0])
    day = int(split[1])
    year = int(split[2])
    d = datetime.datetime(year, month, day)
    return(d)


def time(data):
    split = data.split(":")
    hour = int(split[0])
    minute = int(split[1])
    t = datetime.time(hour, minute)
    return t
 

def process(data):
    end_Day ="06/01/2023" #for testing purposes
    end_time = "00:00"
    start_Day = input("Please enter the start date in mm/dd/yyyy format \n")
    start_time = input("Please enter the start time in hh:mm format \n")

    i =1
    D_start_index = None
    D_end_index = None

    j=1
    while j<len(data):
        data[j][0] = date(data[j][0])
        j+=1

    while i<len(data):
        if date(start_Day) >= data[i][0]:
           D_start_index = i
           break
        i+=1


    while i<len(data):
        if date(end_Day) <= data[i][0]:
            D_end_index = i
            break
            
        i+=1

    if D_start_index == None:
        print("Start value is invalid")
    elif D_end_index == None:
         print("End value is invalid")
    else:
        if time(start_time) != None and data[D_start_index][0] == date(start_Day):
            j =D_start_index
            while j<D_end_index:
                 if time(start_time) <= time(data[j][1]) and data[D_start_index][0] == date(start_Day):
                     D_start_index = j
                     break
                 j+=1
            j =D_start_index
            while j<D_end_index:
                 if time(end_time) >= time(data[j][1]) and data[D_end_index][0] == date(end_Day):
                     D_end_index = j
                     break
                 j+=1
           
        j =D_start_index
        while j<D_end_index:        
            handle.append(float(data[j][2]))
            j+=1  
    stats(handle)


def Avg(lst):
    return sum(lst) / len(lst)

def stats(handel):
    print("The average voltage read is " + str(Avg(handel)))
    print("The max voltage read is " +  str(max(handel)))
    print("The min voltage read is " +  str(min(handel)))
    fields = ['average', 'min', 'max']
    row = [str(Avg(handel)),str(max(handel)), str(min(handel))]
    name = "cvs_test1avg.csv"
    with open(name, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerow(row)

   
    


handle = []
load_csv()
