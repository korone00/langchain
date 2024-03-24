# HuggingFace Local download

라이브러리 설치(pip install을 하면 conda install과 충돌날 수 있으므로 conda install을 통해 설치 해야 함)

```python
(langchain) ➜ ~ conda install pytorch torchvision -c pytorch
```

## Access Token인증

huggingface에 가입하여 access token 을 발급받고 다음과 같이 인증을 한다.

```bash
(langchain) (base) ➜ 03-huggingface-local (main) ✗ python
Python 3.11.8 | packaged by conda-forge | (main, Feb 16 2024, 20:49:36) [Clang 16.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from huggingface_hub import login
>>> login()

    _|    _|  _|    _|    _|_|_|    _|_|_|  _|_|_|  _|      _|    _|_|_|      _|_|_|_|    _|_|      _|_|_|  _|_|_|_|
    _|    _|  _|    _|  _|        _|          _|    _|_|    _|  _|            _|        _|    _|  _|        _|
    _|_|_|_|  _|    _|  _|  _|_|  _|  _|_|    _|    _|  _|  _|  _|  _|_|      _|_|_|    _|_|_|_|  _|        _|_|_|
    _|    _|  _|    _|  _|    _|  _|    _|    _|    _|    _|_|  _|    _|      _|        _|    _|  _|        _|
    _|    _|    _|_|      _|_|_|    _|_|_|  _|_|_|  _|      _|    _|_|_|      _|        _|    _|    _|_|_|  _|_|_|_|

    A token is already saved on your machine. Run `huggingface-cli whoami` to get more information or `huggingface-cli logout` if you want to log out.
    Setting a new token will erase the existing one.
    To login, `huggingface_hub` requires a token generated from https://huggingface.co/settings/tokens .
Token:
Add token as git credential? (Y/n) y
Token is valid (permission: read).
Your token has been saved in your configured git credential helpers (osxkeychain).
Your token has been saved to /Users/korone/.cache/huggingface/token
Login successful
>>>
```

## 환경변수 설정

.env 파일에 API Token 및 MODEL 추가

모델

- LLM leaderboard : https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard
- Upstage leaderboard : https://huggingface.co/spaces/upstage/open-ko-llm-leaderboard

```bash
(langchain) ➜ ~ cat .env
HUGGINGFACEHUB_API_TOKEN=*****
HUGGINGFACEHUB_REPO_ID=beomi/llama-2-ko-7b
```

## 실행

실행하면, $HOME/.cache/huggingface/hub 폴더에 모델이 생성된다.
용량이 꽤 크기 때문에 더이상 필요 없는 경우 삭제를 해야 한다.
다음을 제대로 실행하기 위해서는 GPU가 있는 PC에서 실행해야지 빠른 속도로 실행된다.

```bash
(langchain) ➜ ~ python test.py

```
