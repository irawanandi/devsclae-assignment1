from sqlmodel import create_engine, Session

engine = create_engine(url="sqlite:///database.db")


def get_db():
    with Session(bind=engine) as session:
        yield session
