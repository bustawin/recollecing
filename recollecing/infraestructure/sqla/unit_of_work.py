from typing import Optional

from sqlalchemy.orm import Session, scoped_session, sessionmaker

from recollecing.application.unit_of_work import AbstractUnitOfWork
from recollecing.infraestructure.sqla.repository import SQLARepository, engine


class SQLAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, db_uri: Optional[str] = None) -> None:
        super().__init__()
        self.session_factory = scoped_session(sessionmaker(bind=engine(db_uri)))

    def __enter__(self):
        self.session: Session = self.session_factory()
        self.init_repositories(SQLARepository(self.session))
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def flush(self):
        self.session.flush()

    def commit(self):
        # todo intercept only expected DB exceptions:
        #   URL is not unique
        #   ID already exists...
        self.session.commit()

    def rollback(self):
        self.session.rollback()
