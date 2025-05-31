import configparser
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text


# Load config.ini
config = configparser.ConfigParser()
config.read("config.ini")

# Read DB credentials from the config file
db_user = config.get("DB", "USER")
db_password = config.get("DB", "PASSWORD")
db_name = config.get("DB", "DB_NAME")
db_host = config.get("DB", "DOMAIN")
db_port = config.get("DB", "PORT")

# Build the database URL dynamically
db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":
    try:
        # Try a simple query to test connection
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("✅ Database connection successful:", result.scalar())
    except Exception as e:
        print("❌ Database connection failed:", e)
