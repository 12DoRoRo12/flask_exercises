import sqlite3
from customer_class import Customer

# conn = sqlite3.connect("customers.db")
conn = sqlite3.connect(":memory:")

c = conn.cursor()

c.execute("""CREATE TABLE customers (
            first text,
            last text,
            gender text,
            email text,
            phone text
            )""")
#3 functions
def insert_customer(cust):
    with conn:
        c.execute("INSERT INTO customers VALUES (:first, :last, :gender, :mail, :phone)",
                  {"first": cust.first, "last": cust.last, "gender": cust.gender, "mail": cust.mail,
                   "phone": cust.phone})

def get_cust_by_name(lastname):
    c.execute("SELECT * FROM customers WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_phone(cust, new_number):
    with conn:
        c.execute("""UPDATE customers SET phone = :phone WHERE first= :first AND last= :last""",
                  {'first': cust.first, 'last': cust.last, 'phone': new_number})

def remove_cust(cust):
    with conn:
        c.execute("DELETE from customers WHERE first = :first AND last = :last",
                  {"first": cust.first, "last": cust.last})





#2
cust_1 = Customer("Eleanor", "Rusvelt", "Female", "e.rusvelt@gmail.com", "111 3454 2356")
cust_2 = Customer("Matheus", "Levis", "Male", "m.levis@gmail.com", "555 3345 2431")
# c.execute("INSERT INTO customers VALUES ('{}', '{}', '{}', '{}', '{}')".format(cust_1.first, cust_1.last, cust_1.gender, cust_1.mail, cust_1.phone))
# c.execute("INSERT INTO customers VALUES (?, ?, ?, ?, ?)", (cust_1.first, cust_1.last, cust_1.gender, cust_1.mail, cust_1.phone))
c.execute("INSERT INTO customers VALUES (:first, :last, :gender, :mail, :phone)", {"first": cust_1.first, "last": cust_1.last, "gender": cust_1.gender, "mail": cust_1.mail, "phone": cust_1.phone})


c.execute("INSERT INTO customers VALUES ('Alexs', 'Rusvelt', 'Male', 'a.bezos@gmail.com', '+995 563987')")

c.execute("SELECT * FROM customers WHERE last='Bezos'")
# c.execute("SELECT * FROM customers WHERE last=?", ('Bezos',))
# c.execute("SELECT * FROM customers WHERE last=:last", {'last': 'Bezos'})

# insert_customer(cust_2)
# print(get_cust_by_name("Levis"))
print(c.fetchall())

conn.commit()
conn.close()

