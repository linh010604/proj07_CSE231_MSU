'''
    Computer Project #7
    Algorithm
        openfile()
        read_file()
        get_data_in_range()
        get_min()
        get_max()
        get_average()
        get_modes()
        high_low_averages()
        display_statistics()
        main()
'''
import csv
from datetime import datetime
from operator import itemgetter

COLUMNS = ["date", "average temp", "high temp", "low temp", "precipitation", \
           "snow", "snow depth"]

TOL = 0.02

BANNER = 'This program will take in csv files with weather data and compare \
the sets.\nThe data is available for high, low, and average temperatures,\
\nprecipitation, and snow and snow depth.'

MENU = '''
        Menu Options:
        1. Highest value for a specific column for all cities
        2. Lowest value for a specific column for all cities
        3. Average value for a specific column for all cities
        4. Modes for a specific column for all cities
        5. Summary Statistics for a specific column for a specific city
        6. High and low averages for each category across all data
        7. Quit
        Menu Choice: '''

def open_files():
    '''
    prompts the user to enter a series of cities separated by comma and returns a list of
    cities and a list of file pointers that correspond to that list of cities. If a particular city is not found,
    print an error message and do not insert it in the list of file pointers.
    return:
        cities_list - a list of strings
        list_of_fp - a list of file pointers
    display:
        error message
    '''
    city = input("Enter cities names: ") # prompt for series of cities separated by comma
    cities = city.split(",") # split input to list of cities
    list_of_fp = []
    cities_list = []
    for city2 in cities :
        city1 = city2 + ".csv"
        try : # try to find the city in cities list
            fp = open(city1, "r", encoding="utf-8")
            list_of_fp.append(fp) # add file pointer to list
            cities_list.append(city2) # add city to list
        except: # not find the city
            print("\nError: File {} is not found".format(city1)) # print error message

    return cities_list , list_of_fp

def read_files(cities_fp):
    '''
    read file pointer in the list and add information to a list of lists of tuples
    value:
        cities_fp - a list of file pointers
    return:
        list_of_list_tuples -  a list of lists of tuples
    '''
    list_of_list_tuples = []
    for city_fp in cities_fp:# for each file pointer in the list
        city_list = []
        reader = csv.reader(city_fp)
        # skip the first 2 lines
        next(reader,None)
        next(reader,None)
        for line in reader : # for each line in file pointer
            information_list = []
            # format and add data to a tuple
            line[0] = str(line[0])
            information_list.append(line[0])
            for idx in range(1,7):
                try:
                    line[idx] = float(line[idx])
                except:
                    line[idx] = None
                information_list.append(line[idx])
            information_tuple = tuple(information_list)
            # add tuple to a list
            city_list.append(information_tuple)
        city_fp.close() # close file
        # add a list of tuples to a list
        list_of_list_tuples.append(city_list)
    return list_of_list_tuples

def get_data_in_range(master_list, start_str, end_str):
    '''
    keep all the tuples in data with dates in – between the start and end
    dates inclusive
    value:
        master_list - a list of  lists of tuples - take from read_file()
        start_str - string - date string
        end_str - string - date string
    return:
        list_of_list_tuples - a list of lists of tuples
    '''
    # format date string to datetime
    start_date = datetime.strptime(start_str, "%m/%d/%Y").date()
    end_date = datetime.strptime(end_str, "%m/%d/%Y").date()
    list_of_list_tuples = []
    # compare datetime to keep the data in range in a new list
    for city in master_list:
        city_list = []
        for infor in city:
            date = datetime.strptime(infor[0], "%m/%d/%Y").date()
            if date >= start_date and date <= end_date :
                city_list.append(infor)
        list_of_list_tuples.append(city_list)

    return list_of_list_tuples

def get_min(col, data, cities):
    '''
    finds the minimum value of the corresponding column for each city in list.
    value:
        col - int - column index
        data - list of lists of tuples
        cities - list of strings
    return:
        list_of_tuples - list of tuples - contain list of tuples of city and its min value
    '''
    list_of_tuples = []
    for idx , city in enumerate(data):
        min_value = 1000
        # find min column value of each city
        for info in city :
            try:
                min_value = min(min_value,info[col])
            except:
                continue
        list_of_tuples.append((cities[idx],min_value))
    return list_of_tuples

