import mysql.connector

class DatabaseHandler:
    def __init__(self):
        self.mydb = self.get_connecion()
        self.mycursor = self.mydb.cursor()
        self.init_db()

    def give_value(self):
        self.mydb = self.get_connecion()
        self.mycursor = self.mydb.cursor()

    def get_connecion(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="db_proj"
        )

    def init_db(self):
        with open('init.sql', 'r') as file:
            sql_script = file.read()
        self.mycursor.execute(sql_script, multi=True)

    def create_table(self, table_name: str, table_attr: str):
        self.mycursor.execute(f"CREATE TABLE {table_name} ({table_attr})")

    def insert_into_table(self, table_name: str, table_attr: str):
        self.mycursor.execute(f"INSERT INTO {table_name} VALUES ({table_attr})")