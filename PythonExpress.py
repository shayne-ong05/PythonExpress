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
from random import randint
from datetime import datetime
import re

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

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def display_menu():
    menu_text = (
         "[bold yellow]🥪 SNACKS:[/bold yellow]\n"
    "\t[bold bright_green]1.[/bold bright_green]  {0:<20}  [bold yellow]{25}[/bold yellow]\n"
    "\t[bold bright_green]2.[/bold bright_green]  {1:<20}  [bold yellow]{26}[/bold yellow]\n"
    "\t[bold bright_green]3.[/bold bright_green]  {2:<20}  [bold yellow]{27}[/bold yellow]\n"
    "\t[bold bright_green]4.[/bold bright_green]  {3:<20}  [bold yellow]{28}[/bold yellow]\n"
    "\t[bold bright_green]5.[/bold bright_green]  {4:<20}  [bold yellow]{29}[/bold yellow]\n"
    "\t[bold bright_green]6.[/bold bright_green]  {5:<20}  [bold yellow]{30}[/bold yellow]\n\n"

    "[bold cyan]🐟 SEAFOOD:[/bold cyan]\n"
    "\t[bold bright_green]7.[/bold bright_green]  {6:<20}  [bold yellow]{31}[/bold yellow]\n"
    "\t[bold bright_green]8.[/bold bright_green]  {7:<20}  [bold yellow]{32}[/bold yellow]\n\n"

    "[bold red]🥩 BEEF:[/bold red]\n"
    "\t[bold bright_green]9.[/bold bright_green]  {8:<20}  [bold yellow]{33}[/bold yellow]\n"
    "\t[bold bright_green]10.[/bold bright_green] {9:<20}  [bold yellow]{34}[/bold yellow]\n\n"

    "[bold magenta]🐖 PORK:[/bold magenta]\n"
    "\t[bold bright_green]11.[/bold bright_green] {10:<20}  [bold yellow]{35}[/bold yellow]\n"
    "\t[bold bright_green]12.[/bold bright_green] {11:<20}  [bold yellow]{36}[/bold yellow]\n\n"

    "[bold orange]🍗 CHICKEN:[/bold orange]\n"
    "\t[bold bright_green]13.[/bold bright_green] {12:<20}  [bold yellow]{37}[/bold yellow]\n"
    "\t[bold bright_green]14.[/bold bright_green] {13:<20}  [bold yellow]{38}[/bold yellow]\n"
    "\t[bold bright_green]15.[/bold bright_green] {14:<20}  [bold yellow]{39}[/bold yellow]\n\n"

    "[bold green]🍝 PASTA:[/bold green]\n"
    "\t[bold bright_green]16.[/bold bright_green] {15:<20}  [bold yellow]{40}[/bold yellow]\n"
    "\t[bold bright_green]17.[/bold bright_green] {16:<20}  [bold yellow]{41}[/bold yellow]\n"
    "\t[bold bright_green]18.[/bold bright_green] {17:<20}  [bold yellow]{42}[/bold yellow]\n\n"

    "[bold red]🔥 HOT DRINKS:[/bold red]\n"
    "\t[bold bright_green]19.[/bold bright_green] {18:<20}  [bold yellow]{43}[/bold yellow]\n"
    "\t[bold bright_green]20.[/bold bright_green] {19:<20}  [bold yellow]{44}[/bold yellow]\n\n"

    "[bold blue]❄️ COLD DRINKS:[/bold blue]\n"
    "\t[bold bright_green]21.[/bold bright_green] {20:<20}  [bold yellow]{45}[/bold yellow]\n"
    "\t[bold bright_green]22.[/bold bright_green] {21:<20}  [bold yellow]{46}[/bold yellow]\n"
    "\t[bold bright_green]23.[/bold bright_green] {22:<20}  [bold yellow]{47}[/bold yellow]\n"
    "\t[bold bright_green]24.[/bold bright_green] {23:<20}  [bold yellow]{48}[/bold yellow]\n"
    "\t[bold bright_green]25.[/bold bright_green] {24:<20}  [bold yellow]{49}[/bold yellow]\n"

    ).format(*[menu_options[str(i)][0] for i in range(1, 26)], *[menu_options[str(i)][1] for i in range(1, 26)])

    console.print(Panel(menu_text, title="🍽 FOOD & DRINKS MENU 🍽", border_style="green", width = 100))
    console.print("\nPress [bold bright_green]0[/bold bright_green] to return: ")
    input()

