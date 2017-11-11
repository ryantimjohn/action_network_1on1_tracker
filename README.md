# action_network_1on1_tracker
A tracker of one-on-ones for Alinsky style organizations in Action Network. 
Web project can be found in the folder titled "web"

## Installation
1. Clone repository: `git clone https://github.com/ryantimjohn/action_network_1on1_tracker.git`

2. Create virtual environment
	<ol type="a">
		<li>Install virtualenv: <code>pip install virtualenv</code></li>
		<li>Make a directory for virtual environment: <code>mkdir venv</code></li>
		<li>Activate virtual environement: <code>source venv/bin/activate</code></li>
	</ol>
2. Install dependencies: `pip install -r requirements.txt`

3. Navigate to web project: `cd web`

4. Setup Database
	<ol type="a">
		<li>Create a databse on your localhost</li>
		<li>Edit database configuration in setting.py, modify DATABASES variable</li>
		<li>Run Migration: <code>python manage.py migrate tracker</code> or <code>python manage.py migrate</code></li>
	</ol>
	

4. Run server: `python manage.py runserver`

N.B. To stop running virtual environment run `deactivate`