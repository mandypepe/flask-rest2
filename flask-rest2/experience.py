class Experince:
    domain=None
    years=None
    projects=None

    def __init__(self,domain,years,projects=[]):
        self.domain=domain
        self.years=years
        self.projects

    @property
    def domain(self):
        return self.domain

    @domain.setter
    def domain(self,domain):
        self.domain=domain

    @property
    def years(self):
        return self.years

    @years.setter
    def years(self,years):
        self.years=years

    @property
    def projects(self):
        return self.projects

    @projects.setter
    def projects(self,value):
        self.projects=value


    def serialice(self):
        return {
            "domanin":self.domain,
            "projects": [pjr.serialice for pjr in self.projects]
        }
