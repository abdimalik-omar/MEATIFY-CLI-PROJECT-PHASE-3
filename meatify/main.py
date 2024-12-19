from sqlalchemy.orm import sessionmaker
from db import get_db_session
from customer_operations import manage_customers
from product_operations import manage_products
from order_operations import manage_orders
from models import Customer, Product, Order

# Define ANSI color codes
RED = '\033[31m'
GREEN = '\033[32m'
CYAN = '\033[36m'
RESET = '\033[0m'
YELLOW = '\033[33m'


def main():
    while True:
        print(f"{CYAN}Main Menu:{RESET}")
        print("1. Manage Customers")
        print("2. Manage Products")
        print("3. Manage Orders")
        print("4. Exit")
        choice = input(f"{YELLOW}Enter your choice:{RESET} ")

        if choice == "1":
            manage_customers()
        elif choice == "2":
            manage_products()
        elif choice == "3":
            manage_orders()
        elif choice == "4":
            print(f"{GREEN}Exiting the system. Goodbye!{RESET}")
            break
        else:
            print(f"{RED}Invalid choice! Please try again.{RESET}")

if __name__ == "__main__":
    main()
