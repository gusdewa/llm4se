from langchain.prompts import ChatPromptTemplate
from langchain.chat_models.openai import ChatOpenAI
from langchain.chains.llm import LLMChain


def invoke(query: str):
    # Do prompt engineering first
    prompt = ChatPromptTemplate.from_template(
        "Answer this in {output_language}: {query}"
    )
    # Now initiate the Chat Model
    llm = ChatOpenAI()

    # Chain everything
    chain = LLMChain(
        prompt=prompt,
        llm=llm
    )
    result = chain.run({
        "output_language": "German",
        "query": query
    })
    return result


def invoke_lcel(query: str):
    # Do prompt engineering first
    prompt = ChatPromptTemplate.from_template(
        "Answer this in {output_language}: {query}"
    )
    # Now initiate the Chat Model
    llm = ChatOpenAI()

    # Chain everything !!
    # Ref: LCEL
    chain = prompt | llm

    # Invoke with all the required variables in the template
    result = chain.invoke({
        "output_language": "German",
        "query": query
    })

    return result.content
