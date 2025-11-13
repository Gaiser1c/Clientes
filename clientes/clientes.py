import psycopg2
import os
from dotenv import load_dotenv

# Loads environment variables of .env file
load_dotenv()

# Custumer registration funcion
def custumer_record(connection):
    # cursor
    with connection.cursor() as cursor:

        # Variables
        while True:
            # DDD validation
            ddd = input("DDD: ")
            if ddd.isdigit() and len(ddd) == 2:
                break
            print("DDD inválido! Tente novamente.")

        while True:
            # Number validation
            number = input("Número: ")
            if number.isdigit() and 8 <= len(number) <= 9:
                break
            print("Número inválido! Tente novamente.")

        phone = ddd + number 

        name = input("Nome: ").strip().title()

        values = (name, phone)

        # SQL commands
        sql = "INSERT INTO clientes (name, phone) VALUES (%s, %s)"

        # Execute and confirm the SQL command
        cursor.execute(sql, values)
        connection.commit()

        print(f"Cliente '{name}' cadastrado com sucesso!")

# Main
 
try:
    # Server information and connection
    with psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        sslmode=os.getenv("DB_SSLMODE") 
    )as connection:
        print("Conexão bem sucedida!")

        costumer_record(connection)


except psycopg2.OperationalError as e:
    print("Erro na conexão com o banco de dados", e)

except psycopg2.Error as e:
    print("Erro ao executar o comando SQL!", e)