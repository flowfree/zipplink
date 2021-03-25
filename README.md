ZippLink
--------
My personal URL shortener service - https://zipp.link


Requirements
------------
- Python 3.8+
- [Pipenv](https://pipenv.pypa.io)


Installation on local machine
-----------------------------
1.  Clone this repository.

2.  Install Django and other dependencies:

        pipenv install --dev

3.  Create a new file named `.env` in the project's root directory. You need to specify the `SECRET_KEY` var:

        SECRET_KEY=<some random string>

    You can leave the `DB_*` variables empty since it will use sqlite3 on development machine.

4.  Run database migration:

        pipenv run ./manage.py migrate

5.  Run the development server:

        pipenv run ./manage.py runserver 3000

    Then open `http://localhost:3000` using your browser.


Sample Deployment to AWS
------------------------
You might want to deploy and run this application on production. This section will explain sample deployment to AWS 
Lambda using [Zappa](https://github.com/zappa/Zappa).

1.  Make sure you have successfully run the application on your local machine.

2.  Open the `config/settings/production.py` file and modify the following settings to match with your domain:

        ALLOWED_HOSTS = ['<your domain name>']
        ...
        URL_SHORTENER_PREFIX = '<your domain name>'

3.  Create a new PostgreSQL instance on Amazon RDS and fill in the `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, and 
    `DB_PASSWORD` in the `.env` file.

4.  Run the initial Zappa setup:

        pipenv run zappa init

    It will create the `zappa_settings.json` file. You need to set the `django_settings` field to `config.settings.production`. In addition to this, you might want to adjust the other values to suit with your needs as well. 
    Here is a sample configuration setup:

        {
            "prod": {
                "aws_region": "us-west-2",
                "django_settings": "config.settings.production",
                "profile_name": "default",
                "project_name": "myurlshortener",
                "runtime": "python3.8",
                "s3_bucket": "myurlshortener",
            }
        }

5.  Deploy to AWS:

        pipenv run zappa deploy prod

    If everything is okay, it will display the URL of the application. 

6.  Run the database migration:

        pipenv run zappa manage prod migrate

7.  Open your application's URL using your browser.


For more information about Zappa, please consult with [the documentation](https://github.com/zappa/Zappa).


Run the unit tests
------------------
Type the command below to run the unit tests:

    pipenv run pytest
