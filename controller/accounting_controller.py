# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
from controller import common

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    options = ["Add new record",
               "Remove record",
               "Update record",
               "Which year has the highest profit?",
               "What is the average (per item) profit in a given year?"]

    terminal_view.print_menu("Menu", options, "Back to Main Menu")
