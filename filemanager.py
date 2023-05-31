import abc
import json


class VacancyFileManager(abc.ABC):
    @abc.abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abc.abstractmethod
    def get_vacancies(self, criteria):
        pass

    @abc.abstractmethod
    def delete_vacancies(self, criteria):
        pass


class JsonVacancyFileManager(VacancyFileManager):
    def __init__(self, filename):
        self.filename = filename

    def add_vacancy(self, vacancy):
        with open(self.filename, 'a', encoding='utf-8') as file:
            json.dump(vacancy, file, ensure_ascii=False)
            file.write('\n')

    def get_vacancies(self, criteria):
        with open(self.filename, 'r', encoding='utf-8') as file:
            vacancies = []
            for line in file:
                vacancy = json.loads(line)
                if self.matches_criteria(vacancy, criteria):
                    vacancies.append(vacancy)
            return vacancies

    def delete_vacancies(self, criteria):
        with open(self.filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(self.filename, 'w', encoding='utf-8') as file:
            for line in lines:
                vacancy = json.loads(line)
                if not self.matches_criteria(vacancy, criteria):
                    file.write(line)

    def get_top_n_vacancies(self, filename, n):
        with open(filename, 'r', encoding='utf-8') as file:
            vacancies = json.load(file)

        sorted_vacancies = sorted(vacancies, key=lambda x: x['salary_from'], reverse=True)
        return sorted_vacancies[:n]

    @staticmethod
    def matches_criteria(vacancy, criteria):
        keywords = criteria.get('keywords', [])
        for keyword in keywords:
            if keyword.lower() in vacancy['description'].lower():
                return True
        return False
