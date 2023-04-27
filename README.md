# Deshawn Django Dog-Walking
# Working thru Book 3
- https://github.com/nashville-software-school/bangazon-llc/tree/cohort-62/book-3-levelup

## Setup
```
mkdir -p ~/workspace/python/deshawn
cd ~/workspace/python/deshawn
pipenv shell
```
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/nashville-software-school/bangazon-llc/cohort-58/book-3-levelup/chapters/scripts/deshawn-setup.sh)"`

- open the Command Palette, and select "Python: Select Interpreter"

## ERD
- https://dbdiagram.io/d/644990cc6b319470514200da
<img width="700" alt="Django Deshawn Dog-Walking ERD" src="https://user-images.githubusercontent.com/114124374/234915412-4c021594-b696-4316-b56d-c200b9e66afa.png">

## Model Classes
- To create a `walker_id` foreign key field, you don't need to put `_id` in the class definition. Django does that for you.
- The `default` argument will automatically set the value to 0 when a new row is inserted, making it optional on creation.
-The `'Walker'` argument for the foreign key field is the name of the related class.

# Initialize the Migration for `deshawnapi` project
- RUN: `python3 manage.py makemigrations deshawnapi`
- OUTPUTS: `Migrations for 'deshawnapi':
  deshawnapi/migrations/0002_appointment.py
    - Create model Appointment`
- RUN: `python3 manage.py migrate`
- OUTPUTS: `Operations to perform:
  Apply all migrations: admin, auth, authtoken, contenttypes, deshawnapi, sessions
Running migrations:
  Applying deshawnapi.0002_appointment... OK`

## Object Relational Mapper Tools
- https://github.com/nashville-software-school/bangazon-llc/blob/cohort-62/book-3-levelup/chapters/DD_DJANGO_ORM.md 

# Serialization
- Serialization =	Serializers are a key component for working with data. They are used to convert complex data types, such as Django model instances, into Python datatypes (ie. lists and dictionaries) that can be easily rendered into JSON when sent as the view's Response data

# CREATE POST
- Now that you have a model, a view, a serializer, and the URL defining the route for appointments, the final step is to create an appointment or two and then get them.
