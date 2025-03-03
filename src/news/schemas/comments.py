"""
Pydantic schemas for Comments
"""

from datetime import datetime

from pydantic import BaseModel


class CommentReadSchema(BaseModel):
    """
    Schema for reading a comment
    """
    id: int
    news_id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class CommentsCreateSchema(BaseModel):
    """
    Comment create schema
    """
    news_id: str
    

class CommentUpdateSchema(BaseModel):
    """
    Schema for updating a comment
    """
    content: str