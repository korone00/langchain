import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo", temperature=0)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a culinary expert"),
        ("user", "{input}"),
    ]
)

output_parser = StrOutputParser()

# LCEL
chain1 = prompt
chain2 = prompt | llm
chain3 = prompt | llm | output_parser

response1 = chain1.invoke({"input": "Speaking of good Japanese food, name one."})
print(response1)
print("------------")
response2 = chain2.invoke({"input": "Speaking of good Japanese food, name one."})
print(response2)
print("------------")
response3 = chain3.invoke({"input": "Speaking of good Japanese food, name one."})
print(response3)
print("------------")