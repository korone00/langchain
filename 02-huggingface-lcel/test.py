import os
from dotenv import load_dotenv
from langchain_community.llms import HuggingFaceEndpoint
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
HUGGINGFACEHUB_API_TOKEN = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
HUGGINGFACEHUB_REPO_ID = os.environ.get("HUGGINGFACEHUB_REPO_ID")

# llm = HuggingFaceHub(
#     repo_id=HUGGINGFACE_REPO_ID,
#     task="text-generation",
#     model_kwargs={
#         "max_new_tokens": 512,
#         "top_k": 30,
#         "temperature": 0.1,
#         "repetition_penalty": 1.03,
#     },
# )
llm = HuggingFaceEndpoint(
    repo_id=HUGGINGFACEHUB_REPO_ID,
    max_new_tokens=2048,
    temperature=0.1,
    # callbacks=[StreamingStdOutCallbackHandler()],  # 콜백을 설정합니다.
    # streaming=True,  # 스트리밍을 사용합니다.
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