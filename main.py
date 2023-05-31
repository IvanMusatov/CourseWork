from api_vac_comp import HeadHunterAPI, SuperJobAPI
from func import get_sorted_vacancies, get_top_n_vacancies, get_vacancies_with_keywords
from jsonsaver import VacancyJSONWriter


def interact_with_user():
    print("Добро пожаловать в программу по поиску вакансий!")
    print("Выберите платформы для получения вакансий:")
    print("1. HeadHunter")
    print("2. SuperJob")
    platforms = []
    selected_platforms = input("Введите номера платформ (через запятую): ")
    for platform in selected_platforms.split(","):
        platform = platform.strip()
        if platform == "1":
            platforms.append("HeadHunter")
        elif platform == "2":
            platforms.append("SuperJob")

    writer = VacancyJSONWriter("all_vacancies.json")

    for platform in platforms:
        if platform == "HeadHunter":
            headhunter = HeadHunterAPI()
            vacancies = headhunter.get_vacancies()
            if vacancies:
                writer.write_vacancies(vacancies)
            else:
                print("Не удалось получить данные о вакансиях с HeadHunter")
        elif platform == "SuperJob":
            superjob = SuperJobAPI()
            vacancies = superjob.get_vacancies()
            if vacancies:
                writer.write_vacancies(vacancies)
            else:
                print("Не удалось получить данные о вакансиях с SuperJob")

    print("Данные о вакансиях успешно сохранены!")

    while True:
        print("\nМеню:")
        print("1. Получить топ N вакансий по зарплате")
        print("2. Получить вакансии в отсортированном виде")
        print("3. Получить вакансии с ключевыми словами в описании")
        print("4. Выход")
        choice = input("Введите номер действия: ")

        if choice == "1":
            n = int(input("Введите количество вакансий для вывода: "))
            top_vacancies = get_top_n_vacancies("all_vacancies.json", n)
            print(top_vacancies)
        elif choice == "2":
            sorted_vacancies = get_sorted_vacancies("all_vacancies.json")
            print(sorted_vacancies)
        elif choice == "3":
            keywords = input("Введите ключевые слова через запятую: ")
            vacancies_with_keywords = get_vacancies_with_keywords("all_vacancies.json", keywords)
            print(vacancies_with_keywords)
        else:
            print("Неправильный выбор. Попробуйте ещё раз.")


if __name__ == "__main__":
    interact_with_user()
