from sched.app import app, db

def create_tables():
    "Create relational database tables."
    db.create_all()

def drop_tables():
    "Drop all project relational database tables. THIS DELETES DATA."
    db.drop_all()

if __name__ == '__main__':
    db.create_all()
    manager.run()
