# Adds @property for house
# while Java's Private setters can't be circumvented,
# Pythons's _.instanceVariable relies on suggestions


class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        # since we have an instance variable .house, 
        # Student can't also have a property attribute called .house
        # Python needs a way to distinguish the two
        self.house = house # calls property function .house()

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property # getter decorator
    def house(self):
        return self._house # instance variable is ._house

    # setter called whenever Student.house is assigned
    @house.setter # setter decorator
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house # instance variable is ._house


def main():
    student = get_student()
    # successful circumvention of the 4 allowed houses 
    student._house = "School of the Wolf"
    print(student)
    # failed circumvention of the 4 allowed houses 
    student.house = "Number Four, Privet Drive"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
