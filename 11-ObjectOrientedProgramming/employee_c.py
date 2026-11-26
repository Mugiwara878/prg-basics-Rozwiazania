class C:
    def __init__(self, first_name, last_name, age, seniority):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.seniority = seniority

    def __str__(self):
        result = f"{self.last_name}{self.first_name[0]}{self.seniority}"
        if self.age >= 18:
            return result.upper()
        else:
            return result.lower()