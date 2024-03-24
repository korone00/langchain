# 개발환경 설정

## anaconda 설치

설치가 안된 경우 설치

```bash
$ brew install --cask anaconda
```

환경변수에 anaconda 경로 추가 하고, zshrc 파일을 다시 적용한다.

```bash
$ /opt/homebrew/anaconda3/bin/conda init zsh
$ source ~/.zshrc
```

## anaconda 가상환경 설정

Anaconda를 설치하면 base 가상환경이 활성화된 상태로 시작되므로 base 가상환경을 시작을 해제한다.

```bash
(base) ➜ ~ conda deactivate
➜ ~
```

다음과 같이, langchain 가상환경을 생성하고 활성화 시킨다.

```bash
$ conda create --name langchain python=3.11
$ conda activate langchain
```

다음과 같이 langchain을 설치한다.

```bash
(langchain) ➜ ~ conda install langchain -c conda-forge
```

## jupyter notebook 설치

jupyter를 설치하고 설치된 버전 확인

```bash
(langchain) ➜ ~ conda install jupyter
(langchain) ➜ ~ jupyter --version
Selected Jupyter core packages...
IPython          : 8.20.0
ipykernel        : 6.28.0
ipywidgets       : 8.1.2
jupyter_client   : 8.6.0
jupyter_core     : 5.5.0
jupyter_server   : 2.10.0
jupyterlab       : 4.0.11
nbclient         : 0.8.0
nbconvert        : 7.10.0
nbformat         : 5.9.2
notebook         : 7.0.8
qtconsole        : 5.5.1
traitlets        : 5.7.1
```

config파일 생성

$HOME/.jupyter/jupyter_notebook_config.py 파일이 생성돈다.

```bash
(langchain) ➜ ~ jupyter notebook --generate-config
Writing default config to: /Users/korone/.jupyter/jupyter_notebook_config.py
```

password 생성

```bash
(langchain) ➜ ~ jupyter server password
Enter password:
Verify password:
[JupyterPasswordApp] Wrote hashed password to /Users/korone/.jupyter/jupyter_server_config.json
```

다음과 같이 jupyter notebook을 실행한다. 실행이 되면 localhost:8888로 접속된다.

비밀번호를 설정한경우 비밀번호 입력후 진입 가능하다.

```bash
(langchain) ➜ ~ jupyter notebook
```

## 참고사이트

[Installation | 🦜️🔗 Langchain](https://python.langchain.com/docs/get_started/installation)

# OpenAI LCEL(LangChain Expression Langauge)

라이브러리 설치(pip install을 하면 conda install과 충돌날 수 있으므로 conda install을 통해 설치 해야 함)

```python
(langchain) ➜ ~ conda install python-dotenv langchain-openai
```

## 환경변수 설정

.env 파일에 OpenAI API KEY 추가

(https://openai.com 에서 가입필요함)

```bash
(langchain) ➜ ~ cat .env
OPENAI_API_KEY="******"
```

## 소스코드(test.py)

- model : gtp-3.5-trubo

```python
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
```

## 실행

```bash
(langchain) ➜ ~ python test.py
messages=[SystemMessage(content='You are a culinary expert'), HumanMessage(content='Speaking of good Japanese food, name one.')]
------------
content='One popular Japanese dish that is loved by many is sushi. Sushi is a dish that typically consists of vinegared rice combined with various ingredients such as raw fish, vegetables, and seaweed. It is not only delicious but also visually appealing, making it a favorite choice for many people around the world.' response_metadata={'token_usage': {'completion_tokens': 62, 'prompt_tokens': 25, 'total_tokens': 87}, 'model_name': 'gpt-3.5-turbo', 'system_fingerprint': 'fp_3bc1b5746c', 'finish_reason': 'stop', 'logprobs': None}
------------
One popular Japanese dish is sushi. It typically consists of vinegared rice topped with various ingredients such as raw fish, seafood, vegetables, and sometimes tropical fruits. Sushi is not only delicious but also visually appealing, making it a favorite choice for many people around the world.
------------
```

## 참고 사이트

[Getting Started with LangChain](https://dev.to/0xnari/getting-started-with-langchain-2m10)
