# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
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
               "What is the id of the customer with the longest name?",
               "Which customers has subscribed to the newsletter?"]
    data = common.get_table("/home/stanki/Desktop/ERP_TW/erp-mvc-marcin_marcin_natalia/model/crm/customers.csv")
    print(data)
    title_list = ["id", "Name", "Email", "Subscribed"]
    common.draw_table(data, title_list)
    terminal_view.print_menu("Menu", options, "Back to Main Menu")
    choice = terminal_view.get_choice(options)

    while choice != "0":
        if choice == "1":
            store_controller.run()
        elif choice == "2":
            hr_controller.run()
        elif choice == "3":
            inventory_controller.run()
        elif choice == "4":
            accounting_controller.run()
        elif choice == "5":
            sales_controller.run()
        elif choice == "6":
            crm_controller.run()
        else:
            terminal_view.print_error_message("There is no such choice.")

