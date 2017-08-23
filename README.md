StartupWeekendDO
-------------------
This project provides a CMS platform for the StartupWeekendDO page.

Requirements
---------------

Please ensure the following software is installed and running on your machine
before proceeding with installation:

- Python 3 (recommended)

Installation
---------------

1. Clone necessary repositories:

        git clone ssh://git@github.com:codemera/startupweekenddo.git

2. Create a virtualenv

        mkvirtualenv startupweekenddo

    or

        virtualenv startupweekendo

3. Install base dependencies:

        cd startupweekendo
        pip install -r requirements.txt  # If production

    or

        pip install -r deploy/local.txt  # If local

4. Copy the local_settings template to the proper location and modify to suit
   your environment. Remove debug toolbar for local repos.

        cd startupweekenddo/startupweekenddo
        cp local_settings.py.template local_settings.py

5. Run syncdb and apply migrations

        ./manage.py syncdb
        ./manage.py migrate

6. Install third-party assets:

        npm install
        bower install
        gulp

7. Load initial data

        ./manage.py loaddata startupweekenddo/fixtures/initial_data.json

Running
---------

    cd startupweekenddo
    ./manage.py run_server

Then navigate to [localhost](http://localhost:8000)
