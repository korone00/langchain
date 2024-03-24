import os
from dotenv import load_dotenv
from langchain_community.llms import HuggingFaceEndpoint
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
HUGGINGFACEHUB_API_TOKEN = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
HUGGINGFACEHUB_REPO_ID = os.environ.get("HUGGINGFACEHUB_REPO_ID")

llm = HuggingFaceEndpoint(
    repo_id=HUGGINGFACEHUB_REPO_ID,
    max_new_tokens=2048,
    temperature=0.1,
)

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

response1 = chain1.invoke({"input": "Speaking of good Korean food, name one."})
print(response1)
print("------------")
response2 = chain2.invoke({"input": "Speaking of good Korean food, name one."})
print(response2)
print("------------")
response3 = chain3.invoke({"input": "Speaking of good Korean food, name one."})
print(response3)
print("------------")