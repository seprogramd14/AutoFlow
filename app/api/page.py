from fastapi import APIRouter, HTTPException
from service.ai.page_extractor import create_page_details
from service.utils.section_extractor import section_extractor
from schemas.page import RequestPage, StructuredPageDetails
from schemas.common import ErrorResponse

router = APIRouter(prefix="/page")

page_description = """
- Section 3: System Structure
- Section 4: Functional Requirements
- Section 5.1: API Requirements - Endpoints Needed

추출된 요구사항 명세를 기반으로 세부 페이지를 산출합니다.
OpenAI gpt-5-mini를 사용합니다.

input(StructuredRequirement), 사용할 section_id
-> section_id를 통해서 필요한 섹션만 추출
-> gpt-5에 투입
-> 구조 output에 따라 figma로 옮기기
"""

@router.post(
    "",
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
        # 1. 섹션 정제
        sections = await section_extractor(request.section_ids, request.requirement)

        # 2. 페이지 상세 생성
        page_details = await create_page_details(sections)

        return page_details
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
