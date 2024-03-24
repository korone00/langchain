import os
from dotenv import load_dotenv
from langchain_community.llms import HuggingFaceEndpoint
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline

load_dotenv()
HUGGINGFACEHUB_API_TOKEN = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
HUGGINGFACEHUB_REPO_ID = os.environ.get("HUGGINGFACEHUB_REPO_ID")

llm = HuggingFacePipeline.from_model_id(
    model_id=HUGGINGFACEHUB_REPO_ID,
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 512},
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "당신은 요리 전문가입니다."),
        ("user", "{input}"),
    ]
)

output_parser = StrOutputParser()

# LCEL
chain1 = prompt
chain2 = prompt | llm
chain3 = prompt | llm | output_parser

response1 = chain1.invoke({"input": "맛있는 한국 음식이 생각나서 말인데 하나만 꼽아주세요."})
print(response1)
print("------------")
response2 = chain2.invoke({"input": "맛있는 한국 음식이 생각나서 말인데 하나만 꼽아주세요."})
print(response2)
print("------------")
response3 = chain3.invoke({"input": "맛있는 한국 음식이 생각나서 말인데 하나만 꼽아주세요."})
print(response3)
print("------------")