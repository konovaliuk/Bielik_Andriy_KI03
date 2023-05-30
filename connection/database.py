from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseConnection:
    def __init__(self):
        self.engine = create_engine('mysql://root:password@localhost/library')
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()
