import os
from abc import ABC, abstractmethod

import requests

from vacancy import Vacancy


class ApiVacComp(ABC):
    """Позволяет конкретизировать метод получения вакансии для каждого сайта отдельно"""
    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(ApiVacComp):
    """Получаем данные с сайта hh.ru"""

    def get_vacancies(self):

        url = 'https://api.hh.ru/vacancies'
        params = {'area': 1, 'text': 'python',
                  'per_page': 10}

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            vac = []
            for el in data['items']:
                salary = el.get('salary', {})
                vac.append(
                    Vacancy(
                        name=el['name'],
                        url=el['url'],
                        description=el['snippet']['requirement'],
                        salary_to=salary.get('to') if salary is not None else None,
                        salary_from=salary.get('from') if salary is not None else None
                    )
                )
            return vac
        else:
            print('Ошибка при запросе данных о вакансиях')
            return None


class SuperJobAPI(ApiVacComp):
    """Получаем данные с сайта superjob.ru"""

    def get_vacancies(self, city):
        api_key: str = os.getenv('JOB_API')
        api_url = "https://api.superjob.ru/2.0/vacancies/"
        headers = {'X-Api-App-Id': api_key}
        params = {'keyword': 'python', 'town': city}
        response = requests.get(api_url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            vac = []
            for el in data['objects']:
                try:
                    vac.append(
                        Vacancy(
                            name=el['profession'],
                            url=el['client']['link'],
                            description=el['vacancyRichText'],
                            salary_to=el['payment_to'],
                            salary_from=el['payment_from']
                        )
                    )
                except KeyError:
                    continue
            return vac
        else:
            print('Ошибка при запросе данных о вакансиях')
            return None
