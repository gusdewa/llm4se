from langchain_core.pydantic_v1 import BaseModel, Field, ConstrainedList
from langchain.output_parsers.pydantic import PydanticOutputParser


class Person(BaseModel):
    name: str = Field(description="Name of the person to answer user query")
    dob: str = Field(description="Date of birth of the person in YYYY-MM-DD format")
    height: float = Field(description="Height of the person in cm")


class CoolAnswer(BaseModel):
    answer: str = Field(description="Short answer of the query")
    funfact: str = Field(description="Any fun fact relevant to the answer")
    ref: str = Field(description="Relevant URL to the answer")
    joke: str = Field(description="Any joke relevant to the answer")


parser = PydanticOutputParser(
    pydantic_object=CoolAnswer
)

def get_format_instructions():
    return parser.get_format_instructions()

def get_parser():
    return parser
