def display_menu(menu):
    print("\n=*=*=*=*=* FAST FOOD MENU *=*=*=*=*=")

    for item, price in menu.items():
        print(f"{item:<25} ₱{price:.2f}")

    print("====**==========**===========**=====")


    
def display_receipt(orders, menu):
    total_order = 0

    print("\n=*==========*= RECEIPT =*==========*=")
    print(f"{'MENU ITEM':<25} {'QTY':<5} {'PRICE':<10} {'TOTAL':<10}")
    print("-------------------------------------")

    for item, quantity in orders.items():
        price = menu[item]
        item_total = price * quantity
        total_order += item_total

        print(f"{item:<25} {quantity:<5} "
              f"₱{price:<9.2f} ₱{item_total:<9.2f}")

    print("-------------------------------------")
    print(f"{'TOTAL ORDER':<25} {'':<5} {'':<10} ₱{total_order:.2f}")
    print("===========***************===========")



def get_order(menu):
    orders = {}

    while True:
        item_name = input("\nEnter menu item: ")

        if item_name in menu:
            quantity = int(input("Enter quantity: "))

            if item_name in orders:
                orders[item_name] += quantity
            else:
                orders[item_name] = quantity

            print(f"{quantity} x {item_name} added to your order.")

            another_order = input(
                "Do you want to order another item? (yes/no): "
            ).lower()

            if another_order == "no":
                break

        else:
            print("Sorry, that item is not on the menu.")
            print("Please choose an item from the menu.")

    return orders



def main():


    menu = {
        "Burger": 49.00,
        "Cheeseburger": 179.00,
        "Chicken": 129.00,
        "French Fries": 59.00,
        "Spaghetti": 99.00,
        "Chicken Sandwich": 119.00,
        "Soft Drink": 25.00,
        "Ice Cream": 35.00
    }


    display_menu(menu)


    wants_to_order = input(
        "\nDo you want to place an order? (yes/no): "
    ).lower()

    if wants_to_order == "yes":


        orders = get_order(menu)


        display_receipt(orders, menu)

        print("\nThank you for ordering!")
        print("Please come again!")

    else:
        print("\nThank you! Have a nice day!")



main()