allorders = {}

def add_to_order():
    console.print("\n🛒 Are you ready to place an order?", style="bold yellow")
    console.print("Press [1] to start ordering")
    console.print("Press [0] to return to the Main Menu")

    choice = input("\nYour choice: ").strip()

    if choice == '0':
        return
    elif choice == '1':
        menu_text = (
            "[bold yellow]🥪 SNACKS:[/bold yellow]\n"
            "\t[bold bright_green]1.[/bold bright_green]  {0:<20}  [bold yellow]{25}[/bold yellow]\n"
            "\t[bold bright_green]2.[/bold bright_green]  {1:<20}  [bold yellow]{26}[/bold yellow]\n"
            "\t[bold bright_green]3.[/bold bright_green]  {2:<20}  [bold yellow]{27}[/bold yellow]\n"
            "\t[bold bright_green]4.[/bold bright_green]  {3:<20}  [bold yellow]{28}[/bold yellow]\n"
            "\t[bold bright_green]5.[/bold bright_green]  {4:<20}  [bold yellow]{29}[/bold yellow]\n"
            "\t[bold bright_green]6.[/bold bright_green]  {5:<20}  [bold yellow]{30}[/bold yellow]\n\n"

            "[bold cyan]🐟 SEAFOOD:[/bold cyan]\n"
            "\t[bold bright_green]7.[/bold bright_green]  {6:<20}  [bold yellow]{31}[/bold yellow]\n"
            "\t[bold bright_green]8.[/bold bright_green]  {7:<20}  [bold yellow]{32}[/bold yellow]\n\n"

            "[bold red]🥩 BEEF:[/bold red]\n"
            "\t[bold bright_green]9.[/bold bright_green]  {8:<20}  [bold yellow]{33}[/bold yellow]\n"
            "\t[bold bright_green]10.[/bold bright_green] {9:<20}  [bold yellow]{34}[/bold yellow]\n\n"

            "[bold magenta]🐖 PORK:[/bold magenta]\n"
            "\t[bold bright_green]11.[/bold bright_green] {10:<20}  [bold yellow]{35}[/bold yellow]\n"
            "\t[bold bright_green]12.[/bold bright_green] {11:<20}  [bold yellow]{36}[/bold yellow]\n\n"

            "[bold orange]🍗 CHICKEN:[/bold orange]\n"
            "\t[bold bright_green]13.[/bold bright_green] {12:<20}  [bold yellow]{37}[/bold yellow]\n"
            "\t[bold bright_green]14.[/bold bright_green] {13:<20}  [bold yellow]{38}[/bold yellow]\n"
            "\t[bold bright_green]15.[/bold bright_green] {14:<20}  [bold yellow]{39}[/bold yellow]\n\n"

            "[bold green]🍝 PASTA:[/bold green]\n"
            "\t[bold bright_green]16.[/bold bright_green] {15:<20}  [bold yellow]{40}[/bold yellow]\n"
            "\t[bold bright_green]17.[/bold bright_green] {16:<20}  [bold yellow]{41}[/bold yellow]\n"
            "\t[bold bright_green]18.[/bold bright_green] {17:<20}  [bold yellow]{42}[/bold yellow]\n\n"

            "[bold red]🔥 HOT DRINKS:[/bold red]\n"
            "\t[bold bright_green]19.[/bold bright_green] {18:<20}  [bold yellow]{43}[/bold yellow]\n"
            "\t[bold bright_green]20.[/bold bright_green] {19:<20}  [bold yellow]{44}[/bold yellow]\n\n"

            "[bold blue]❄️ COLD DRINKS:[/bold blue]\n"
            "\t[bold bright_green]21.[/bold bright_green] {20:<20}  [bold yellow]{45}[/bold yellow]\n"
            "\t[bold bright_green]22.[/bold bright_green] {21:<20}  [bold yellow]{46}[/bold yellow]\n"
            "\t[bold bright_green]23.[/bold bright_green] {22:<20}  [bold yellow]{47}[/bold yellow]\n"
            "\t[bold bright_green]24.[/bold bright_green] {23:<20}  [bold yellow]{48}[/bold yellow]\n"
            "\t[bold bright_green]25.[/bold bright_green] {24:<20}  [bold yellow]{49}[/bold yellow]\n"

        ).format(*[menu_options[str(i)][0] for i in range(1, 26)], *[menu_options[str(i)][1] for i in range(1, 26)])

        console.print(Panel(menu_text, title="🍽 FOOD & DRINKS MENU 🍽", border_style="green", width=100))
    else:
        console.print("❌ Invalid choice! Please enter 1 to order or 0 to return!", style="bold red")
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
            if item_name in allorders:
                allorders[item_name] += 1
            else:
                allorders[item_name] = 1
            console.print(f"✅ Added {item_name} (x{allorders[item_name]}) to your order!", style="bold green")
        else:
            console.print("❌ Invalid choice, please try again!", style="bold red")

