""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
from model import data_manager
from model import common


#print(data_manager.get_table_from_file("items.csv"))

def add(table, record):
    """
    Add new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
    """
    # data_manager.get_table_from_file("items.csv")
    table.append(record)
    # data_manager.write_table_to_file(file_name, table)

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """
    # data_manager.get_table_from_file("items.csv")
    for collection in table:
        if collection[0] == id_:
            table.remove(collection)
    # data_manager.write_table_to_file(file_name, table)

    return table


def update(table, id_, record):
    """
    Updates specified record in the table.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
        record (list): updated record

    Returns:
        list: table with updated record
    """

    i = 0
    for collection in table:
        if collection[0] == id_:
            table[i] = record
            i += 1

    return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    profit_year = {}
    for collection in table:
        if collection[3] not in profit_year:
            profit_year[collection[3]] = 0
        if collection[4] == "in":
            profit_year[collection[3]] += int(collection[5])
        else:
            profit_year[collection[3]] -= int(collection[5])

    years_profits = list(profit_year.items())
    the_best_year = years_profits[0][0]
    the_best_profit = float(years_profits[0][0])
    for collection in years_profits:
        if collection[1] > the_best_profit:
            the_best_profit = collection[1]
            the_best_year = float(collection[0])
    return the_best_year


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # your code
