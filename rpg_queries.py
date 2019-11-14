import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
cur = conn.cursor()

cur.execute('SELECT * FROM charactercreator_character')
cur.fetchall()
cur.execute('SELECT * FROM charactercreator_cleric')
cur.fetchall()
cur.execute('SELECT * FROM charactercreator_fighter')
cur.fetchall()
cur.execute('SELECT * FROM charactercreator_mage')
cur.fetchall()
cur.execute('SELECT * FROM charactercreator_necromancer')
cur.fetchall()
cur.execute('SELECT * FROM charactercreator_thief')
cur.fetchall()
cur.execute('SELECT * FROM armory_item')
cur.fetchall()
cur.execute('SELECT * FROM armory_weapon')
cur.fetchall()
cur.execute('SELECT * FROM charactercreator_character_inventory LIMIT 20')
cur.fetchall()
query = """
SELECT * FROM charactercreator_character_inventory  WHERE id IN (
SELECT item_ptr_id FROM armory_weapon
) LIMIT 20
"""
cur.execute(query)
cur.fetchall()
query = """
SELECT AVG(c) 
FROM
(
   SELECT COUNT(*) c 
   FROM charactercreator_character_inventory 
   GROUP BY character_id
)
"""
cur.execute(query)
cur.fetchall()
query = """
SELECT AVG(c) 
FROM
(
   SELECT COUNT(*) c 
   FROM charactercreator_character_inventory 
   WHERE id IN (
	SELECT item_ptr_id 
	FROM armory_weapon
)
   GROUP BY character_id
)
"""
cur.execute()
cur.fetchall()
