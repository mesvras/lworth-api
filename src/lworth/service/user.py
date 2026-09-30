from fastapi import Depends

from lworth.base.exceptions import AlreadyExistsError, NotFoundError
from lworth.models import User
from lworth.schemas import UserCreate
from lworth.repository.user import UserRepository


class UserService:
    def __init__(self, repo: UserRepository = Depends()):
        self.repo = repo

    async def get_all(self):
        return await self.repo.get_all()

    async def get_by_id(self, user_id: int):
        user = await self.repo.get_by_id(user_id)
        if user is None:
            raise NotFoundError("Usuário", user_id)
        return user

    async def create(self, data: UserCreate):
        next_id = await self.repo.get_next_id()

        user = User(
            username=data.username,
            password_hash=data.password,
            id=next_id,
        )

        created = await self.repo.create(user)
        if created is None:
            raise AlreadyExistsError("Usuário", data.username)
        return created

    async def get_next_id(self):
        return await self.repo.get_next_id()
