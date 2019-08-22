""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""
# everything you'll need is imported:
from model import data_manager
from model import common


def add(table, record):
    """
    Add new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
    """
    # your code
    data_manager.get_table_from_file(file_name)
    table.append(record)
    data_manager.write_table_to_file(file_name, table)

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

    # your code

    data_manager.get_table_from_file(file_name)
    for sublist in table:
        if id_ in sublist:
            table.remove(sublist)
    data_manager.write_table_to_file(file_name, table)

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

    # your code
    max_year = table[0][2]

    for sublist in table:
        if sublist[2] < max_year:
            max_year = sublist[2]

    oldest_name = []
    for sublist in table:
        if max_year in sublist:
            oldest_name.append(sublist[1])


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code
    max_year = table[0][2]

    for sublist in table:
        if sublist[2] < max_year:
            max_year = sublist[2]
    print(max_year)

    oldest_name = []
    for sublist in table:
        if max_year in sublist:
            oldest_name.append(sublist[1])
    print(oldest_name)


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
    year_avg = []
    for sublist in table:
        year_avg.append(int(sublist[-1]))

    sum_year = 0
    for element in year_avg:
        sum_year += element

    avg_year = int(sum_year / (len(year_avg)))

    persons_closest_to_average_age = []

    min = abs(avg_year - int(sublist[2]))
    for sublist in table:
        if abs(avg_year - int(sublist[2])) <= min:
            min = abs(avg_year - int((sublist[2])))
            persons_closest_to_average_age.append(sublist[1])
    
    return persons_closest_to_average_age
