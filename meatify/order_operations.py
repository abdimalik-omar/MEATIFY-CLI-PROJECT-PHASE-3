from db import get_db_session
from models import Order, Product, Customer

RED = '\033[31m'
GREEN = '\033[32m'
CYAN = '\033[36m'
RESET = '\033[0m'
YELLOW = '\033[33m'

def add_order():
    customer_id = input("Enter customer ID: ")
    product_id = input("Enter product ID: ")
    quantity = int(input("Enter quantity: "))

    session = get_db_session()

    order = Order(customer_id=customer_id, product_id=product_id, quantity=quantity)
    session.add(order)
    session.commit()

    print(f"{GREEN}Order added successfully!{RESET}")
    session.close()

def view_orders():
    session = get_db_session()

    orders = session.query(Order).all()

    if orders:
        for order in orders:
            print(f"Order ID: {order.id}, Customer ID: {order.customer_id}, Product ID: {order.product_id}, Quantity: {order.quantity}")
    else:
        print(f"{RED}No orders found.{RESET}")

    session.close()

def update_order():
    order_id = input("Enter order ID to update: ")
    product_id = input("Enter new product ID: ")
    quantity = int(input("Enter new quantity: "))

    session = get_db_session()

    order = session.query(Order).filter(Order.id == order_id).first()
    if order:
        order.product_id = product_id
        order.quantity = quantity
        session.commit()
        print(f"{GREEN}Order {order_id} updated successfully!{RESET}")
    else:
        print(f"{RED}Order not found.{RESET}")

    session.close()

def delete_order():
    order_id = input("Enter order ID to delete: ")

    session = get_db_session()

    order = session.query(Order).filter(Order.id == order_id).first()
    if order:
        session.delete(order)
        session.commit()
        print(f"{GREEN}Order {order_id} deleted successfully!{RESET}")
    else:
        print(f"{RED}Order not found.{RESET}")

    session.close()

def manage_orders():
    while True:
        print(f"{CYAN}\nOrder Management Menu:{RESET}")
        print("1. Add Order")
        print("2. View Orders")
        print("3. Update Order")
        print("4. Delete Order")
        print("5. Back to Main Menu")

        choice = input(f"{YELLOW}Enter your choice:{RESET}")

        if choice == "1":
            add_order()
        elif choice == "2":
            view_orders()
        elif choice == "3":
            update_order()
        elif choice == "4":
            delete_order()
        elif choice == "5":
            break
        else:
            print(f"{RED}Invalid choice. Please try again.{RESET}")
