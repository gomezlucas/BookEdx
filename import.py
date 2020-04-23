import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


def main():
    # create books, users and review tables
    db.execute(
        "CREATE TABLE books(book_id SERIAL PRIMARY KEY, title VARCHAR(30) NOT NULL, author VARCHAR(30) NOT NULL, isbn VARCHAR(10), year INTEGER)"
    )
    db.execute(
        "CREATE TABLE users (id_user SERIAL PRIMARY KEY, password VARCHAR NOT NULL)"
    )
    db.execute(
        "CREATE TABLE reviews (score INTEGER NOT NULL, review VARCHAR(1000) NOT NULL, user_id INTEGER REFERENCES users, book_id INTEGER REFERENCES books)"
    )
    # load books tables from file(books.csv)
    file = open("books.csv")
    reader = csv.reader(file)
    for isb, tit, auth, ye in reader:
        db.execute(
            "INSERT INTO books (title, author, isbn, year) VALUES (:title, :author, :isbn, :year )",
            {"title": tit, "author": auth, "year": ye, "isbn": isb},
        )
        print(f"{isb}- {tit} - {auth} -{ye}")
    #commit 
    db.commit()


if __name__ == "__main__":
    main()
