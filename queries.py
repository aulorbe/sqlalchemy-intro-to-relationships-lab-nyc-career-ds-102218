from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()


def return_gwyneth_paltrows_roles():
# should return the list of Gwyneth Paltrow's Role instances

    gwyn = session.query(Actor).filter(Actor.name=='Gwyneth Paltrow').first()

    return gwyn.roles_
    # could do gwyn.roles_.character to see the actual characters she played


def return_tom_hanks_2nd_role():
# should return the Tom Hanks' second Role instance
    tom = session.query(Actor).filter_by(name='Tom Hanks').first()

    return tom.roles_[1]
