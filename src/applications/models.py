from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber

class ApplicationBase(BaseModel):
    telegram_id: Optional[str] = None
    discord_id: Optional[str] = None
    submitted_at: Optional[str] = datetime.now().astimezone().isoformat()
    updated_at: Optional[str] = datetime.now().astimezone().isoformat()
    email: EmailStr
    phone: Optional[PhoneNumber] = None
    name: str
    surname: str
    patronymic: str
    university: str
    student_group: Optional[str] = None
    application_role: str
    title: str
    adviser: str
    coauthors: Optional[List[str]|None] = None


class ApplicationGet(ApplicationBase):
    id: int


class ApplicationUpdate(ApplicationBase):
    id: Optional[int] = None
    telegram_id: Optional[str] = None
    discord_id: Optional[str] = None
    submitted_at: Optional[str] = None
    updated_at: Optional[str] = datetime.now().astimezone().isoformat()
    email: Optional[EmailStr] = None
    phone: Optional[PhoneNumber] = None
    name: Optional[str] = None
    surname: Optional[str] = None
    patronymic: Optional[str] = None
    university: Optional[str] = None
    student_group: Optional[str] = None
    application_role: Optional[str] = None
    title: Optional[str] = None
    adviser: Optional[str] = None
    coauthors: Optional[List[str]] = None


class ApplicationDelete(BaseModel):
    telegram_id: Optional[str] = None
    discord_id: Optional[str] = None
    email: Optional[EmailStr] = None
