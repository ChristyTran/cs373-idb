#!/user/bin/env python3

from loader import app, db
from models import Artist, Track, Album
from flask_script import Manager, Shell, Server
import os



manager = Manager(app)

def make_shell_context():
    d = {
        'app': app,
        'db': db,
        'Artist': Artist,
        'Album': Album,
        'Track': Track
    }
    return d


@manager.command
def builddb():
    """ clear the database """

    decision = input('Think hard, are you sure you want to replace? Y/N: ')
    if decision.lower() == 'y':
        db.drop_all()
        db.configure_mappers()
        db.create_all()
        db.session.commit()
        print('Well now you\'ve done it...Dropped the tables and recreated the db')

@manager.command
def test():
    import subprocess
    output = subprocess.getoutput('python test.py')
    print(output)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("rundebug", Server(host='0.0.0.0', port="5000", use_debugger=True))
manager.add_command("runserver", Server(host='0.0.0.0', port="5000"))

if __name__ == "__main__":
    manager.run()

        




