import uuid
from django.db import models
from schemas import BaseCreate, BaseUpdate


class BaseService:
    model: models.Model = None

    @classmethod
    def get_all(cls) -> list[models.Model]:
        return cls.model.objects.all()
    
    @classmethod
    def get_by_id(cls, id: uuid.UUID) -> models.Model:
        return cls.model.objects.get(id=id)
    
    @classmethod
    def create(cls, data: BaseCreate) -> models.Model:
        return cls.model.objects.create(**data.model_dump())
    
    @classmethod
    def update(cls, id: uuid.UUID, data: BaseUpdate) -> models.Model:
        return cls.model.objects.filter(id=id).update(**data.model_dump(exclude_unset=True, exclude_none=True))
    
    @classmethod
    def delete(cls, id: uuid.UUID) -> bool:
        return cls.model.objects.filter(id=id).delete()
    
    