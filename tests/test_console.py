#!/usr/bin/python3
""" Test for Console """
import unittest
import os.path
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """ Test for Console """

    def setUp(self):
        """ Move json file if it exists """
        if os.path.isfile("file.json"):
            os.rename("file.json", "file.json.temp")

    def tearDown(self):
        """ Delete test json file and put original file back """
        if os.path.isfile("file.json.temp"):
            os.rename("file.json.temp", "file.json")

    def test_create(self):
        """ Test create """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(type(f), str)
            self.assertEqual(len(f.getvalue().strip()), 36)
            id = f.getvalue().strip()

    def test_show(self):
        """ Test show """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel" + str(id))
            self.assertTrue(type(f), str)
            self.assertEqual(len(f.getvalue().strip()), 25)

    def test_newline_spaces(self):
        """ Test newline and spaces input """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(" ")
            self.assertEqual(f.getvalue().strip(), "")

    def test_fake_command(self):
        """ Test commands that do not exist """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("garbage")
            self.assertEqual(f.getvalue().strip(),
                             "*** Unknown syntax: garbage")

    def test_help(self):
        """ Test help """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertEqual(f.getvalue().strip(),
                             "Documented commands (type help <topic>):" +
                             "\n========================================" +
                             "\nEOF  all  count  create  destroy  help  " +
                             "quit  show  update")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(f.getvalue().strip(), "EOF to exit the program")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(f.getvalue().strip(), "Print all instances.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
            self.assertEqual(f.getvalue().strip(),
                             "Counts the number of objects.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(f.getvalue().strip(),
                             "Create a new instance of BaseModel.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(f.getvalue().strip(),
                             "Delete an instance based on class name and id.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help help")
            self.assertEqual(f.getvalue().strip(), "List available " +
                             "commands with \"help\" or detailed help " +
                             "with \"help cmd\".")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(f.getvalue().strip(),
                             "Quit to exit the program")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(f.getvalue().strip(),
                             "Print an instance based on class name and id.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertEqual(f.getvalue().strip(),
                             "Update an instance based on class name and id.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help garbage")
            self.assertEqual(f.getvalue().strip(),
                             "*** No help on garbage")

if __name__ == '__main__':
    unittest.main()
