"""
Comments router
"""

from typing import Sequence, Annotated
from fastapi import APIRouter, Depends, Form
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Comments, User
from ..schemas import CommentReadSchema, CommentsCreateSchema
from ..services import CommentsService
from src.database import get_db
from src.users.auth import current_user, fastapi_users



authenticated_user = fastapi_users.current_user(active=True)

router = APIRouter(
    prefix="/comments",
    tags=["Comments"]
)

@router.get("", response_model=Sequence[CommentReadSchema])
async def get_comments(offset: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)) -> Sequence[Comments]:
    """
    Get all comments
    """
    return await CommentsService.get_comments(db=db, offset=offset, limit=limit)

@router.get("/{comment_id}", response_model=CommentReadSchema)
async def get_comment_object(comment_id: int, db: AsyncSession = Depends(get_db)) -> Comments:
    """
    Get comment by id
    """
    return await CommentsService.get_comment_object(db=db, comment_id=comment_id)

@router.post("", response_model=CommentReadSchema)
async def create_comment_object(
    content: Annotated[str, Form()],
    news_id: Annotated[int, Form()], 
    user: User = Depends(authenticated_user),  
    db: AsyncSession = Depends(get_db),
) -> Comments:
    """ Creates a comment object """
    return await CommentsService.create_comment(
        db=db,
        comment={
            "content": content,
            "news_id": news_id,
            "user_id": user.id,
        }
    )

@router.put("/{comment_id}", response_model=CommentReadSchema)
async def update_comment(
    comment_id: int,
    content: Annotated[str, Form()],
    user: User = Depends(authenticated_user),
    db: AsyncSession = Depends(get_db),
) -> Comments:
    """ Updates a comment object by id """
    comment = await CommentsService.get_comment_object(db, comment_id)
    return await CommentsService.update_comment(
        db=db,
        comment_id=comment_id,
        comment={"content": content}
    )

@router.delete("/{comment_id}", status_code=204)
async def delete_comment_object(comment_id: int, db: AsyncSession = Depends(get_db), user: User = Depends(authenticated_user)) -> None:
    """
    Deletes a comment
    """
    return await CommentsService.delete_comment(db=db, comment_id=comment_id, user=user)








