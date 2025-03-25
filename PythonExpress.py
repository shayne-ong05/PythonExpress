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
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()

# Menu Items
menu_options = {
    '1': ("French Fries - ₱250", "snack"),
    '2': ("Onion Rings - ₱270", "snack"),
    '3': ("Mozzarella Sticks - ₱290", "snack"),
    '4': ("Quesadillas - ₱300", "snack"),
    '5': ("Nachos with Cheese - ₱280", "snack"),
    '6': ("Caesar Salad - ₱260", "snack"),

    '7': ("Fish & Chips - ₱550", "seafood"),
    '8': ("Grilled Shrimp Skewers - ₱750", "seafood"),

    '9': ("Beef Broccoli - ₱600", "beef"),
    '10': ("Beef Tenderloin - ₱950", "beef"),

    '11': ("Grilled Pork Steak - ₱650", "pork"),
    '12': ("Baby Back Ribs - ₱900", "pork"),

    '13': ("Chicken Parmesan - ₱620", "chicken"),
    '14': ("Stir-fry Honey Garlic Chicken - ₱580", "chicken"),
    '15': ("Roasted Duck - ₱990", "chicken"),

    '16': ("Spaghetti Aglio E Olio - ₱520", "pasta"),
    '17': ("Chicken Spinach Alfredo Pasta - ₱680", "pasta"),
    '18': ("Pesto Pasta - ₱600", "pasta"),

    '19': ("Hot Coffee - ₱180", "hot drink"),
    '20': ("Green Tea - ₱160", "hot drink"),

    '21': ("Iced Coffee - ₱190", "cold drink"),
    '22': ("Lemon Iced Tea - ₱170", "cold drink"),
    '23': ("Apple Juice - ₱150", "cold drink"),
    '24': ("Pineapple Juice - ₱180", "cold drink"),
    '25': ("Matcha - ₱200", "cold drink"),
}

allorders = []

# Function to display the menu
def display_menu():
    menu_text = f"""
🍽 WELCOME TO PYTHON EXPRESS 🍽
Each item is assigned a number. Simply type the number of the item to add it to your cart.
We hope that you'll enjoy your time with us! Happy ordering!

🥪 SNACKS:  
\t1. {menu_options['1'][0]}\t\t2. {menu_options['2'][0]}  
\t3. {menu_options['3'][0]}\t4. {menu_options['4'][0]}  
\t5. {menu_options['5'][0]}\t6. {menu_options['6'][0]}  

🐟 SEAFOOD:  
\t7. {menu_options['7'][0]}\t8. {menu_options['8'][0]}  

🥩 BEEF:  
\t9. {menu_options['9'][0]}\t10. {menu_options['10'][0]}  

🐖 PORK:  
\t11. {menu_options['11'][0]}\t12. {menu_options['12'][0]}  

🍗 CHICKEN:  
\t13. {menu_options['13'][0]} 14. {menu_options['14'][0]}  
\t15. {menu_options['15'][0]}  

🍝 PASTA:  
\t16. {menu_options['16'][0]}  
\t17. {menu_options['17'][0]}  
\t18. {menu_options['18'][0]}  

🔥 HOT DRINKS:  
\t19. {menu_options['19'][0]}\t20. {menu_options['20'][0]}  

❄️ COLD DRINKS:  
\t21. {menu_options['21'][0]}\t22. {menu_options['22'][0]}  
\t23. {menu_options['23'][0]}\t24. {menu_options['24'][0]}  
\t25. {menu_options['25'][0]}  
"""
    console.print(Panel(menu_text, title="🍽 FOOD & DRINKS MENU", border_style="blue"))
    input("\nPress 0 to return: ")

