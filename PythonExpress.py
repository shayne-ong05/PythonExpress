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
                
                order.display_menu()
                input("\nPress Enter to return to the main menu...")
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