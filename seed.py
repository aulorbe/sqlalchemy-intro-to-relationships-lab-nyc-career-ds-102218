from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()


# Tom hanks instantiations
tom = Actor(name='Tom Hanks')

tom.roles_ = [Role(character='Forrest Gump'), Role(character='Jim Lovell'), Role(character='Woody'), Role(character='Robert Langdon')]



# Gwyneth Paltrow instantiations
gwyneth =  Actor(name='Gwyneth Paltrow')

gwyneth.roles_ = [Role(character='Pepper Potts'), Role(character='Margot Tenenbaum')]




# Cynthia Nixon instantiations
cynthia = Actor(name='Cynthia Nixon')

cynthia.roles_ = [Role(character='Miranda'), Role(character='Emily Dickenson')]


session.add_all([tom,gwyneth,cynthia])

session.commit()
