class Vacancy:
    """Класс для работы с платформами, реализован для создания нужных объектов"""
    def __init__(self, name: str, url: str, salary_to: int, salary_from: int, description: str):
        self.name = name
        self.url = url
        self.salary_to = salary_to
        self.salary_from = salary_from
        self.description = description

    def __str__(self) -> str:
        """Возвращает строковое представление объекта"""
        return f"Vacancy: {self.name}\nURL: {self.url}\nSalaryTo: {self.salary_to}\nSalaryFrom: {self.salary_from}\nDescription: {self.description}"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other) -> bool:
        """Позволяет реализовать проверку на равенство для экземпляров пользовательских типов"""
        return self.salary_to == other.salary

    def __lt__(self, other) -> bool:
        """Позволяет реализовать проверку на «меньше чем» для экземпляров пользовательских типов"""
        return self.salary_to < other.salary