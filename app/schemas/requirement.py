from pydantic import BaseModel

class RequestRequirement(BaseModel):
  input_text: str

class ResponseRequirement(BaseModel):
  output_text: str