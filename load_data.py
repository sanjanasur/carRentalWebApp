import csv
import mysql.connector


def load_data_from_csv(file_path, table_name, conn):
    try:
        cursor = conn.cursor()
        with open(file_path, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)
            batch_size = 50
            rows = []
            for row in reader:

                row = [None if value == '' else value for value in row]
                rows.append(row)
                if len(rows) >= batch_size:
                    cursor.executemany(
                        f"INSERT INTO {table_name} VALUES ({','.join(['%s']*len(row))})",
                        rows
                    )
                    rows = []
            if rows:
                cursor.executemany(
                    f"INSERT INTO {table_name} VALUES ({','.join(['%s']*len(row))})",
                    rows
                )
        conn.commit()
        print(f"Data from {file_path} loaded into {table_name} successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error loading data into {table_name}: {e}")
    finally:
        cursor.close()

def main():

    user = 'xxx'
    password = 'xxx'
    host = 'xxx'
    database = 'xxx'


    conn = mysql.connector.connect(
        user=user, password=password, host=host, database=database
    )

    try:
        load_data_from_csv('RENTS.csv', 'RENTS', conn)
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    main()
