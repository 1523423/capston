import openai
import os
import parse
from dotenv import load_dotenv
# 환경 변수 로드
load_dotenv()

key = os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = openai.OpenAI(
    api_key=os.environ.get(key),
)

"""질문 생성 모델
prompt = input("질문을 입력하세요: ")
response = openai.chat.completions.create(
    
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an assistant who analyzes the input questions and generates them again so that you can easily answer them.\nAlways provide guidelines for your answers."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=3000,
    stop=None,
    temperature=0
)
"""

"""
#질문 답변 모델(일반적 질문)
pre_prompt = "Answers to questions should be 1. specific, 2. example code, 3. provide guidelines and 4. easy to understand.\n"
response = openai.chat.completions.create(
model="gpt-3.5-turbo",
messages=[
  {"role": "system", "content": "You are Security Engineering assistant.\nPlease answer in Korean.\nAlways provide guidelines for your answers."},
  {"role": "user", "content":  pre_prompt + prompt}
],

max_tokens=3000,
stop=None,
temperature=0
)
"""
# 질문 답변 모델(코드)
file_name = input("input File name: ")
pre_prompt = "Please analyze the code to be provided in the future by functional unit and let us know the possibility of vulnerability.\nAdditionally, if secure coding is possible, please do it."
with open(f'{file_name}', 'rb') as file:
  prompt = file.read()
response = openai.chat.completions.create(
model="gpt-3.5-turbo",
messages=[
  {"role": "system", "content": "You are Security Engineering assistant\nPlease answer in Korean.\nAlways provide guidelines for your answers."},
  {"role": "user", "content": pre_prompt + str(prompt)}
],

max_tokens=3000,
stop=None,
temperature=0
)
""" 프로젝트 버전 정보 취약점 탐지 모델
file_name = input("input File name: ")
parse.extract_version_ref(file_name)
pre_prompt = "Please analyze the code to be provided in the future by functional unit and let us know the possibility of vulnerability.\nAdditionally, if secure coding is possible, please do it."
with open(f'{file_name}', 'rb') as file:
  prompt = file.read()
response = openai.chat.completions.create(
model="gpt-3.5-turbo",
messages=[
  {"role": "system", "content": "You are Security Engineering assistant\nPlease answer in Korean.\nAlways provide guidelines for your answers."},
  {"role": "user", "content": pre_prompt + str(prompt)}
],

max_tokens=3000,
stop=None,
temperature=0
)
"""
answer = response.choices[0].message.content.strip()
print(answer)