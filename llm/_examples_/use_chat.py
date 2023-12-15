from llm.prompts.chat_prompt import create_prompt
from llm.foundation_models.chat_model import create_model

def ask(query):
    prompt = create_prompt(query)
    model = create_model()
    output = model.invoke(prompt)
    return output.content
