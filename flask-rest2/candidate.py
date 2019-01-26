import uuid

class Candidate:
    id=None
    first_name=""
    last_name=""
    experience=[]

    def __init__(self,firts_name,last_name,experience=[]):
        self.id=uuid.uuid4()
        self.first_name=firts_name
        self.last_name=last_name
        self.experience=experience

    @property
    def id(self):
        return self.id


    @property
    def first_name(self):
        return self.first_name

    @first_name.setter
    def firts_name(self,firts_name):
        self.first_name=firts_name

    @property
    def last_name(self):
        return self.last_name

    @last_name.setter
    def last_name(self, last_name):
        self.last_name = last_name

    @property
    def experience(self):
        return self.last_name

    @experience.setter
    def experience(self, experience):
        self.experience = experience


    def serialice(self):
        return {
            "firt_name":self.firts_name,
            "last_name":self.last_name,
            "id":self.id,
            "experience":[exp.serialice() for exp in self.experience]
        }

    def add_experience(self,experiance):
        self.experience.append(experiance)