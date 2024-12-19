from db import get_db_session
from models import Customer

RED = '\033[31m'
GREEN = '\033[32m'
CYAN = '\033[36m'
RESET = '\033[0m'
YELLOW = '\033[33m'

# Add a new customer
def add_customer():
    name = input("Enter the customer's name: ")
    email = input("Enter the customer's email: ")
    contact = input("Enter the customer's contact: ")

    session = get_db_session()
    new_customer = Customer(name=name, email=email, contact=contact)
    
    session.add(new_customer)
    session.commit()
    session.close()

    print(f"{GREEN}Customer {name} added successfully!{RESET}")

# View all customers
def view_customers():
    session = get_db_session()
    customers = session.query(Customer).all()

    if customers:
        for customer in customers:
            print(f"ID: {customer.id}, Name: {customer.name}, Email: {customer.email}, Contact: {customer.contact}")
    else:
        print(f"{RED}No customers found.{RESET}")

    session.close()

# Update customer details
def update_customer():
    customer_id = input("Enter customer ID to update: ")
    name = input("Enter new name: ")
    email = input("Enter new email: ")
    contact = input("Enter new contact: ")

    session = get_db_session()
    customer = session.query(Customer).filter(Customer.id == customer_id).first()

    if customer:
        customer.name = name
        customer.email = email
        customer.contact = contact
        session.commit()
        print(f"{GREEN} {customer_id} updated successfully!{RESET}")
    else:
        print(f"{RED}Customer with ID {customer_id} not found.{RESET}")
    
    session.close()

# Delete a customer
def delete_customer():
    customer_id = input("Enter customer ID to delete: ")

    session = get_db_session()
    customer = session.query(Customer).filter(Customer.id == customer_id).first()

    if customer:
        session.delete(customer)
        session.commit()
        print(f"{GREEN}Customer {customer_id} deleted successfully!{RESET}")
    else:
        print(f"{RED}Customer with ID {customer_id} not found.{RESET}")
    
    session.close()

# Manage customers
def manage_customers():
    while True:
        print(f"{CYAN}\nCustomer Management Menu:{RESET}")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Update Customer")
        print("4. Delete Customer")
        print("5. Back to Main Menu")

        choice = input(f"{YELLOW} your choice:{RESET} ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            view_customers()
        elif choice == "3":
            update_customer()
        elif choice == "4":
            delete_customer()
        elif choice == "5":
            break
        else:
            print(f"{RED}Invalid choice. Please try again.{RESET}")
