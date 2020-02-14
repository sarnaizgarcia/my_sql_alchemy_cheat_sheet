
from db import (Base, Column, Integer,
                String, ForeignKey, session, engine)

### MODELS:

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name =  Column(String(50))
    password = Column(String(50))

    def save(self):
        session.add(self)
        session.commit()

    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter(cls.id == 1).first()
    
    def delete_user(self):
        session.delete(self)
        session.commit()

    def __repr__(self):
        return f'{self.__dict__}'

class Recipes(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    name =  Column(String(50))
    user_id = Column(ForeignKey('user.id'))

    def save(self):
        session.add(self)
        session.commit()