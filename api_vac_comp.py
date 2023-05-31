from abc import ABC, abstractmethod
import os
import requests

from vacancy import Vacancy


class ApiVacComp(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunter(ApiVacComp):

    def get_vacancies(self):
        url = 'https://api.hh.ru/vacancies'
        params = {'area': 1, 'text': 'python',
                  'per_page': 10}

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            vac = []
            for el in data['items']:
                vac.append(
                    Vacancy(
                        name=el['name'],
                        url=el['url'],
                        description=el['snippet']['requirement'],
                        salary_to=el['salary']['to'],
                        salary_from=el['salary']['from']
                    )
                )
            return vac
        else:
            print('Ошибка при запросе данных о вакансиях')
            return None


class SuperJob(ApiVacComp):

    def get_vacancies(self):
        api_key: str = os.getenv('JOB_API')
        api_url = "https://api.superjob.ru/2.0/vacancies/"
        headers = {
            "X-Api-App-Id": api_key
        }
        params = {'area': 1, 'text': 'python',
                  'per_page': 10}
        response = requests.get(api_url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            vac = []
            for el in data['items']:
                vac.append(
                    Vacancy(
                        name=el['profession'],
                        url=el['client']['url'],
                        description=el['vacancyRichText'],
                        salary_to=el['payment_to'],
                        salary_from=el['payment_from']
                    )
                )
            return vac
        else:
            print('Ошибка при запросе данных о вакансиях')
            return None
