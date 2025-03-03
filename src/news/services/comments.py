"""
Services module for Comments
"""

import asyncio
from typing import Sequence

from fastapi import HTTPException
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from ..models import Comments
from ..utils import save_media 

from src.manager import DBManager

class CommentsService():

    @classmethod
    async def get_comments(
        cls,
        db: AsyncSession,
        offset: int = 0,
        limit: int = 10,
    ) -> Sequence[Comments]:
        """
        Service
        """
        return await DBManager.get_objects(db, model=Comments, offset=offset, limit=limit)


    @classmethod
    async def get_comment_object(
        cls,
        db: AsyncSession,
        comment_id: int,
    ) -> Comments:
        """
        Service
        """
        comment = await DBManager.get_object(
            db=db,
            model=Comments,
            field="id",
            value=comment_id,
            options=[joinedload(Comments.user), joinedload(Comments.news)]
        )
        if comment is None:
            raise HTTPException(status_code=404, detail="Comment not found")
        return comment

    @classmethod
    async def create_comment(
        cls,
        db: AsyncSession,
        comment: dict,
        user_id: int
    ) -> Comments:
        """
        Service
        """
        comment["user_id"] = user_id
        return await DBManager.create_object(**comment, db=db, model=Comments, commit=True)

    @classmethod
    async def update_comment(
        cls,
        db: AsyncSession,
        comment_id: int,
        comment_data: dict,
        user_id: int
    ) -> Comments:
        """
        Service
        """
        comment = await cls.get_comment_object(db, comment_id)

        if comment.user_id != user_id:
            raise HTTPException(status_code=403, detail="You can update only your own comments")

        comment_data["updated_at"] = datetime.utcnow()

        return await DBManager.update_object(
            **comment_data, db=db, model=Comments, field="id", value=comment_id, commit=True
        )

    @classmethod
    async def partial_update_comment(
        cls,
        db: AsyncSession,
        comment_id: int,
        comment_data: dict,
        user_id: int
    ) -> Comments:
        """
        Service
        """
        comment = await cls.get_comment_object(db, comment_id)

        if comment.user_id != user_id:
            raise HTTPException(status_code=403, detail="You can update only your own comments")

        comment_data["updated_at"] = datetime.utcnow()

        return await DBManager.partial_update_object(
            **comment_data, db=db, model=Comments, field="id", value=comment_id, commit=True
        )

    @classmethod
    async def delete_comment(
        cls,
        db: AsyncSession,
        comment_id: int,
        user_id: int
    ) -> None:
        """
        Service
        """
        comment = await cls.get_comment_object(db, comment_id)

        if comment.user_id != user_id:
            raise HTTPException(status_code=403, detail="You can delete only your own comments")

        await DBManager.delete_object(db=db, model=Comments, field="id", value=comment_id, commit=True)
