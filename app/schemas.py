from pydantic import BaseModel


class GetUrls(BaseModel):
    domains: list
    status: str


class AddUrls(BaseModel):
    links: list
