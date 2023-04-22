# Employee class

class Employee:
    def __init__(self, name, id, department, job):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__job = job

    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def set_department(self, department):
        self.__department = department

    def set_job(self, job):
        self.__job = job

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_department(self):
        return self.__department

    def get_job(self):
        return self.__job
