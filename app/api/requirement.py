from fastapi import APIRouter, HTTPException
from service.ai.requirement_extractor import create_requirement
from schemas.requirement import RequestRequirement, StructuredRequirement
from schemas.common import ErrorResponse

router = APIRouter(prefix="/requirement")

requirement_description = """
클라이언트의 요청을 요구사항 명세 텍스트로 추출합니다.
OpenAI gpt-5-mini를 사용합니다.
"""
@router.post(
    "",
    description=requirement_description,
    response_model=StructuredRequirement,
    responses={
        500: {
            "model": ErrorResponse,
            "description": "서버 내부 오류"
        }
    }
)
async def requirement(request: RequestRequirement):
	try:
		output = await create_requirement(request.input_text)
		return output
	except:
		raise HTTPException(status_code=500)