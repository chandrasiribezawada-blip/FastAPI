from app.database import engine
from sqlalchemy import text


try:

    with engine.connect() as connection:

        connection.execute(text("SELECT 1"))

    print("Database connected successfully!")


except Exception as e:

    print("Database connection failed!")
    print("Error:", e)