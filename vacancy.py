class Vacancy:
    def __init__(self, name, url, salary_to, salary_from, description):
        self.name = name
        self.url = url
        self.salary_avg = salary_to + salary_from / 2
        self.description = description

    def __str__(self):
        """Возвращает строковое представление объекта"""
        return f"Vacancy: {self.name}\nURL: {self.url}\nSalary: {self.salary_avg}\nDescription: {self.description}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        """Позволяет реализовать проверку на равенство для экземпляров пользовательских типов"""
        return self.salary_avg == other.salary

    def __lt__(self, other):
        """Позволяет реализовать проверку на «меньше чем» для экземпляров пользовательских типов"""
        return self.salary_avg < other.salary
