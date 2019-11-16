import psycopg2
import pandas as pd

host = 'salt.db.elephantsql.com'
user = 'acnpuhxb'
database = 'acnpuhxb'
password = 'O2E1QUU8yL1d2PjrQ8XYCwwWI-vDMK3M'
pg_conn = psycopg2.connect(
    database=database, user=user, password=password, host=host)
pg_cur = pg_conn.cursor()

create_titanic_table = """
CREATE TYPE Sex AS ENUM('male', 'female');

CREATE TABLE Titanic(
    Survived bit NOT NULL,
    Pclass int NOT NULL,
    Name VARCHAR(50) PRIMARY KEY,
    Sex Sex NOT NULL,
    Age int NOT NULL,
    Siblings_Spouses_aboard int NOT NULL,
    Parents_children_aboard int NOT NULL,
    Fare int NOT NULL
);
"""

pg_cur.execute(create_titanic_table)
pg_conn.commit()

df = pd.read_csv('titanic.csv')
df = df.set_index('Name', verify_integrity=True)
df.to_sql('Titanic', pg_conn)
