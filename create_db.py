import sqlite3

con = sqlite3.connect('resourcesDB/dataBase.db')

cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS user (
                    user_id INTEGER PRIMARY KEY NOT NULL,
                    user_name TEXT NOT NULL
               );"""
           )

cur.execute("""CREATE TABLE IF NOT EXISTS blob (
                    blob_id INTEGER PRIMARY KEY NOT NULL,
                    blob_location TEXT NOT NULL
               );"""
           )

cur.execute("PRAGMA foreign_keys=on")
cur.execute("PRAGMA foreign_keys")

r = cur.fetchall()

print(r)

cur.execute("""CREATE TABLE IF NOT EXISTS writable_by (
                    blob_id INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    PRIMARY KEY(blob_id, user_id),
                    FOREIGN KEY(blob_id) REFERENCES blob(blob_id)
                    FOREIGN KEY(user_id) REFERENCES user(user_id)
               );"""
           )

cur.execute("""CREATE TABLE IF NOT EXISTS readable_by (
                    blob_id INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    PRIMARY KEY(blob_id, user_id),
                    FOREIGN KEY(blob_id) REFERENCES blob(blob_id)
                    FOREIGN KEY(user_id) REFERENCES user(user_id)
               );"""
           )



cur.execute("INSERT INTO user(user_name) VALUES ('Juan')")
cur.execute("INSERT OR IGNORE INTO user(user_id, user_name) VALUES ('2', 'Pedro')")
cur.execute("INSERT OR IGNORE INTO blob(blob_id, blob_location) VALUES ('2', 'resourcesBlobs/prueba.txt')")
cur.execute("INSERT OR IGNORE INTO writable_by(blob_id, user_id) VALUES ('2', '1')")
cur.execute("INSERT OR IGNORE INTO readable_by(blob_id, user_id) VALUES ('2', '2')")


con.commit()

con.close()