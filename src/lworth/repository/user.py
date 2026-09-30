from lworth.models import User


users = [
    User(id=1, username="Alice", password_hash="mypass123"),
    User(id=2, username="Bob", password_hash="mypass123"),
]


class UserRepository:
    async def get_by_id(self, target_id: int):
        for u in users:
            if u.id == target_id:
                return u

        return None

    async def get_all(self):
        return users

    async def create(self, user):
        if await self.exists(user):
            return None
        users.append(user)
        return user

    async def exists(self, user: User) -> bool:
        for u in users:
            if u.username == user.username:
                return True
        return False

    async def get_next_id(self) -> int:
        return len(users) + 1
