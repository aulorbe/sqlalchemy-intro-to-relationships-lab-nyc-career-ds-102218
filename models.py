from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Role(Base): #child/children
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    character = Column(Text)
    actor_id = Column(Integer, ForeignKey('actors.id'))
    actors_ = relationship('Actor', back_populates='roles_')


class Actor(Base): #parent
    __tablename__= 'actors'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    roles_ = relationship(Role, order_by=Role.id ,back_populates='actors_') #could have Role as 'Role'



engine = create_engine('sqlite:///actors.db')
Base.metadata.create_all(engine)
