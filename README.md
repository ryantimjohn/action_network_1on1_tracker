# action_network_1on1_tracker
A tracker of one-on-ones for Alinsky style organizations in Action Network.
Web project can be found in the folder titled "web"

## Installation
1. Clone repository: `git clone https://github.com/ryantimjohn/action_network_1on1_tracker.git`

2. Install & run MySQL:
  1. On Mac:
    1. `brew install postgresql` (if not already installed)
    2. `pg_ctl -D /usr/local/var/postgres start`

3. Create virtual environment
  <ol type="a">
    <li>Install pipenv: <code>pip install pipenv</code></li>
    <li>
      Install dependencies:
      <code>
        pipenv install --ignore-pipfile
      </code>
    </li>
  </ol>

4. Navigate to web project: `cd web`

5. Copy `.env` configuration: `cp .env.example .env` & update as
   necessary.

6. Setup Database
  <ol type="a">
    <li>Activate a postgres shell: `psql postres`</li>
    <li>Create a ROLE: `CREATE ROLE <username> WITH LOGIN PASSWORD 'password string'`</li>
    <li>Allow user to create databases: `ALTER ROLE <username> CREATEDB;`</li>
    <li>Quite shell: `\q`</li>
    <li>Create a database with the ROLE you just created: `createdb <db_name> -U <username>`</li>
    <li>Edit database configuration in `.env` to include the db name,
username & password.</li>
    <li>Run Migration: <code>pipenv run python manage.py migrate tracker</code> or <code>python manage.py migrate</code></li>
  </ol>

5. Create a super user  `pipenv run python manage.py createsuperuser`

6. Run server: `pipenv run python manage.py runserver`

