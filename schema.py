#  _______________________
#  Import LIBRARIES
from sqlmodel import Field, SQLModel
#  Import FILES
#  _______________________


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


# Create rows here?
