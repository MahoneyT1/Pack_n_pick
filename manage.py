from flask_script import Manager
from flask_migrate import MigrateCommand
from api.v1.app import app  # Import the Flask app

manager = Manager(app)

# Add the 'db' command to handle migrations
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
