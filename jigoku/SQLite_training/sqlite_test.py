import sqlite3
import random

dbname = 'sample.db'

conn = sqlite3.connect(dbname)
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS card_set")
c.execute("CREATE TABLE card_set(id, suit, num, rank, img)")

suits = ["c", "d", "h", "s"]
for i in range(52):
    p = "INSERT INTO card_set(id, suit, num, rank, img) VALUES(?, ?, ?, ?, ?)"
    suit = suits[i // 13]
    num = i % 13 + 1
    if num == 1:
        rank = 14
    else:
        rank = num
    c.execute(p, (i + 1, suit, num, rank, suit + str(num) + ".png"))
conn.commit()

c.execute("SELECT * FROM card_set")

deal_index = list(range(1, 53))
random.shuffle(deal_index)
print(deal_index)
for i in deal_index:
    p = "SELECT * FROM card_set WHERE id=?"
    c.execute(p, (i,))
    print(c.fetchone())