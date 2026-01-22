from pydantic import BaseModel
from schemas.requirement import StructuredRequirement

class RequestPage(StructuredRequirement):
    pass

class PageDetail(BaseModel):
    page_name: str
    description: str
    features: list[str]
    api_endpoints: list[str]
    user_actions: list[str]
    data_displayed: list[str]

class StructuredPageDetails(BaseModel):
    pages: list[PageDetail]
