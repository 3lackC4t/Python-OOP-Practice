#!/bin/python

class Employee:
    def __init__(self, fname, lname, title, salary):
        self.fname = fname
        self.lname = lname
        self.title = title
        self.salary = salary

    def get_name(self):


class User(Employee):
    def __init__(self, fname, lname, title, salary, admin_status):
        pass

class Contractor(Employee):
    def __init__(self, fname, lname, title, salary, contract_length):
        pass
