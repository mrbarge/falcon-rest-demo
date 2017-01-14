from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from model import Review
import json

engine = create_engine(
	'sqlite:///app.db'
)
Base = declarative_base(engine)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

class SQLAlchemySessionManager:
    def __init__(self, Session):
        self.Session = Session

    def process_resource(self, req, resp, resource, params):
        resource.session = self.Session()

    def process_response(self, req, resp, resource, req_succeeded):
        if hasattr(resource, 'session'):
            resource.session.close()

class ReviewAPI:

    def on_get(self, req, resp, book_id):
        try:
            reviews = Review.find_by_book_id(self.session, int(book_id))
            rj = [{"review":r.review, "rating":r.rating} for r in reviews]
            resp.body = json.dumps(rj)
        except NoResultFound:
            resp.body = "[]"

        resp.status = falcon.HTTP_200  # This is the default status

import falcon

application = falcon.API(middleware=[
        SQLAlchemySessionManager(Session),
])
reviewapi = ReviewAPI()
application.add_route('/reviews/{book_id}',reviewapi)

