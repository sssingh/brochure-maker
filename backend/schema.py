from typing import List
from pydantic import BaseModel, Field


# Relevant URL output schema
class RelevantUrls(BaseModel):
    company_name: str = Field(description="Name of the company")
    company_url: str = Field(description="Company's home page URL")
    relevant_urls: List[str] = Field(description="Relevant URL list")
