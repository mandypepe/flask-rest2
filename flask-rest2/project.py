import uuid

class Projct:
    name=None
    start_date=None
    end_date=None
    id=None
    description=None
    def __init__(self,name,description,start_date,end_date):
        self.id=uuid.uuid4()
        self.name=name
        self.start_date=start_date
        self.end_date=end_date
        self.description=description

    @property
    def id(self):
        return self.id
    @id.setter
    def id(self,id):
        self.id=id

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self,name):
        self.name=name

    @property
    def start_date(self):
        self.start_date

    @start_date.setter
    def start_date(self,start_date):
        self.start_date=start_date

    @property
    def end_date(self):
        return self.end_date
    @end_date.setter
    def end_date(self,end_date):
        self.end_date=end_date

    @property
    def description(self):
        return self.description

    @description.setter
    def description(self,description):
        self.description=description

    def serialize(self):
        return {"name":self.name,
                "description":self.description,
                "id":self.id,
                "start_date":self.start_date,
                "end_date":self.end_date
                }








