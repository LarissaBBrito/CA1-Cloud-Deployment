import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from main import app, db

# Create a manager instance
manager = Manager(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Add the 'db' command to the manager
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    # Set a dummy database URL for local Alembic setup
    # This is not used for the actual migration, but Alembic needs a valid URL to initialize
    os.environ['DATABASE_URL'] = 'sqlite:///temp.db'
    manager.run()
