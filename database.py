from sqlalchemy import create_engine, text
import sqlite3, sys

engine = create_engine("sqlite:///entries.db")

def make_entries_db():
    con = sqlite3.connect("entries.db")
    cur = con.cursor()
    cur.execute("DROP TABLE if exists entries")
    mktable = """CREATE TABLE entries (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    date VARCHAR(10),
    entrytext VARCHAR(300),
    entrytime INTEGER)"""
    cur.execute(mktable)

def get_entries():
    con = engine.connect()
    return list(con.execute(text("SELECT * from entries")))

def get_recent_entries():
    con = engine.connect()
    return list(con.execute(text("SELECT * from entries ORDER BY entrytime DESC LIMIT 5")))

def add_entry(dt, etext, etime):
    con = engine.connect()
    ins = "INSERT INTO entries (date, entrytext, entrytime) VALUES (:dt, :etext, :etime)"
    con.execute(text(ins), {"dt": dt, "etext": etext, "etime": etime})
    con.commit()

#add_entry("20240226", "hi hi bye", 123)

if __name__ == '__main__':
    if '--make-entries' in sys.argv:
        make_entries_db()