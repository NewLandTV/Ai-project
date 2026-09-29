# 소개

## 개발 동기

&nbsp;&nbsp;&nbsp;&nbsp;누구나 **자신이 원하는** 인공지능 버츄얼 유튜버를 만들고, 실제 방송까지 하는 것을 도와주고자 이 프로젝트를 시작하였습니다.

## 목표

&nbsp;&nbsp;&nbsp;&nbsp;**나만의 인공지능**을 만들고, **직접 방송**하며 **가상 버츄얼 유튜버**의 기본이 될 수 있게 도와줍니다.

# 차례

- Ⅰ. 데모 영상
- Ⅱ. 스튜디오 설정
- Ⅲ. 관련 링크

# Ⅰ. 데모 영상

[![방송하는 AI 버튜버 만들기 (Ai project)](https://img.youtube.com/vi/LApZVb76Qj4/0.jpg)](https://www.youtube.com/watch?v=LApZVb76Qj4)

[![실시간 인공지능 버튜버 만드는 법 (Ai project)](https://img.youtube.com/vi/qJGM1dSWAxo/0.jpg)](https://www.youtube.com/watch?v=qJGM1dSWAxo)

# Ⅱ. 스튜디오 설정

## Chapter 0 ― 개막

&nbsp;&nbsp;&nbsp;&nbsp;**Ai 스튜디오**는 Ai 프로젝트에서 다양한 Ai 혹은 유용한 기능을 직관적이고 편리하게 다룰 수 있는 가상의 환경입니다. 단순히 가상의 환경을 설정하는 것에 그치지 않고, 원하는 설정값을 조절하여 원하는 인공지능 버츄얼 유튜버를 관리하고자 사용합니다.

## Chapter 1 ― 준비

### 1. Ai 프로젝트 리포지토리 설치

&nbsp;&nbsp;&nbsp;&nbsp;본 프로젝트 GitHub 페이지에 있는 **<> Code ▼** 버툰을 누르고 **Download ZIP** 또는 아래의 과정 (1)을 수행합니다.

**과정 (1)**

&nbsp;&nbsp;&nbsp;&nbsp;git이 설치된 환경에서 명령 프롬프트(cmd) 혹은 배시 스크립트 입력에 다음 명령을 사용하여 리포지토리를 로컬 환경으로 복제해 옵니다.

```sh
git clone https://github.com/NewLandTV/Ai-project.git
```

### 2. 파이썬 환경 설정

&nbsp;&nbsp;&nbsp;&nbsp;Ai 프로젝트는 초기 파이썬 구동 환경을 자동으로 설정해 주는 스크립트를 제공하고 있습니다. 아래의 스크립트 파일을 실행하여 파이썬 코드를 실행할 수 있도록 합니다.

&nbsp;&nbsp;&nbsp;&nbsp;마찬가지로 명령 프롬프트나 배시 스크립트에서 아래의 명령을 실행합니다.

```sh
init.bat
```

## Chapter 2 ― 설정

### 1. Ollama 준비

&nbsp;&nbsp;&nbsp;&nbsp;Ollama 플랫폼을 로컬 환경에 설치한 상태에서 아래의 과정 (2)를 수행합니다.

**과정 (2)**

&nbsp;&nbsp;&nbsp;&nbsp;① Ai 프로젝트 최상단을 경로를 기준으로 **src/main.py**에 존재하는 파일을 엽니다.

&nbsp;&nbsp;&nbsp;&nbsp;② 코드에서 chatbot = Chatbot(model="…") 중 …에 해당하는 내용을 Ollama에서 지원하는 **모델명**을 입력하고 파일을 저장합니다.

### 2. VTube Studio 연동

&nbsp;&nbsp;&nbsp;&nbsp;VTube Studio 프로그램과 Ai 프로젝트를 연결하기 위해서 아래의 과정 (3)을 수행합니다.

**과정 (3)**

&nbsp;&nbsp;&nbsp;&nbsp;① VTube Studio 좌측의 **Settings** 버튼을 누릅니다.

&nbsp;&nbsp;&nbsp;&nbsp;② 왼쪽 위에 **General Settings & External Connections**를 선택합니다.

&nbsp;&nbsp;&nbsp;&nbsp;③ 우측 메뉴에서 **VTube Studio Plugins**를 찾아 Start API (allow plugins)를 사용하도록 체크합니다.

### 3. OBS 연동

&nbsp;&nbsp;&nbsp;&nbsp;OBS의 WebSocket 서버와 Ai 프로젝트를 연결하기 위해서 아래의 과정 (4)를 수행합니다.

**과정 (4)**

&nbsp;&nbsp;&nbsp;&nbsp;① OBS 프로그램의 상단 메뉴바에서 **도구(T) > WebSocket 서버 설정**을 엽니다.

&nbsp;&nbsp;&nbsp;&nbsp;② 플러그인 설정에서 **WebSocket 서버 사용**을 체크하고, 서버 설정에서 **서버 포트**와 **서버 비밀번호**를 복사합니다.

&nbsp;&nbsp;&nbsp;&nbsp;③ 복사된 서버 정보를 Ai 프로젝트 최상단 디렉토리에서 **.env** 파일을 생성하고 아래의 양식에 따라서 정보를 붙여 넣습니다.

```py
# OBS 설정
obs_host = "localhost"
obs_port = "your obs server port"
obs_password = "your obs server password"
```

## Chapter 3 ― 실행

&nbsp;&nbsp;&nbsp;&nbsp;아래의 명령을 수행하여 Ai 스튜디오를 실행합니다.

```sh
run
```

# Ⅲ. 관련 링크

<div>
    <a href="https://www.youtube.com/@장경혁tv" target="_blank">
        <img alt="JkhTV YouTube" src="https://img.shields.io/badge/장경혁tv-FF0000.svg?&style=flat-square&logo=YouTube&logoColor=white"/>
    </a>
    <a href="https://cafe.naver.com/2019newland" target="_blank">
        <img alt="NewLand Naver Cafe" src="https://img.shields.io/badge/NewLand Naver Cafe-03C75A.svg?&style=flat-square&logo=Naver&logoColor=white"/>
    </a>
    <a href="https://discord.gg/2J646MaZGA" target="_blank">
        <img alt="NewLand Discord" src="https://img.shields.io/badge/NewLand Discord-5865F2.svg?&style=flat-square&logo=Discord&logoColor=white"/>
    </a>
</div>
