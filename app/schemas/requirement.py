from pydantic import BaseModel

class RequestRequirement(BaseModel):
  input_text: str

class ResponseRequirement(BaseModel):
  output_text: str

class Requirement(BaseModel):
  section_id: int
  section_name: str
  sentences: list[str]

class StructuredRequirement(BaseModel):
  requirement: list[Requirement]