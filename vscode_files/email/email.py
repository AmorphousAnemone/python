import sqlite3

conn = sqlite3.connect('emaildb.sqlite') # Connects to database, creates if none.
cur = conn.cursor() # Send sql commands through 'cursor' and receive response

cur.execute('DROP TABLE IF EXISTS Counts') # DROP TABLE is sql command.
# Keeps this script from blowing up (?)
# inserts sql db into file (?)

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')
# Create table table_name (column1 datatype, column2 datatype...)

# opens and loops through file to grabs emails.
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    # Question mark '?' indicates where a value is to be inserted, 
    # the value being the tuple at the end.
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', 
                    (email,))
    # In DB, it's better to use "UPDATE" because multiple apps may be talking to DB at one time.
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
# print('It works' + fname)
