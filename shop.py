class InsufficientFundsError(Exception):
    pass

class MaximumPurchaseAttemptsReached(Exception):
    pass

def shop_simulation():
    items = {
        'item1': 50,
        'item2': 75,
        'item3': 150
    }

    customer_balance = 100
    purchase_attempts = 0

    try:
        print("Welcome to the Shop!")
        print("Items available for purchase:")
        for item, price in items.items():
            print(f"{item}: £{price}")

        while True:
            option = input("Enter the item you would like to purchase (or 'exit' to leave): ")

            if option == 'exit':
                print("Thank you for visiting the shop. Goodbye!")
                break

            try:
                if option not in items:
                    raise ValueError("Invalid item selected!")

                item_price = items[option]

                if item_price > customer_balance:
                    raise InsufficientFundsError("Insufficient funds to purchase this item.")

                customer_balance -= item_price
                print(f"Here's your {option}!")

                if customer_balance <= 0:
                    print("You have no more money left.")
                    break

            except ValueError as ve:
                print(ve)
                continue

            except InsufficientFundsError as ife:
                print(ife)
                response = input("Do you have more money? (yes/no): ")

                if response.lower() == 'yes':
                    try:
                        additional_money = int(input("Enter the additional amount: "))
                        if additional_money <= 0:
                            raise ValueError("Invalid additional amount entered!")

                        customer_balance += additional_money
                        continue

                    except ValueError as ve:
                        print(ve)
                        continue

                else:
                    print("You don't have enough money to continue shopping.")
                    break

            finally:
                purchase_attempts += 1

                if purchase_attempts >= 3:
                    raise MaximumPurchaseAttemptsReached("Maximum purchase attempts reached. Exiting the shop.")

    except MaximumPurchaseAttemptsReached as mpar:
        print(mpar)

shop_simulation()
