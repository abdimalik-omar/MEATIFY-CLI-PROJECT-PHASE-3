# from sqlalchemy import Column, Integer, String, create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# Base = declarative_base()

# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     email = Column(String, nullable=False)

# # Create an engine that stores data in the local SQLite database
# engine = create_engine('sqlite:///butchery.db')

# # Create all tables defined by Base (including User)
# Base.metadata.create_all(engine)

# # Session configuration
# Session = sessionmaker(bind=engine)
# session = Session()
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    contact = Column(String, nullable=False)

    orders = relationship('Order', back_populates='customer')

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    product_type = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    orders = relationship('Order', back_populates='product')

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    
    customer = relationship('Customer', back_populates='orders')
    product = relationship('Product', back_populates='orders')
