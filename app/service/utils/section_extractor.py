from schemas.requirement import Requirement

async def section_extractor(ids, requirement) -> list[Requirement]:
  output_section = [section for section in requirement if section.section_id in ids]
  return output_section