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

def display_menu():
    # Centered welcome text
    welcome = Align.center(welcome_text)

    # Construct the menu with prices
    menu_text = f"""
Welcome to Python Express!
Each item is assigned to a number. Simply type the number of the item 
of your choice and it will automatically be added to your cart.

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

(E) - Exit
"""
    console.print(Panel(menu_text, title="🍽 FOOD & DRINKS MENU", border_style="blue"))

def add_to_order():
    while True:
        display_menu()
        order = input("Enter the number of your choice (or 'E' to finish): ").strip().upper()

        if order in menu_options:
            if order == 'E':
                console.print("\nThank you for ordering! Here’s your order summary:")
                console.print(Panel("\n".join(allorders), title="Your Order", border_style="green"))
                break
            else:
                item_name, category = menu_options[order]
                allorders.append(item_name)
                console.print(f"Added {item_name} to your order!\n")
        else:
            console.print("Invalid choice, please try again!")

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
    
        sel = input("\n\nPlease select an option. ")
    
        match sel:
            case '1':
                display_menu()
            case '2':
                add_to_order()
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
