from Data.Persistance.database import *
from Data.Domain import User,Role
from flask_security import SQLAlchemySessionUserDatastore,Security

init_db()
user_datastore = SQLAlchemySessionUserDatastore(db_session,User.User,Role.Role)

db_session.commit()

#
# u = User("admin", "admin@localhost.com", "pass1234")
# db_session.add(u)
# db_session.commit()
