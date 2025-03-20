'''
Python Express

A project by:
Ong, Precious Roshayne
Tafalla, Carl Andrei
Tolentino, Wayne Ian

In partial fulfillment in the course Programming Logic and Design Lecture, under Mr. John Vincent Cortez.

Updates:
V1.0 - added main function, and some functions to be defined later for main menu 

'''
# Clear screen code, referencing GeeksforGeeks.org
import os
import order
from order import orders, menu_options

def rev_order():
    raise NotImplementedError


def admin_check():
    clear_screen()
    password = input("Enter admin password: ")
    if password == "PROLOGI-123":  # Replace with a secure password
        admin_menu()
    else:
        print("Incorrect password. Access denied.")
    input("\nPress Enter to return to the main menu...")
    clear_screen()


def view_all_orders():
    clear_screen()
    if not orders:
        print("No orders have been placed yet.")
    else:
        print("All Orders:")
        for order in orders:
            print(f"- {order}")

def add_menu_item():
    clear_screen()
    item_number = input("Enter the number for the new item: ")
    item_name = input("Enter the name of the new item: ")
    menu_options[item_number] = item_name
    print(f"Added '{item_name}' to the menu!")

def remove_menu_item():
    clear_screen()
    item_number = input("Enter the number of the item to remove: ")
    if item_number in menu_options:
        removed_item = menu_options.pop(item_number)
        print(f"Removed '{removed_item}' from the menu.")
    else:
        print("Item not found in the menu.")

def reset_orders():
    clear_screen()
    orders.clear()
    print("All orders have been reset.")

def admin_menu():
    clear_screen()
    while True:
        print("\tAdmin Menu")
        print("-" * 100 + "\n\n")
        admin_options = [
            '[1] View All Orders',
            '[2] Add Menu Item',
            '[3] Remove Menu Item',
            '[4] Reset Orders',
            '[5] Return to Main Menu'
        ]
        for option in admin_options:
            print(option.center(100))
        
        choice = input("\n\nPlease select an option: ")
        
        match choice:
            case '1':
                view_all_orders()
            case '2':
                add_menu_item()
            case '3':
                remove_menu_item()
            case '4':
                reset_orders()
            case '5':
                print("Returning to the main menu...")
                break
            case _:
                print("Invalid choice. Please try again.")
        input("\nPress Enter to continue...")
        clear_screen()



def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def main():
# Main Menu Screen
    clear_screen()
    while True:
        
        print("\tWelcome to Python Express, where we move at slithering speeds to make your order!")
        print("-" * 100 + "\n\n")
    
        mmtxt = ['Main Menu\n', '[1] View Menu', '[2] Add to Order', '[3] Review Order', '[4] Finalize Order', '[5] Admin Settings', '[6] Exit']
        for txt in mmtxt:
            print(txt.center(100))
        
        sel = 0
        sel = input("\n\nPlease select an option. ")
    
        match sel:
            case '1':
                clear_screen()
                order.display_menu()
                input("\nPress Enter to return to the main menu...")
                clear_screen()
            case '2':
                order.add_to_order()
            case '3':
                rev_order()
            case '4':
                print("Order has been finalized. Please wait, printing your receipt!")
                rev_order()
                break
            case '5':
                admin_check() # integrate function admin_menu() once done, as well as the main menu for admin and its functions
            case '6':
                print("Thank you for using Python Express!")
                break
            case _:
                clear_screen()
                print("Invalid choice. Please try again.") 
                
            

if __name__ == "__main__":
    main()