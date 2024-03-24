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
