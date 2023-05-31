import json


def get_top_n_vacancies(filename, n):
    with open(filename, 'r', encoding='utf-8') as file:
        vacancies = json.load(file)

    sorted_vacancies = sorted(vacancies, key=lambda x: x.get('salary_from', 0) or 0, reverse=True)
    filtered_vacancies = [v for v in sorted_vacancies if v.get('salary_from') is not None and v.get('salary_from') > 0]

    return filtered_vacancies[:n]


def get_sorted_vacancies(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        vacancies = json.load(file)

    sorted_vacancies = sorted(vacancies, key=lambda x: x['name'])
    return sorted_vacancies


def get_vacancies_with_keywords(filename, keywords):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    filtered_vacancies = []
    for vacancy in data:
        description = vacancy.get('description')
        if description:
            description = description.lower()
            for keyword in keywords:
                if keyword.lower() in description:
                    filtered_vacancies.append(vacancy)
                    break

    return filtered_vacancies
