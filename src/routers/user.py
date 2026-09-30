from fastapi import APIRouter, Depends, Response, status

from src.schemas import UserCreate, UserOut
from src.service.user import UserService

router = APIRouter(prefix="/user", tags=["user"])


@router.get("", response_model=list[UserOut])
async def get_all(service: UserService = Depends()):
    return await service.get_all()


@router.get("/{user_id}", response_model=UserOut)
async def get_by_id(user_id: int, service: UserService = Depends()):
    return await service.get_by_id(user_id)


@router.post("", response_model=UserOut)
async def create_user(
    user: UserCreate, response: Response, service: UserService = Depends()
):
    created = await service.create(user)
    response.status_code = status.HTTP_201_CREATED
    return created
