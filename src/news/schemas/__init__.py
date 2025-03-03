"""
__init__.py
"""

from .categories import CategoryCreateSchema, CategoryReadSchema
from .news import NewsReadSchema, NewsReadDetailsSchema
from .comments import CommentReadSchema, CommentsCreateSchema, CommentUpdateSchema


__all__ = [
    "CategoryCreateSchema",
    "CategoryReadSchema",
    "NewsReadSchema",
    "NewsReadDetailsSchema",
    "CommentCreateSchema",
    "CommentReadSchema",
    "CommentUpdateSchema"
]
