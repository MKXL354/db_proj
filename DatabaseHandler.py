import mysql.connector

class DatabaseHandler:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="db_proj"
        )
        self.mycursor = self.mydb.cursor()

    def create_table(self, table_name: str, table_attr: str):
        self.mycursor.execute(f"CREATE TABLE {table_name} ({table_attr})")

    def insert_into_table(self, table_name: str, table_attr: str):
        self.mycursor.execute(f"INSERT INTO {table_name} VALUES ({table_attr})")