def rev_order():
    clear_screen()
    while True:
        console.print("\t🛒 Order Review 🐍", style="bold yellow")
        console.print("-" * 50 + "\n")

        if not allorders:
            console.print("🗑️Your order is currently empty.", style="bold red")
        else:
            console.print("🛒Your Current Order:\n", style="bold cyan")

            total_cost = 0
            for item, quantity in allorders.items():
                item_price = int(item.split(" - ₱")[1])
                total_cost += item_price * quantity
                console.print(f"{item} x{quantity}", style="bold green")

            console.print(f"\n💰 Total Cost: ₱{total_cost:,}", style="bold magenta")

        console.print("\nOptions:", style="bold blue")
        console.print("[1] Remove an item ❌")
        console.print("[2] Add more items 🔍")
        console.print("[3] Finalize order 💾")
        console.print("[0] Return to main menu ⌨")

        choice = input("\nYour choice: ").strip()

        if choice == '1':
            remove_item_from_order()
        elif choice == '2':
            add_to_order()
        elif choice == '3':
            amount = payment()
            change = amount - total_cost
            console.print("\n✅ Order has been finalized. Please wait, printing your receipt!", style="bold green")
            try:
                current_time = datetime.now().strftime("%m/%d/%Y %H:%M")
                with open('receipt.txt', 'w', encoding="utf-8") as file:
                    qty_width = 5
                    item_width = 19
                    price_width = 15
                    amount_width = 9
                    
                    file.write("=" * 50 + "\n")
                    file.write("Python Express".center(50))
                    file.write(f"\n\n{current_time}")
                    file.write("\n" + "=" * 50 + "\n")
                    file.write("SALE INVOICE".center(50))
                    file.write("\n" + "=" * 50 + "\n")
                    file.write(f"{'QTY'.ljust(qty_width)}{'Items'.ljust(item_width)}{'Item Price'.rjust(price_width)}{'Amount'.rjust(amount_width)}")
                    file.write("\n" + "=" * 50 + "\n")

                    for item, quantity in allorders.items():
                        item_price = int(item.split("₱")[1])
                        itemdisplay = item.split(" - ₱")[0].strip()
                        file.write(f"{str(quantity).ljust(qty_width)}{itemdisplay.ljust(item_width)}₱{str(item_price).rjust(price_width - 1)}₱{str(item_price * quantity).rjust(amount_width - 1)}\n")

                    file.write("=" * 50 + "\n")
                    file.write(f"TOTAL AMOUNT: ₱{total_cost:,}\n")
                    file.write("=" * 50 + "\n")
                    file.write(f"Amount ₱ {amount}")
                    file.write(f"\n\nChange ₱ {change}")

                console.print("\n✅ Receipt has been saved as 'receipt.txt'.", style="bold green")
                allorders.clear()
            except IOError:
                print("INVALID! Please pick again") 
            console.print("\n𓆙" + "." * 20)
            digits = randint(1000,9999)
            console.print(f"\nPlease present the number {digits} to the cashier!")
            input("\nPress Enter to return to the main menu...")
            return
        elif choice == '0':
            return
        else:
            console.print("❌ Invalid choice, please try again!", style="bold red")

def remove_item_from_order():
    clear_screen()
    if not allorders:
        console.print("Your order is empty!❎", style="bold red")
        input("\nPress Enter to return...")
        return

    console.print("\t🗑 Remove an Item🗑️", style="bold yellow")
    console.print("-" * 50)

    for position, item in enumerate(allorders, start=1):
        console.print(f"{position}. {item}", style="bold red")

    try:
        item_number = int(input("\nEnter the number of the item to remove (or 0 to cancel): ").strip())
        if item_number == 0:
            return
        elif 1 <= item_number <= len(allorders):
            removed_item = allorders.pop(item_number - 1)
            console.print(f"✅ Removed {removed_item} from your order!", style="bold green")
        else:
            console.print("❌ Invalid number, please try again!", style="bold red")
    except ValueError:
        console.print("❌ Invalid input, please enter a number!", style="bold red")

    input("\nPress Enter to continue...")
    clear_screen()

    input("\nPress Enter to return to the main menu...")
    clear_screen()

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
    if not allorders:
        print("No orders have been placed yet.")
    else:
        print("All Orders:")
        for order in allorders:
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
    allorders.clear()
    print("All orders have been reset.")

