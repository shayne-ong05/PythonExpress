from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()

# Welcome text
welcome_text = """
Welcome to Python Express!
Each item is assigned to a number. Simply type the number of the item 
of your choice and it will be added to your cart.
"""

menu_options = {

    '1': ("French Fries - ₱250", "snack"),
    '2': ("Onion Rings - ₱270", "snack"),
    '3': ("Mozzarella Sticks - ₱290", "snack"),
    '4': ("Quesadillas - ₱300", "snack"),
    '5': ("Nachos with Cheese - ₱280", "snack"),
    '6': ("Caesar Salad - ₱260", "snack"),

    '7': ("Fish & Chips - ₱550", "main"),
    '8': ("Grilled Shrimp Skewers - ₱750", "main"),

    '9': ("Beef Broccoli - ₱600", "main"),
    '10': ("Beef Tenderloin - ₱950", "main"),

    '11': ("Grilled Pork Steak - ₱650", "main"),
    '12': ("Baby Back Ribs - ₱900", "main"),

    '13': ("Chicken Parmesan - ₱620", "main"),
    '14': ("Stir-fry Honey Garlic Chicken - ₱580", "main"),
    '15': ("Roasted Duck - ₱990", "main"),

    '16': ("Spaghetti Aglio E Olio - ₱520", "main"),
    '17': ("Chicken Spinach Alfredo Pasta - ₱680", "main"),
    '18': ("Pesto Pasta - ₱600", "main"),

    '19': ("Hot Coffee - ₱180", "drink"),
    '20': ("Green Tea - ₱160", "drink"),

    '21': ("Iced Coffee - ₱190", "drink"),
    '22': ("Lemon Iced Tea - ₱170", "drink"),
    '23': ("Apple Juice - ₱150", "drink"),
    '24': ("Pineapple Juice - ₱180", "drink"),
    '25': ("Matcha - ₱200", "drink"),

    'E': ("Exit", "exit")
}

orders = []

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
