# Banu and Brent's Airbnb Clone: The Console

![Image of our Airbnb Logo](https://pbs.twimg.com/media/EJI6yBEWkAAZD4H?format=jpg&name=4096x4096)

Banu and Brent's Airbnb Clone: The Console is a command interpreter to manage our Airbnb objects. This is the first step towards building our first full web application: the Airbnb clone.

We put in place a parent class (BaseModel) that takes care of initialization, serialization, and deserialization of our future instances.

We create a simple flow of serialization and deserialization:<br>
Instance <-> Dictionary <-> JSON string <-> File

We create all classes used for Airbnb: User, State, City, Place, Amenity, and Review.

We create the first abstracted storage engine of the project: file storage.

We create all the unittests to validate all our classes and storage engine.