def payment():
    total_amount = sum(int(item.split(" - ₱")[1]) * qty for item, qty in allorders.items())

    while True:
        print("How do you wish to pay? Please pick a payment option:")
        print("[1] Credit Card")
        print("[2] G-Cash")
        
        Pchoice = input("Choice: ").strip()

        if Pchoice == '1':
            card_number = input("Please enter your credit card number (16 digits): ").strip()
            if not re.fullmatch(r"\d{16}", card_number):
                print("Invalid credit card number. Please enter exactly 16 digits.")
                continue

            while True:
                try:
                    amount = float(input(f"Please enter payment amount (Total: ₱{total_amount:,}): "))
                    if amount < total_amount:
                        print("❌ Not enough funds. Enter a higher amount.")
                    else:
                        change = amount - total_amount
                        print(f"✅ Payment of ₱{amount:,} processed using card ending in {card_number[-4:]}.")
                        if change > 0:
                            print(f"💰 Change: ₱{change:,}")
                        return amount
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")

        elif Pchoice == '2':
            gcash_number = input("Enter your G-Cash number (11 digits): ").strip()
            if not re.fullmatch(r"\d{11}", gcash_number):
                print("❌ Invalid G-Cash number. Enter a valid 11-digit number.")
                continue

            while True:
                try:
                    amount = float(input(f"Enter payment amount (Total: ₱{total_amount:,}): "))
                    if amount < total_amount:
                        print("❌ Not enough funds. Enter a higher amount.")
                    else:
                        change = amount - total_amount
                        print(f"✅ Payment of ₱{amount:,} processed via G-Cash ({gcash_number}).")
                        if change > 0:
                            print(f"💰 Change: ₱{change:,}")
                        return amount
                except ValueError:
                    print("❌ Invalid amount. Enter a valid number.")

        else:
            print("❌ Invalid choice. Please pick 1 or 2.")
    


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

def main():
    # Main Menu Screen
    clear_screen()
    while True:

        console.print(Align("🐍 Welcome to Python Express, where we move at slithering speeds to make your order! 🐉", align = "center", style = "bold bright_yellow"))
        console.print(Align("-" * 100,align="center", style = "bold white"))

        mmtxt = [
            ("🗂️ Main Menu 🗂️", "bold bright_cyan"),
            ("[1] View Food Menu ⓘ", "bold yellow"),
            ("[2] Add to Order 📝", "bold cyan"),
            ("[3] Review Order 🔎", "bold blue"),
            ("[4] Finalize Order 📋", "bold green"),
            ("[5] Admin Settings ⚙️", "bold white"),
            ("[6] Exit 🖐", "bold red")
        ]
        for text, style in mmtxt:
            console.print(Align(text, style=style, align="center"))

        sel = 0
        sel = input("\n\nPlease select an option: ")

        match sel:
            case '1':
                clear_screen()
                display_menu()
                input("\nPress Enter to return to the main menu...")
                clear_screen()
            case '2':
                add_to_order()
            case '3':
                rev_order()
            case '4':
                if not allorders:  # Check if the order list is empty
                    console.print("\n❌ Cannot finalize order! No items have been added.", style="bold red")
                    input("\nPress Enter to return to the main menu...")
                    clear_screen()
                else:
                    console.print("Order has been finalized. Please wait, printing your receipt!\n𓆙" + "." * 30, style="bold yellow")
                    rev_order()
                    break
            case '5':
                admin_check()  # integrate function admin_menu() once done, as well as the main menu for admin and its functions
            case '6':
                console.print(Align("Thank you for using Python Express!\n😃 Goodbye and Stay Safe! 😃", style = "bold bright_green", align = "center"))
                break
            case _:
                clear_screen()
                console.print("Invalid choice. Please try again.🙂", style = "red")


if __name__ == "__main__":
    main()
