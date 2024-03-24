from sqlalchemy import create_engine, text
import sqlite3, sys, time

engine = create_engine("sqlite:///entries.db")

def make_entries_db():
    con = sqlite3.connect("entries.db")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS entries")
    mktable = """CREATE TABLE entries (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    date VARCHAR(10),
    entrytext VARCHAR(300),
    entrytime INTEGER)"""
    cur.execute(mktable)

def get_entries(num=None, show=False):
    con = engine.connect()
    query_common = "SELECT * from entries"
    query_num = '' if num == None else " ORDER BY entrytime DESC LIMIT {}".format(num)
    query = query_common + query_num
    res = list(con.execute(text(query)))
    if show:
        for r in res:
            print(r)
    return res

def add_entry(dt, etext):
    etime = int(time.time())
    con = engine.connect()
    ins = "INSERT INTO entries (date, entrytext, entrytime) VALUES (:dt, :etext, :etime)"
    con.execute(text(ins), {"dt": dt, "etext": etext, "etime": etime})
    con.commit()

if __name__ == '__main__':
    if '--make-entries' in sys.argv:
        make_entries_db()
    if '--add' in sys.argv:
        add_entry(sys.argv[1], sys.argv[2])
    if '--show' in sys.argv:
        get_entries(None, True)