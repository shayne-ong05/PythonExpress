from rich.console import Console
from rich.panel import Panel

console = Console()

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

    console.print(Panel(menu_text, title="🍽Food & Drinks Menu", border_style="blue", expand=True))

    options = {
        '1': "☕ Coffee",
        '2': "🍵 Green Tea",
        '3': "🧃 Apple Juice",
        '4': "🍟 Fries",
        '5': "🌮 Nachos",
        '6': "🍿 Popcorn",
        '7': "🍔 Burger",
        '8': "🍕 Pizza",
        '9': "🍝 Pasta",
        '10': "Exiting..."
    }
display_menu()