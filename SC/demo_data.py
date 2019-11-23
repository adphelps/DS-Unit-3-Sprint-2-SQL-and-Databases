"""
~~~~~~~~~~~~output~~~~~~~~~~~~~~~

[(3,)]
[(2,)]
[(2,)]

"""


import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
c = conn.cursor()

query = """
CREATE TABLE demo(
    [s] text,
    [x] INTEGER,
    [y] INTEGER
)
"""

c.execute(query)

query = """
INSERT INTO demo(s, x, y)
VALUES
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7);
"""

c.execute(query)
conn.commit()

query = """
SELECT COUNT(*)
FROM demo;
"""

print(c.execute(query).fetchall())

query = """
SELECT COUNT(*)
FROM demo
WHERE x >=5
AND y>=5;
"""

print(c.execute(query).fetchall())

query = """
SELECT COUNT(
    DISTINCT y
)
FROM demo;
"""

print(c.execute(query).fetchall())