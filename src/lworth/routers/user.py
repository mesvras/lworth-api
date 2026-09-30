from fastapi import APIRouter, Depends
from lworth.schemas import UserCreate, UserOut
from lworth.service.user import UserService

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/", response_model=list[UserOut])
async def get_all(service: UserService = Depends()):
    return await service.get_all()


@router.get("/{user_id}", response_model=UserOut)
async def get_by_id(user_id: int, service: UserService = Depends()):
    return await service.get_by_id(user_id)


@router.post("/", response_model=UserOut)
async def create_user(user: UserCreate, service: UserService = Depends()):
    return await service.create(user)
