#!/bin/python

class Employee:
    def __init__(self, fname: str, lname: str, title: str, salary: float, UID=0):
        self.fname = fname
        self.lname = lname
        self.title = title
        self.salary = salary
        self.UID = UID

    def get_name(self) -> str:
        return f"{self.fname} {self.lname}"

    def get_title(self) -> str:
        return self.title

    def get_salary(self) -> float:
        return self.salary

    def set_title(self, title) -> None:
        self.title = title

    def set_salary(self, salary) -> None:
        self.salary = salary

class User(Employee):
    def __init__(self, fname, lname, title, salary, admin_status: bool):
        super().__init__(fname, lname, title, salary)
        self.admin_status = admin_status

    def is_admin(self):
        return self.admin_status

    def set_admin(self):
        self.admin_status = True

    def revoke_admin(self):
        self.admin_status = False

class Contractor(Employee):
    def __init__(self, fname, lname, title, salary, contract_length: float):
        super().__init__(fname, lname, title, salary)
        self.contract_length = contract_length

    def get_contract_length(self) -> int:
        return self.contract_length

    def set_contract_length(self, length) -> None:
        self.contract_length = length

    def get_contract_cost(self) -> float:
        return self.contract_length * self.salary


