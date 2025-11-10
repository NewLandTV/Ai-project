@echo off

rem 가상 환경 생성 및 활성화
set envName=".venv"
set pyVer="3.14"

call py -%pyVer% -m venv %envName%
call %envName%\Scripts\activate

rem 필요한 모듈 설치
call python -m pip install --upgrade pip
call pip install -r requirements.txt