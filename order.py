from rich.console import Console
from rich.panel import Panel

console = Console()

menu_options = {
    '1': "☕ Coffee",
    '2': "🍵 Green Tea",
    '3': "🧃 Apple Juice",
    '4': "🍟 Fries",
    '5': "🌮 Nachos",
    '6': "🍿 Popcorn",
    '7': "🍔 Cheese Burger",
    '8': "🍕 Cheese Pizza",
    '9': "🍝 Truffle Pasta",
    '10': "Exit"
}

orders = []

def display_menu():
    menu_text = """
🍹 Drinks
1. Coffee
2. Green Tea
3. Apple Juice

🍟 Snacks
4. Fries
5. Nachos
6. Popcorn

🍽 Mains
7. Cheese Burger
8. Cheese Pizza
9. Truffle Pasta

10. Exit
"""
    console.print(Panel(menu_text, title="🍽 Food & Drinks Menu", border_style="blue", expand=True))

def add_to_order():
    while True:
        display_menu()
        choice = input("Enter the number of your choice (or 10 to finish): ")

        if choice in menu_options:
            if choice == '10':
                break
            else:
                orders.append(menu_options[choice])
                console.print(f"Added {menu_options[choice]} to your order!✅\n")
        else:
            console.print("Invalid choice, please try again!")