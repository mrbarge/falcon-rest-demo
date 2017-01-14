from sqlalchemy import event
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from app.model import Book, Review
import random
import datetime
import argparse
import sys

def load_words(dict_file):
    with open(dict_file) as f:
        words = f.read().splitlines()
    return words


def make_sentence(words, length):
    ln = len(words)
    w = [words[random.randint(0,ln-1)] for i in range(0,length)]
    s = ' '.join(w)
    return s

def _fk_pragma_on_connect(dbapi_con, con_record):
    dbapi_con.execute('PRAGMA foreign_keys = ON')

def init_db(uri):
    engine = create_engine(uri)
    event.listen(engine, 'connect', _fk_pragma_on_connect)
    Review.metadata.create_all(engine)
    Book.metadata.create_all(engine)
    session_factory = sessionmaker(bind=engine)
    session = scoped_session(session_factory)

    return session

def build_db(dict_path, db_uri):

    session = init_db(db_uri)
    words = load_words(dict_path)
    for i in range(0,10000):
        title_len = random.randint(1,3)
        num_reviews = random.randint(1,4)

        title = make_sentence(words, title_len)
        b = Book(name=title,release_date=datetime.datetime.now())
        session.add(b)
        session.commit()
        for j in range(0,num_reviews):
            review_len = random.randint(1,30)
            review = make_sentence(words, review_len)
            r = Review(review=review,book_id=b.id,rating=random.randint(1,5))
            session.add(r)
            session.commit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate DB.')

    parser.add_argument('--words', dest='words_path',
                        help='path to words file')
    parser.add_argument('--out', dest='outfile',
                        help='output db file')

    args = parser.parse_args()

    if args.words_path is None or args.outfile is None:
        parser.print_help()
        sys.exit(1)

    build_db(args.words_path,'sqlite:///' + args.outfile)