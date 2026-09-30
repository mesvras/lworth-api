from pydantic import BaseModel, ConfigDict, Field, field_validator


class UserBase(BaseModel):
    username: str = Field(min_length=3, max_length=30)


class UserCreate(UserBase):
    password: str = Field(min_length=8)

    @field_validator("password")
    @classmethod
    def password_has_digits(cls, v: str) -> str:
        if not any(c.isdigit() for c in v):
            raise ValueError("A senha deve ter ao menos um número")
        return v


class UserUpdate(BaseModel):
    username: str | None = Field(default=None, min_length=3, max_length=30)


class UserOut(UserBase):
    model_config = ConfigDict(
        from_attributes=True
    )  # permite criar o schema a partir de objetos ORM
    id: int
