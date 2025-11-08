@echo off
call .venv\Scripts\activate
call ollama pull mistral
call python src\main.py