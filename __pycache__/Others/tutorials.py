import  pyodbc

def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("select * from tbl_customers")
    for row in cursor:
        print(f'row = {row}')
    print()

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-A5P1CUL\HAMEEDSQLSERVER;"
    "Database=tutorial;"
    "Trusted_Connection=yes;"
)

read(conn)
#create(conn)