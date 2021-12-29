from typing import Optional, List, Union
from datetime import datetime
from uuid import UUID


from pydantic import BaseModel
from pydantic.networks import EmailStr

from .question import Question
    
# Shared properties
class DeckBase(BaseModel):
    uuid: UUID    

# Shared properties
class DeckSimplified(DeckBase):

    class Config:
        orm_mode = True


# Properties to receive on deck creation
class DeckCreate(DeckBase):
    owner_uuid: Union[UUID, None]
    # honeypot
    name: str
    email: Optional[str]



# Properties to receive on deck update
class DeckUpdate(DeckBase):
    pass


# Properties shared by models stored in DB
class DeckInDBBase(DeckBase):
    id: int
    owner_uuid: Optional[UUID] = None
    date_added: Optional[datetime]

# Properties to return to client
class Deck(DeckBase):
    questions: List[Question]
    owner_uuid: Optional[UUID]
    date_added: Optional[datetime]

    class Config:
        orm_mode = True


# Properties properties stored in DB
class DeckInDB(DeckInDBBase):
    pass

class DeckDBDump(DeckInDBBase):
    pass
