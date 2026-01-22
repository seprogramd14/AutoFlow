from fastapi import APIRouter, HTTPException
from service.ai.page_extractor import create_page_details
from schemas.page import RequestPage, StructuredPageDetails
from schemas.common import ErrorResponse

router = APIRouter(prefix="/page")

page_description = """
- Section 3: System Structure
- Section 4: Functional Requirements
- Section 5.1: API Requirements - Endpoints Needed

추출된 요구사항 명세를 기반으로 세부 페이지를 산출합니다.
OpenAI gpt-5-mini를 사용합니다.
"""

@router.post(
    "/details",
    description=page_description,
    response_model=StructuredPageDetails,
    responses={
        500: {
            "model": ErrorResponse,
            "description": "서버 내부 오류"
        }
    }
)
async def get_page_details(request: RequestPage):
    try:
        output = await create_page_details(request)
        return output
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
