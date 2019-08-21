""" Terminal view module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    table_marker = "-"
    separator = "|"
    space = " "
    max_len_elements = []
    i = 0
    while i < len(title_list):
        max_len_element_collection = []
        for collection in table:
            max_len_element_collection.append(collection[i])
        i += 1
        max_len_element = max_len_element_collection[0]
        for element in max_len_element_collection:
            if len(element) > len(max_len_element):
                max_len_element = element
        max_len_elements.append(max_len_element)
        print(max_len_element_collection)
        print(max_len_elements)
    max_len_title = []

    i = 0
    while i < len(max_len_elements):
        if len(title_list[i]) > len(max_len_elements[i]):
            max_len_title.append(title_list[i])
        else: 
            max_len_title.append(max_len_elements[i])
        i += 1

    print(max_len_title)
    total_length = 0
    for title in max_len_title:
        total_length += len(title)
    print(total_length)
    print(len(max_len_title))

    main_line = table_marker * (total_length + (2 * len(max_len_title) + len(separator) * (len(max_len_title) + 1)))
    print(main_line)
    i = 0
    while i < len(title_list) - 1:
        print(f"{separator}{(title_list[i]).center(len(max_len_title[i]) + 2 * len(space))}", end="")
        i += 1
    print(f"{separator}{(title_list[i]).center(len(max_len_title[i]) + 2 * len(space))}{separator}")
    print(main_line)
    for collection in table:
        i = 0
        for element in collection:
            if i < len(title_list) - 1:
                print("{}{}".format(separator, element.center(len(max_len_title[i]) + 2 * len(space))), end="")
                i += 1
            else:
                print("{}{}{}".format(separator, element.center(len(max_len_title[i]) + 2 * len(space)), separator))
                print(main_line)


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    n = "\n"
    print(f"{label}: {n}{result}")


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    print(title, ":")
    for index in range(len(list_options)):
        print("\t{} {}".format(index + 1, list_options[index]))
    print("\t0 {}".format(exit_message))


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []

    # your code
    print(title, ":")
    for index in range(len(list_labels)):
        print("\t{}:".format(list_labels[index]), end=' ')
        user_input = input()
        inputs.append(user_input)  

    return inputs

def get_choice(options):
    print_menu("Main menu",options, "Exit program")
    inputs = get_inputs(["Please enter a number: "], "")
    return inputs[0]

def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
#######################################################################################################

    print("Error", message, sep='')


#######################################################################################################

    # your code
