from service.ai.openai_client import client
from schemas.requirement import StructuredRequirement, Requirement
from schemas.page import StructuredPageDetails

instructions = """
You are a Frontend Architect with 10 years of experience in page structure design.

Your role is to analyze requirements and extract detailed page specifications
that enable frontend developers to implement each page effectively.

Given requirements about:
- System structure (pages and features)
- Functional requirements (by page and by feature)
- API endpoints

Extract and organize detailed page specifications for each identified page.

For each page, you must provide:
1. **page_name**: Clear, concise page name (e.g., "Home Dashboard", "Ride Recording")
2. **description**: Brief description of the page's purpose and role
3. **features**: List of reusable features/components used on this page
4. **api_endpoints**: List of API endpoints this page interacts with (e.g., "GET /activities", "POST /recordings/upload")
5. **user_actions**: List of actions users can perform on this page
6. **data_displayed**: List of data/information displayed to the user

Be thorough and extract all pages mentioned in the requirements.
Organize the information clearly for frontend implementation.
"""

def filter_page_relevant_requirements(requirements: list[Requirement]) -> list[Requirement]:
    """
    Filter requirements to include only sections 3, 4, and 5.1
    - Section 3: System Structure
    - Section 4: Functional Requirements
    - Section 5.1: API Requirements - Endpoints Needed
    """
    filtered = []
    for req in requirements:
        section = req.section.strip()
        # Section 3: System Structure
        if section.startswith("3."):
            filtered.append(req)
        # Section 4: Functional Requirements
        elif section.startswith("4."):
            filtered.append(req)
        # Section 5.1: Endpoints
        elif "5.1" in section or section.startswith("5. API Requirements - 5.1"):
            filtered.append(req)
    return filtered

def format_requirements_as_text(requirements: list[Requirement]) -> str:
    """Convert filtered requirements into readable text format"""
    text_parts = []
    for req in requirements:
        text_parts.append(f"## {req.section}")
        for sentence in req.sentences:
            text_parts.append(f"- {sentence}")
        text_parts.append("")  # Empty line between sections
    return "\n".join(text_parts)

async def create_page_details(requirements: StructuredRequirement) -> StructuredPageDetails:
    """
    Extract page details from requirements by filtering sections 3, 4, and 5.1
    and generating structured page specifications using OpenAI API
    """
    # Filter relevant requirements
    filtered_reqs = filter_page_relevant_requirements(requirements.requirements)

    if not filtered_reqs:
        # Return empty result if no relevant sections found
        return StructuredPageDetails(pages=[])

    # Convert to text format for prompt
    requirements_text = format_requirements_as_text(filtered_reqs)

    # Call OpenAI API with structured output
    response = await client.beta.chat.completions.parse(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": requirements_text}
        ],
        response_format=StructuredPageDetails
    )

    return response.choices[0].message.parsed
