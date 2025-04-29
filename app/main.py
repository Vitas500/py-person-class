class Person:
    people = {}

    def __init__(self,  name: str, age: int):
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    result_list = []
    for person in people:
        result_list.append(Person(person["name"], person["age"]))

    for person in people:
        if "wife" in person and person["wife"]:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"]:
            Person.people[person["name"]].husband = Person.people[person["husband"]]

    return result_list
