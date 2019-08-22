""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    the_longest_name = table[0][1]
    id_the_longest_name = table[0][0]
    longest_names_id = {}

    for collection in table:
        if len(collection[1]) > len(the_longest_name):
            the_longest_name = collection[1]
            id_the_longest_name = collection[0]
        elif len(collection[1]) == len(the_longest_name):
            longest_names_id[collection[1]] = collection[0]

    longest_names_id = list(longest_names_id.items())
    for collection in longest_names_id:
        i = 0
        for letter in collection:
            if letter.lower() > the_longest_name[i].lower():
                the_longest_name = collection[0]
                id_the_longest_name = collection[1]
    return id_the_longest_name

# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    email_name = []
    for collection in table:
        if collection[3] == "1":
            email_name.append(collection[2] + ";" + collection[1]) 
    return email_name
