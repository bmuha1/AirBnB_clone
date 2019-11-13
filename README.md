# Banu and Brent's Airbnb Clone: The Console

![Image of our Airbnb Logo](https://pbs.twimg.com/media/EJI6yBEWkAAZD4H?format=jpg&name=4096x4096)

Banu and Brent's Airbnb Clone: The Console is a command interpreter to manage our Airbnb objects. This is the first step towards building our first full web application: the Airbnb clone.

* We put in place a parent class (BaseModel) that takes care of initialization, serialization, and deserialization of our future instances.
* We create a simple flow of serialization and deserialization:<br>
Instance <-> Dictionary <-> JSON string <-> File
* We create all classes used for Airbnb: User, State, City, Place, Amenity, and Review.
* We create the first abstracted storage engine of the project: file storage.
* We create all the unittests to validate all our classes and storage engine.

## Requirements

### Python Scripts

* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the PEP 8 style (version 1.7 or more)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

### Python Unit Tests

* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the unittest module
* All your test files should be python files (extension: .py)
* All your test files and folders should start by test_
* Your file organization in the tests folder should be the same as your project
* e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
* e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
* All your tests should be executed by using this command: python3 -m unittest discover tests
* You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

## Usage

The shell should work like this in interactive mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) quit
$
```

The shell should work like this in non-interactive mode:

```bash
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
$
```

## Supported Commands
* create: Create a new instance of specified class, save it to the JSON file, and print the id
* show: Print the string representation of an instance based on the class name and id
* destroy: Delete an instance based on the class name and id
* all: Print the string representations of all instances based on the class name (or all classes if no class is specified)
* update: Update an instance based on the class name and id by adding or updating an attribute

## Examples

These examples show the commands with regular syntax.<br>

```bash
$ ./console.py
(hbnb) create BaseModel
249391b4-6348-4347-85d2-b01392975f37
(hbnb) show BaseModel 249391b4-6348-4347-85d2-b01392975f37
[BaseModel] (249391b4-6348-4347-85d2-b01392975f37) {'id': '249391b4-6348-4347-85d2-b01392975f37', 'created_at': datetime.datetime(2019, 11, 13, 22, 5, 42, 377621), 'updated_at': datetime.datetime(2019, 11, 13, 22, 5, 42, 378124)}
(hbnb) destroy BaseModel 249391b4-6348-4347-85d2-b01392975f37
(hbnb) show BaseModel 249391b4-6348-4347-85d2-b01392975f37
** no instance found **
(hbnb)
```

```bash
$ ./console.py
(hbnb) create User
45b62ec2-acb8-47dd-82c0-11012d9a343f
(hbnb) update User 45b62ec2-acb8-47dd-82c0-11012d9a343f name Banu
(hbnb) show User 45b62ec2-acb8-47dd-82c0-11012d9a343f
[User] (45b62ec2-acb8-47dd-82c0-11012d9a343f) {'id': '45b62ec2-acb8-47dd-82c0-11012d9a343f', 'name': 'Banu', 'created_at': datetime.datetime(2019, 11, 13, 22, 7, 49, 460358), 'updated_at': datetime.datetime(2019, 11, 13, 22, 7, 49, 460394)}
(hbnb)
```

These examples show the commands with "<class name>.<command>()" syntax.<br>

```bash
$ ./console.py
(hbnb) State.create()
88080931-ffc2-4352-b1c8-1d1bf8edcafd
(hbnb) State.update(88080931-ffc2-4352-b1c8-1d1bf8edcafd, name, California)
(hbnb) State.show(88080931-ffc2-4352-b1c8-1d1bf8edcafd)
[State] (88080931-ffc2-4352-b1c8-1d1bf8edcafd) {'updated_at': datetime.datetime(2019, 11, 13, 22, 26, 0, 582661), 'name': 'California', 'created_at': datetime.datetime(2019, 11, 13, 22, 26, 0, 582038), 'id': '88080931-ffc2-4352-b1c8-1d1bf8edcafd'}
(hbnb) City.create()
ad7128ed-59c6-4942-a4a1-a09100a872d9
(hbnb) City.update(ad7128ed-59c6-4942-a4a1-a09100a872d9, name, Oakland)
(hbnb) City.all()
["[City] (ad7128ed-59c6-4942-a4a1-a09100a872d9) {'updated_at': datetime.datetime(2019, 11, 13, 22, 26, 25, 790329), 'name': 'Oakland', 'created_at': datetime.datetime(2019, 11, 13, 22, 26, 25, 790286), 'id': 'ad7128ed-59c6-4942-a4a1-a09100a872d9'}"]
(hbnb)
```

```bash
$ ./console.py
(hbnb) Amenity.create()
cb8f7cac-4120-4b64-ba65-d7c7fda5a8ad
(hbnb) Place.create()
7743dd1f-2d14-4f87-a161-bc39bd4e42e1
(hbnb) Review.create()
000cd75c-6aa5-4b66-a91f-4c3883e57e67
(hbnb) all
["[Place] (7743dd1f-2d14-4f87-a161-bc39bd4e42e1) {'created_at': datetime.datetime(2019, 11, 13, 22, 29, 17, 20025), 'updated_at': datetime.datetime(2019, 11, 13, 22, 29, 17, 20081), 'id': '7743dd1f-2d14-4f87-a161-bc39bd4e42e1'}", "[Review] (000cd75c-6aa5-4b66-a91f-4c3883e57e67) {'created_at': datetime.datetime(2019, 11, 13, 22, 29, 21, 705391), 'updated_at': datetime.datetime(2019, 11, 13, 22, 29, 21, 705428), 'id': '000cd75c-6aa5-4b66-a91f-4c3883e57e67'}", "[Amenity] (cb8f7cac-4120-4b64-ba65-d7c7fda5a8ad) {'created_at': datetime.datetime(2019, 11, 13, 22, 29, 12, 226034), 'updated_at': datetime.datetime(2019, 11, 13, 22, 29, 12, 226391), 'id': 'cb8f7cac-4120-4b64-ba65-d7c7fda5a8ad'}"]
(hbnb) Amenity.destroy(cb8f7cac-4120-4b64-ba65-d7c7fda5a8ad)
(hbnb) Place.destroy(7743dd1f-2d14-4f87-a161-bc39bd4e42e1)
(hbnb) Review.destroy(000cd75c-6aa5-4b66-a91f-4c3883e57e67)
(hbnb) all
(hbnb)
```

## Authors

[Banu Sapakova](https://github.com/banuaksom)

[Brent Muha](https://github.com/bmuha1)