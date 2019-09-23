import os
from dotenv import load_dotenv
from lib.app import app

project_folder = os.getcwd()
load_dotenv(os.path.join(project_folder, '.env'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')