from llm.prompts.pydantic_prompt import create_prompt
from llm.parsers.json_parser import get_parser
from llm.foundation_models.language_model import create_model

def ask(query):
    prompt = create_prompt(query)
    model = create_model()
    parser = get_parser()

    output = model.invoke(prompt)
    should_be_a_person = parser.parse(output)
    return should_be_a_person.json()
