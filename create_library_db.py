import sqlite3

conn = sqlite3.connect('library.db')

cursor = conn.cursor()

cursor.executescript('''
-- Create Authors table
CREATE TABLE IF NOT EXISTS Authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    bio TEXT,
    birth_date DATE
);

-- Create Books table
CREATE TABLE IF NOT EXISTS Books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER,
    published_date DATE,
    genre TEXT,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

-- Create Members table
CREATE TABLE IF NOT EXISTS Members (
    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT
);

-- Create Loans table
CREATE TABLE IF NOT EXISTS Loans (
    loan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    member_id INTEGER,
    loan_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);
''')

conn.commit()
conn.close()

print("Tables created successfully!")