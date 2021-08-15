# Author : Bhagyashree Nayak
# Date : 08/15/2021
# version : 1
""" This program will read the txt data and header file and combine them into CSV file.
Then it will move the CSV file to destination"""
# ************************Change#:1********************************
# Change(s) Made: Initial build
# Date of Change: 08/15/2021
# Author: Bhagyashree Nayak
# Change Approved by: Bhagyashree Nayak
# Date Moved to Production: 08/15/2021
# ******************************************************************
import csv
from some_storage_library import SomeStorageLibrary as sl
from file_checker import check_files as cf

if __name__ == '__main__':
    """
    This is the entrypoint to the program. 
    'python main.py' will be executed and the expected csv file should exist in ../data/destination/ after the execution is complete.

    """
    """Entrypoint"""
    print('Beginning the ETL process...')
    # defining the file path
    filepath = '/data/source/'
    csv_file = 'sourcedata_with_header.csv'  # Final .csv file name
    # calling the get file function to get list  of files.
    file_list = cf.get_files(filepath)
    # Printing the file location but we can log it using logger because printing is costly
    print(file_list)
    header_file = file_list[0]  # Assigning header file to a variable
    data_file = file_list[1]  # Assigning data file to a variable
    try:
        fhand = open(header_file)
    except:
        print('file cannot be opened: ', header_file)
        exit()
    header_name = dict()
    for line in fhand:  # Reading the header file through each line
        line = line.strip()  # Removing extra space in each line
        words = line.split('|')  # Spliting each line into words
        header_name[int(words[0])] = words[
            1]  # Making one dictionary containing key as the column number and value being the column name
    lst = list(header_name.keys())  # Listing all the column number to sort
    lst.sort()
    header = list()
    for key in lst:
        header_list = header.append(header_name[key])
    print(header)  # Printing sorted header list

    try:
        with open(csv_file, 'w', newline='') as csv_data:  # opening the csv file
            write_file = csv.writer(csv_data, delimiter=',')
            write_file.writerow(header)  # writting the header names
            with open(data_file, 'r', newline='') as pipe_data:  # opening the data file
                stripped = (line.strip() for line in pipe_data)
                lines = (line.split("|") for line in stripped if line)  # splitting the data line by line
                # writing the writer with \r to avoid blank lines between each record.
                # This is happening  because of windows text mode by default uses /r/n
                writer = csv.writer(csv_data, lineterminator='\r')
                writer.writerows(lines)  # writing
                print('CSV file generated as', csv_file)

    except:
        print('wrong file name or file cannot be opened: ', data_file)
        exit()
    sl.load_csv(csv_file) #pass the data to move to destination