# Function to add items to the order
def add_to_order():
    console.print("\n🛒 Are you ready to place an order?", style="bold cyan")
    console.print("Press [1] if you want to start ordering")
    console.print("Press [0] if you want to return to the main menu")

    choice = input("\nChoice: ").strip()

    if choice == '0':
        return  # Return to main menu
    elif choice == '1':
        display_menu()  # Show menu ONCE before ordering starts
    else:
        console.print("❌ Invalid choice, please enter 1 to order or 0 to return!", style="bold red")
        return

    # Order selection loop
    while True:
        order = input("\nEnter item number to add (or '0' to go back to the main menu): ").strip().upper()

        if order == '0':
            return  # Go back to main menu
        elif order in menu_options:
            item_name, _ = menu_options[order]
            allorders.append(item_name)
            console.print(f"✅ Added {item_name} to your order!\n", style="bold green")
        else:
            console.print("❌ Invalid choice, please try again!", style="bold red")


# Function to review the order
def add_to_order():
    console.print("\n🛒 Are you ready to place an order?", style="bold cyan")
    console.print("Press [1] to start ordering")
    console.print("Press [0] to return to the main menu")

    choice = input("\nYour choice: ").strip()

    if choice == '0':
        return  # Return to main menu
    elif choice == '1':
        # Show menu without "Press 0"
        menu_text = """
🥪 SNACKS:  
\t1. French Fries - ₱250\t\t2. Onion Rings - ₱270  
\t3. Mozzarella Sticks - ₱290\t4. Quesadillas - ₱300  
\t5. Nachos with Cheese - ₱280\t6. Caesar Salad - ₱260  

🐟 SEAFOOD:  
\t7. Fish & Chips - ₱550\t8. Grilled Shrimp Skewers - ₱750  

🥩 BEEF:  
\t9. Beef Broccoli - ₱600\t10. Beef Tenderloin - ₱950  

🐖 PORK:  
\t11. Grilled Pork Steak - ₱650\t12. Baby Back Ribs - ₱900  

🍗 CHICKEN:  
\t13. Chicken Parmesan - ₱620  14. Stir-fry Honey Garlic Chicken - ₱580  
\t15. Roasted Duck - ₱990  

🍝 PASTA:  
\t16. Spaghetti Aglio E Olio - ₱520  
\t17. Chicken Spinach Alfredo Pasta - ₱680  
\t18. Pesto Pasta - ₱600  

🔥 HOT DRINKS:  
\t19. Hot Coffee - ₱180\t20. Green Tea - ₱160  

❄️ COLD DRINKS:  
\t21. Iced Coffee - ₱190\t22. Lemon Iced Tea - ₱170  
\t23. Apple Juice - ₱150\t24. Pineapple Juice - ₱180  
\t25. Matcha - ₱200  

(E) - Finish Ordering  
(0) - Return to Main Menu
"""
        console.print(Panel(menu_text, title="🍽 FOOD & DRINKS MENU", border_style="blue"))
    else:
        console.print("❌ Invalid choice, please enter 1 to order or 0 to return!", style="bold red")
        return

    while True:
        order = input("\nEnter item number that you want to order (or 'E' to finish, '0' to go back): ").strip().upper()
        if order == '0':
            return
        elif order == 'E':
            rev_order()
            return
        elif order in menu_options:
            item_name, _ = menu_options[order]
            allorders.append(item_name)
            console.print(f"✅ Added {item_name} to your order!\n", style="bold green")
        else:
            console.print("❌ Invalid choice, please try again!", style="bold red")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main menu function
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

        mmtxt = ['Main Menu\n', '[1] View Menu', '[2] Add to Order', '[3] Review Order', '[4] Finalize Order',
                 '[5] Admin Settings', '[6] Exit']
        for txt in mmtxt:
            print(txt.center(100))

        sel = input("\n\nPlease select an option. ")

        match sel:
            case '1':
                display_menu()
            case '2':
                add_order()
            case '3':
                rev_order()
            case '4':
                print("Order has been finalized. Please wait, printing your receipt!")
                rev_order()
                break
            case '5':
                admin_check()  # integrate function admin_menu() once done, as well as the main menu for admin and its functions
            case '6':
                print("\nThank you for using Python Express! Goodbye. 🐍)
                break
            case _:
                clear_screen()
                print("❌ Invalid choice. Please try again.")
                input("\nPress 0 to return: ")


if __name__ == "__main__":
    main()