def get_max(col, data, cities):
    '''
    finds the maximum value of the corresponding column for each city in list.
    value:
        col - int - column index
        data - list of lists of tuples
        cities - list of strings
    return:
        list_of_tuples - list of tuples - contain list of tuples of city and its max value
    '''
    list_of_tuples = []
    # find max column value of each city
    for idx , city in enumerate(data):
        max_value = 0
        for info in city :
            try:
                max_value = max(max_value,info[col])
            except:
                continue
        list_of_tuples.append((cities[idx],max_value))
    return list_of_tuples

def get_average(col, data, cities):
    '''
    finds the average value of the corresponding column col for each city in cities rounded to 2 decimals
    value:
        col - int - column index
        data - list of lists of tuples
        cities - list of strings
    return:
        list_of_tuples - list of tuples - contain list of tuples of city and its max average
    '''
    list_of_tuples = []
    for idx, city in enumerate(data):
        total = 0
        count = 0
        # calculate total data of the column
        for info in city:
            try: # if value != None
                total += info[col]
            except:
                count += 1
                continue
        average = total/(len(city)-count) # calculate the average
        list_of_tuples.append((cities[idx], round(average,2)))
    return list_of_tuples

def get_modes(col, data, cities):
    '''
    finds the list of modes, or the most common value in the column col for each city in cities.
    value:
        col - int - column index
        data - list of lists of tuples
        cities - list of strings
    return:
        list_of_tuples - list of tuples - contain list of tuples of city and its mode
    '''
    list_of_tuples = []
    for idx, city in enumerate(data) :
        col_list = []
        # create a list of column value
        for info in city:
            if info[col] != None :
                col_list.append(info[col])
        col_list.sort() # sort the value list
        # recreate the list with only number after checking tolerance
        for idx1 , number in enumerate(col_list):
            if idx1 > 0 and  col_list[idx1-1] != 0 \
            and abs((number - col_list[idx1-1])/col_list[idx1-1]) <= TOL :
                col_list[idx1] = col_list[idx1-1]
        # count the appearance and find mode of the list
        check_list = [cities[idx],[],0]
        idx1 = max_number = 0
        while idx1 < len(col_list):
            number = col_list.count(col_list[idx1])
            max_number_check = max_number
            if col_list[idx1] != 0 :
                max_number = max(max_number,number)
                if max_number_check != max_number:
                    check_list[1] = []
                    check_list[1].append(col_list[idx1])
                    check_list[2] = max_number
                elif max_number == number:
                    check_list[1].append(col_list[idx1])
            idx1 += number
        if check_list[2] == 1 :
            check_list[1] = []
        list_of_tuples.append(tuple(check_list))
    return list_of_tuples

def high_low_averages(data, cities, categories):
    ''' Docstring'''
    categories_list = []
    for category in categories:
        if category in COLUMNS:
            category_list = get_average(COLUMNS.index(category),data,cities)
            category_list.sort(key=itemgetter(1))
            tuple1 = category_list[0]
            category_list.sort(key=itemgetter(1),reverse = True)
            tuple2 = category_list[0]
            categories_list.append([tuple1,tuple2])
        else:
            categories_list.append(None)
    return categories_list

def display_statistics(col, data, cities):
    ''' Docstring'''
    min_list = get_min(col,data,cities)
    max_list = get_max(col,data,cities)
    average_list = get_average(col,data,cities)
    modes_list = get_modes(col,data,cities)
    print("\n\t{}: ".format(COLUMNS[col]))
    for idx , info in enumerate(min_list) :
        print("\t{}: ".format(info[0]))
        print("\tMin: {:.2f} Max: {:.2f} Avg: {:.2f}".\
        format(info[1],max_list[idx][1],average_list[idx][1]))
        string = ''
        for item in modes_list[idx][1] :
            string = string + str(item) + ','
        string = string[:-1]
        if string.strip() != '' :
            print("\tMost common repeated values ({:d} occurrences): {:s}\n"\
            .format(modes_list[idx][2],string))
        else:
            print("\tNo modes.")

