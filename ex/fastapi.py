# from pydoc import describe
#
# from fastapi import FastAPI, HTTPException
# from pydentic import BasedModel, Field
#
# app = FastAPI()
#
# class PromptRequest(BasedModel):
#     prompt: str = Field(..., min_length=5, description='Prompt')
#     token: int = Field(default=0, len=500, description='Token')
#
# class PromptResponse(BasedModel):
#     status: str
#     rply: str
#
# @app.post("/prompt", response_model=PromptResponse)
# async def prompt(prompt_request: PromptRequest):
#     if 'error' in prompt_request.prompt.lower():
#         raise HTTPException(status_code=400, detail='Error')
#     rply = 'Success'
#     return PromptResponse(status=rply)

# import json
# import re
#
# def jsonvalidator(raw_json):
#     try:
#         match = re.search(r"\{.*\}", raw_json)
#         return json.loads(match.group(0))
#     except json.decoder.JSONDecodeError:
#         raise ValueError(raw_json)
# print(jsonvalidator("Sure! Here is your data: ```json\n{\"task\": \"Deploy\", \"status\": \"Ready\"}\n```"))  # Valid JSON

# logs = [
#     {"service": "auth", "status": 200},
#     {"service": "auth", "status": 500},
#     {"service": "payment", "status": 500},
#     {"service": "payment", "status": 500},
# ]
# c=0
# res = {}
# for d in logs:
#     if d['status'] == 500:
#         if d['service'] not in res:
#             res[d['service']] = 1
#         else:
#             res[d['service']] += 1
# print(res)

import time
from functools import wraps
def time_measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        time_taken = end - start
        print(time_taken)
        # print(f"{func.__name__} executed in {time_taken:.4f} seconds")
        return result
    return wrapper
@time_measure
def data_load():
    time.sleep(1)
    return "Data loaded"
print(data_load())