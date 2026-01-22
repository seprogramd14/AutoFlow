from pydantic import BaseModel
from schemas.requirement import Requirement

class RequestPage(BaseModel):
    section_ids: list[int]
    requirement: list[Requirement]

class PageDetail(BaseModel):
    page_name: str
    description: str
    features: list[str]
    api_endpoints: list[str]
    user_actions: list[str]
    data_displayed: list[str]

class StructuredPageDetails(BaseModel):
    pages: list[PageDetail]