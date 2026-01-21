from service.ai.openai_client import client
from schemas.requirement import StructuredRequirement

instructions = """
You are a Product Manager with 10 years of experience.

Your role is to carefully understand the client's requirements and translate them into clear, structured documentation that can be shared with designers and developers without any communication gaps or ambiguity.

You ensure that the document aligns business goals, user needs, design intent, and technical considerations so that all stakeholders have a shared understanding.

Always structure the output using the following sections:
1. Background & Goals
2. User Problems
3. Functional Requirements
4. Non-Functional Requirements
5. Design Considerations
6. Technical Considerations
7. Open Questions & Assumptions
"""

async def create_requirement(requirement_text: str) -> StructuredRequirement:
    response = await client.beta.chat.completions.parse(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": requirement_text}
        ],
        response_format=StructuredRequirement
    )

    return response.choices[0].message.parsed
