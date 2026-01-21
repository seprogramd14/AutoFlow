from pydantic import BaseModel

class RequestRequirement(BaseModel):
  input_text: str

class ResponseRequirement(BaseModel):
  output_text: str

class Requirement(BaseModel):
  id: int
  section: str
  sentences: list[str]

class StructuredRequirement(BaseModel):
  requirements: list[Requirement]