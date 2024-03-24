# HuggingFace LCEL(LangChain Expression Langauge)

라이브러리 설치(pip install을 하면 conda install과 충돌날 수 있으므로 conda install을 통해 설치 해야 함)

```python
(langchain) ➜ ~ conda install python-dotenv langchain-openai
```

## 환경변수 설정

.env 파일에 OpenAI API KEY 및 MODEL 추가
(https://openai.com 에서 가입필요함)

```bash
(langchain) ➜ ~ cat .env
OPENAI_API_KEY="******"
OPENAI_MODEL=gpt-3.5-turbo
```

## 실행

```bash
(langchain) ➜ ~ python test.py
messages=[SystemMessage(content='You are a culinary expert'), HumanMessage(content='Speaking of good Korean food, name one.')]
------------
content="One popular Korean dish is bibimbap, which is a delicious and colorful mixed rice bowl topped with an assortment of vegetables, meat (usually beef), a fried egg, and spicy gochujang sauce. It's a flavorful and satisfying meal that showcases the vibrant flavors of Korean cuisine." response_metadata={'token_usage': {'completion_tokens': 58, 'prompt_tokens': 25, 'total_tokens': 83}, 'model_name': 'gpt-3.5-turbo', 'system_fingerprint': 'fp_3bc1b5746c', 'finish_reason': 'stop', 'logprobs': None}
------------
One popular Korean dish is bibimbap, which is a delicious and colorful mixed rice bowl topped with an assortment of vegetables, meat, and a spicy gochujang sauce.
------------
```

## 참고 사이트

[Getting Started with LangChain](https://dev.to/0xnari/getting-started-with-langchain-2m10)
