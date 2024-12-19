from db import get_db_session
from models import Product

RED = '\033[31m'
GREEN = '\033[32m'
CYAN = '\033[36m'
RESET = '\033[0m'
YELLOW = '\033[33m'

def manage_products():
    while True:
        print(f"{CYAN}\nProduct Management Menu:{RESET}")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Back to Main Menu")

        choice = input(f"{YELLOW}Enter your choice:{RESET} ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            update_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            break
        else:
            print(f"{RED}Invalid choice. Please try again.{RESET}")

def add_product():
    name = input("Enter the product name: ")
    product_type = input("Enter the product type: ")
    
    try:
        price = float(input("Enter the product price: "))
    except ValueError:
        print(f"{RED}Invalid price format. Please enter a numeric value.{RESET}")
        return

    session = get_db_session()

    new_product = Product(name=name, product_type=product_type, price=price)
    session.add(new_product)
    session.commit()

    print(f"{GREEN}Product '{name}' added successfully!{RESET}")
    session.close()

def view_products():
    session = get_db_session()

    products = session.query(Product).all()

    if products:
        print("\nList of Products:")
        for product in products:
            print(f"ID: {product.id}, Name: {product.name}, Type: {product.product_type}, Price: {product.price}")
    else:
        print(f"{RED}No products found.{RESET}")

    session.close()

def update_product():
    product_id = input("Enter product ID to update: ")
    name = input("Enter new name: ")
    product_type = input("Enter new type: ")
    price = input("Enter new price: ")

    session = get_db_session()

    product = session.query(Product).filter(Product.id == product_id).first()
    if product:
        product.name = name
        product.product_type = product_type
        product.price = float(price)
        session.commit()
        print(f"{GREEN}Product {product_id} updated successfully!{RESET}")
    else:
        print(f"{RED}Product not found.{RESET}")

    session.close()

def delete_product():
    product_id = input("Enter product ID to delete: ")

    session = get_db_session()
    product = session.query(Product).filter(Product.id == product_id).first()
    if product:
        session.delete(product)
        session.commit()
        print(f"{GREEN}Product {product_id} deleted successfully!{RESET}")
    else:
        print(f"{RED}Product not found.{RESET}")

    session.close()



