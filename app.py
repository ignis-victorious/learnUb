#  _______________________
#  Import LIBRARIES
from sqlmodel import SQLModel, create_engine

#  Import FILES
import schema
#  _______________________


# Server DB - Properties
# ....
# Hosted DB - Properties
sqlite_file_name: str = "database.db"
sqlite_url: str = f"sqlite:///{sqlite_file_name}"
# In-memory DB - Properties
# sqlite_file_name: str = ""
# sqlite_url: str = f"sqlite://{sqlite_file_name}"


engine = create_engine(sqlite_url, echo=True)
# echo=True makes the engine print all the SQL statements it executes,


if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)
