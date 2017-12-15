# action_network_1on1_tracker
A tracker of one-on-ones for Alinsky style organizations in Action Network.
Web project can be found in the folder titled "web"

## Installation
1. Clone repository: `git clone https://github.com/ryantimjohn/action_network_1on1_tracker.git`

2. Install & run MySQL:
  1. On Mac:
    1. `brew install mysql` (if not already installed)
    2. `mysql.server start`

3. Create virtual environment
  <ol type="a">
    <li>Install virtualenv: <code>pip install virtualenv</code></li>
    <li>Make a directory for virtual environment: <code>mkdir venv</code></li>
    <li>Create the virtual environment: <code>virtualenv venv</code></li>
    <li>Activate virtual environement: <code>source venv/bin/activate</code></li>
  </ol>
4. Install dependencies: `pip install -r requirements.txt`

5. Navigate to web project: `cd web`

6. Copy `.env` configuration: `cp .env.example .env` & update as
   necessary.

6. Setup Database
  <ol type="a">
    <li>Create a databse on your localhost (like `mysql -u root -e 'create database oneonone_dev' `)</li>
    <li>Edit database configuration in `.env`.</li>
    <li>Run Migration: <code>python manage.py migrate tracker</code> or <code>python manage.py migrate</code></li>
  </ol>

5. Create a super user  `python manage.py createsuperuser`

6. Run server: `python manage.py runserver`

N.B. To stop running virtual environment run `deactivate`
