from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an engine that stores data in the local SQLite database
engine = create_engine('sqlite:///butchery.db')




# Session configuration
Session = sessionmaker(bind=engine)

def get_db_session():
    return Session()