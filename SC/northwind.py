"""
~~~~~~output~~~~~~~~~

[(263.5,), (123.79,), (97,), (81,), (62.5,), (55,), (53,), (49.3,), (46,), (45.6,)]
31.22222222222217
[(263.5, 'Aux joyeux ecclésiastiques'), (123.79, 'Plutzer Lebensmittelgroßmärkte AG'), (97, 'Tokyo Traders'), (81, 'Specialty Biscuits, Ltd.'), (62.5, 'Pavlova, Ltd.'), (55, 'Gai pâturage'), (53, "G'day, Mate"), (49.3, "Forêts d'érables"), (46, 'Leka Trading'), (45.6, 'Plutzer Lebensmittelgroßmärkte AG')]
[('Beverages', 1)]

"""

import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
c = conn.cursor()

query = """
SELECT UnitPrice
FROM Product
ORDER BY UnitPrice
DESC
LIMIT 10;
"""

print(c.execute(query).fetchall())

query = """
SELECT AVG(BirthDate)
FROM Employee;
"""

print(2019 - (c.execute(query).fetchall()[0][0]))

query = """
SELECT UnitPrice, CompanyName
FROM Product
INNER JOIN Supplier
ON Product.SupplierID = Supplier.ID
ORDER BY UnitPrice
DESC
LIMIT 10;
"""

print(c.execute(query).fetchall())

query = """
SELECT CategoryName, COUNT(DISTINCT c.Id)
FROM Category c
INNER JOIN Product p
ON c.ID = p.CategoryId
GROUP BY CategoryName
ORDER BY COUNT(DISTINCT c.Id)
DESC
LIMIT 1;
"""

# this one doesn't work, not sure what I did wrong
print(c.execute(query).fetchall())

# print(c.execute('SELECT sql FROM sqlite_master WHERE name="Supplier";').fetchall())