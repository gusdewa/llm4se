from langchain.prompts.chat import ChatPromptTemplate
from llm.parsers.json_parser import get_format_instructions
from langchain.prompts import PromptTemplate

def create_prompt(query):
    prompt_template = PromptTemplate(
        template="Answer the user query.\n{format_instructions}\n{query}\n",
        input_variables=["query"],
        partial_variables={"format_instructions": get_format_instructions()},
    )
    output = prompt_template.format_prompt(query=query)
    return output.to_string()
