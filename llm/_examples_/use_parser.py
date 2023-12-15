from llm.prompts.pydantic_prompt import create_prompt
from llm.parsers.json_parser import get_parser
from llm.foundation_models.language_model import create_model

def ask(query):
    prompt = create_prompt(query)
    # output parser only support language model - not chat model
    model = create_model()
    parser = get_parser()
    
    output = model.invoke(prompt)
    parsed_output = parser.parse(output)
    return parsed_output.json()
