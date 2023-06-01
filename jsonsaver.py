import json

from api_vac_comp import HeadHunterAPI, SuperJobAPI


class VacancyJSONWriter:
    """Класс позволяет сохранить вакансии """

    def __init__(self, filename: str):
        self.filename = filename

    def write_vacancies(self, vacancies):
        vacancy_data = []
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                vacancy_data = json.load(file)
        except FileNotFoundError:
            pass

        for vacancy in vacancies:
            vacancy_data.append({
                'name': vacancy.name,
                'url': vacancy.url,
                'description': vacancy.description,
                'salary_to': vacancy.salary_to,
                'salary_from': vacancy.salary_from
            })

        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(vacancy_data, file, ensure_ascii=False, indent=4)


headhunter = HeadHunterAPI()
vacancies = headhunter.get_vacancies()

if vacancies:
    writer = VacancyJSONWriter("all_vacancies.json")
    writer.write_vacancies(vacancies)
else:
    print("Не удалось получить данные о вакансиях с HeadHunter")

superjob = SuperJobAPI()
city = input("Введите город для поиска: ")
vacancies = superjob.get_vacancies(city)

if vacancies:
    writer = VacancyJSONWriter("all_vacancies.json")
    writer.write_vacancies(vacancies)
else:
    print("Не удалось получить данные о вакансиях с SuperJob")