def main():
    print(BANNER)
    cities_list , cities_fp = open_files()
    master_list = read_files(cities_fp)
    while 1 :
        option = input(MENU)
        if option == '1' :
            start_date = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end_date = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            date_list = get_data_in_range(master_list, start_date, end_date)
            while 1:
                category = input("\nEnter desired category: ")
                category = category.lower()
                if category in COLUMNS:
                    break
                print("\n\t{} category is not found.".format(category))

            max_list = get_max(COLUMNS.index(category),date_list,cities_list)
            print("\n\t{}: ".format(category))
            for item in max_list:
                print("\tMax for {:s}: {:.2f}".format(item[0],item[1]))
        elif option == '2' :
            start_date = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end_date = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            date_list = get_data_in_range(master_list, start_date, end_date)
            while 1:
                category = input("\nEnter desired category: ")
                category = category.lower()
                if category in COLUMNS:
                    break
                print("\n\t{} category is not found.".format(category))

            min_list = get_min(COLUMNS.index(category),date_list,cities_list)
            print("\n\t{}: ".format(category))
            for item in min_list:
                print("\tMin for {:s}: {:.2f}".format(item[0],item[1]))
        elif option == '3':
            start_date = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end_date = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            date_list = get_data_in_range(master_list, start_date, end_date)
            while 1:
                category = input("\nEnter desired category: ")
                category = category.lower()
                if category in COLUMNS:
                    break
                print("\n\t{} category is not found.".format(category))

            average_list = get_average(COLUMNS.index(category),date_list,cities_list)
            print("\n\t{}: ".format(category))
            for item in average_list:
                print("\tAverage for {:s}: {:.2f}".format(item[0],item[1]))
        elif option == '4' :
            start_date = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end_date = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            date_list = get_data_in_range(master_list, start_date, end_date)
            while 1:
                category = input("\nEnter desired category: ")
                category = category.lower()
                if category in COLUMNS:
                    break
                print("\n\t{} category is not found.".format(category))

            modes_list = get_modes(COLUMNS.index(category), date_list, cities_list)
            print("\n\t{}: ".format(category))
            for item in modes_list:
                string = ''
                for number in item[1]:
                    string = string + str(number) + ','
                if len(string[:-1].strip()) != 0 :
                    print("\tMost common repeated values for {:s} ({:d} occurrences): {:s}\n"\
                    .format(item[0],item[2],string[:-1]))
                else :
                    print("\tNo modes.")
        elif option == '5' :
            start_date = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end_date = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            date_list = get_data_in_range(master_list, start_date, end_date)
            while 1:
                category = input("\nEnter desired category: ")
                category = category.lower()
                if category in COLUMNS:
                    break
                print("\n\t{} category is not found.".format(category))

            display_statistics(COLUMNS.index(category),date_list,cities_list)
        elif option == '6':
            start_date = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end_date = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            date_list = get_data_in_range(master_list, start_date, end_date)
            categories = input("\nEnter desired categories seperated by comma: ")
            categories = categories.lower().split(',')
            categories_list = high_low_averages(date_list,cities_list,categories)
            print("\nHigh and low averages for each category across all data.")
            for idx , category in enumerate(categories) :

                if categories_list[idx] != None:
                    print("\n\t{}: ".format(category))
                    print("\tLowest Average: {:s} = {:.2f} Highest Average: {:s} = {:.2f}"\
                          .format(categories_list[idx][0][0],categories_list[idx][0][1],\
                                  categories_list[idx][1][0],categories_list[idx][1][1]))
                else :
                    print("\n\t{} category is not found.".format(category))

        else :
            print("\nThank you using this program!")
            break

# DO NOT CHANGE THE FOLLOWING TWO LINES OR ADD TO THEM
# ALL USER INTERACTIONS SHOULD BE IMPLEMENTED IN THE MAIN FUNCTION
if __name__ == "__main__":
    main()