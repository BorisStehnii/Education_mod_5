from sqlalchemy import create_engine, Column, String, Integer, or_, text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, aliased


engine = create_engine('sqlite:///lib.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Reader(Base):

    __tablename__ = 'reader'

    reader_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    books = relationship('Book', back_populates='reader')


class Author(Base):

    __tablename__ = 'author'

    author_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    books = relationship('BookAuthor', back_populates='author', cascade='all, delete')


class Book(Base):

    __tablename__ = 'book'

    book_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)

    reader_id = Column(Integer, ForeignKey('reader.reader_id'), ondelete='CASCADE')     # связь с атрибутами другой таблиці
    authors = relationship('BookAuthor', back_populates='book', cascade='all, delete')     # обратная связь с промежуточной таблицей

    reader = relationship('Reader', back_populates='books')


class BookAuthor(Base):     # промежуточная таблица

    __tablename__ = 'book_author'

    ba_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('author.author_id', ondelete='CASCADE'))
    book_id = Column(Integer, ForeignKey('book.book_id', ondelete='CASCADE'))

    author = relationship('Author', back_populates='books')
    book = relationship('Book', back_populates='authors')


if __name__ == '__main__':
    session = Session()

    # Base.metadata.create_all(engine)
    #
    # author_1 = Author(name='King')
    # author_2 = Author(name='Pratchet')
    #
    # book_1 = Book(title='Dark Tower', genre='fantasy')
    # session.add_all([author_1, book_1])
    # book_2 = Book(title='Mort', genre='fantasy')
    # session.add_all([author_2, book_2])
    #
    # ba_1 = BookAuthor(author=author_1, book=book_1)
    # session.add(ba_1)
    # ba_2 = BookAuthor(author=author_2, book=book_2)
    # session.add(ba_2)
    #
    # reader_1 = Reader(name='Boris', age=24)
    # session.add(reader_1)
    # reader_1.books.append(book_1)
    # reader_1.books.append(book_2)
    #
    # session.commit()
    # session.close()
    print("__________")
    # reader = session.query(Reader).filter(Reader.name == 'Boris').all()

    # reader = session.query(Reader).filter_by(name='Boris', age=24)

    # print(reader[0].name, reader[0].age)
    # print(reader)
    # books = session.query(Book).join(BookAuthor).filter(BookAuthor.book_id == Book.book_id).join(Author).filter(Author.name == 'King').all()
    books = session.query(Book, BookAuthor, Author).filter_by(Book.book_id == BookAuthor.book_id, Author.author_id == BookAuthor.author_id)

    reader = books[0].reader
    reader.name = 'Bob'

    book = session.query(Book).filter(Book.title == 'Mort').all()[0]

    # session.delete(book)
    session.commit()
    session.close()



