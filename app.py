#  _______________________
#  Import LIBRARIES
from sqlmodel import SQLModel, Session, create_engine, select

#  Import FILES
from schema import Hero
#  _______________________


# Server DB - Parameters
# ....
# Hosted DB - Parameters
sqlite_file_name: str = "database.db"
sqlite_url: str = f"sqlite:///{sqlite_file_name}"
# In-memory DB - Parameters
# sqlite_file_name: str = ""
# sqlite_url: str = f"sqlite://{sqlite_file_name}"


engine = create_engine(sqlite_url, echo=True)
# echo=True makes the engine print all the SQL statements it executes,


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


def create_heroes() -> None:
    hero_1: Hero = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2: Hero = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3: Hero = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)

        session.commit()

        # session.close()


def select_heroes() -> None:
    with Session(engine) as session:
        statement = select(Hero)
        results = session.exec(statement)
        print("Printing the iterable - results")
        for hero in results:
            print(hero)


def main() -> None:
    create_db_and_tables()
    create_heroes()
    select_heroes()


if __name__ == "__main__":
    main()
