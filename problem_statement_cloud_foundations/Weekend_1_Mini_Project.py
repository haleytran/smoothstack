import pandas as pd
import datetime 
import logging

def main():
    logging.basicConfig(filename="problem_statement_cloud_foundations/Mini_Project.log", 
                        encoding="utf-8", 
                        format="%(asctime)s %(message)s", 
                        datefmt="%m/%d/%Y %I:%M:%S %p", 
                        level="DEBUG")
    logging.info("Writting to log")
    
    file = input("Enter file name or path: ")
    logging.info("File entered: {}".format(file))
    
    monthly_report(file)


def monthly_report(file):
    month, year = parse(file) # get month and year desired
    logging.info("Extracting desired month and year ...\nMonth: {}\nYear: {}".format(month, year))
    
    table = pd.read_excel(file) # extract table from file
    logging.info("Reading table from file ....\n{}".format(table))
    
    col_names = table.columns # column names
    
    date_col_index = list(col_names).index("Calls Offered") - 1 # index of date column name
    
    date_col_name = col_names[date_col_index] # date column name
    
    # convert desired month and year to datetime.datetime object
    date = date_generate(month, year)
    
    # remove any row that doesn't contain a date
    table = table.drop([x for x in table.index if type(table[date_col_name][x]) != type(date)])
    
    # add another date column to contain only month and year
    month_year = [date_generate(x.month, x.year) for x in table[date_col_name]]
    table["Date"] = month_year
    
    date_table = table[table["Date"] == date] # table containing the row desired
    logging.info("Executing monthly report ....")
    
    if len(date_table.index) != 0:
        
        # names of desired columns
        calls_offered = col_names[date_col_index + 1]
        abandon_after_30s = col_names[date_col_index + 2]
        fcr = col_names[date_col_index + 3]
        dsat = col_names[date_col_index + 4]
        csat = col_names[date_col_index + 5]

        for i in range(len(date_table.index)):
            result = "{}: {}\n{}: {} \n{}: {}\n{}: {}\n{}: {}".format(calls_offered, int(date_table.get(calls_offered).tolist()[i]), 
                                                            abandon_after_30s.lstrip(" "), percent(date_table.get(abandon_after_30s), i), 
                                                            fcr, percent(date_table.get(fcr), i), 
                                                            dsat, percent(date_table.get(dsat), i), 
                                                            csat, percent(date_table.get(csat), i))
            
            logging.info("Extracting data .... COMPLETE\nFor {} {}:\n{}".format(month, year, result))
      
        logging.info("Executing monthly report .... COMPLETE")
    else:
        logging.info("Executing monthly report .... NOTHING TO REPORT")


def parse(s):
    lst = s.split("_")
    month = datetime.datetime.strptime(lst[-2], "%B").month
    year = lst[-1].split(".")[0]
    return (month, year)


def date_generate(month, year):
    date_string = "{} {}".format(month, year)
    date_format = "%m %Y"
    return datetime.datetime.strptime(date_string, date_format)


def percent(num, i):
    return "{:.2f}%".format(num.tolist()[i]*100)


main()
