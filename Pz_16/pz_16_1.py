#Создайте класс «Календарь», который имеет атрибуты год, месяц и день. Добавьте
#методы для определения дня недели, проверки на високосный год и определения
#количества дней в месяце.
import calendar
import datetime


class Calendar:
    def __init__(self, year, month, day):
        try:
            datetime.date(year, month, day)
            self.year = year
            self.month = month
            self.day = day
        except ValueError:
            print(f"{day}.{month}.{year} — такой даты не существует!")

    def is_leap_year(self):
        return calendar.isleap(self.year)

    def get_days_in_month(self):
        return calendar.monthrange(self.year, self.month)[1]

    def get_day_of_week(self):
        days_ru = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        date_obj = datetime.date(self.year, self.month, self.day)
        return days_ru[date_obj.weekday()]


def main():
    print("ДОБРО ПОЖАЛОВАТЬ В КАЛЕНДАРЬ")
    print("Формат ввода: ГОД МЕСЯЦ ДЕНЬ (через пробел)")
    print("Пример: 2024 2 29")

    while True:
        user_input = input("Введите дату: ").strip()

        if user_input.lower() in ['выход', 'exit', 'q']:
            print("Завершение работы. До свидания!")
            break

        parts = user_input.split()

        if len(parts) != 3:
            print("Ошибка: Нужно ввести ровно три числа через пробел (Год Месяц День).\n")
            continue

        try:
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])

            cal = Calendar(year, month, day)

            print(f" Проверенная дата : {cal.day:02d}.{cal.month:02d}.{cal.year}")
            print(f"️ День недели      : {cal.get_day_of_week()}")
            print(f" Високосный год   : {'Да' if cal.is_leap_year() else 'Нет'}")
            print(f" Дней в месяце    : {cal.get_days_in_month()}")

        except ValueError as e:
            error_msg = str(e)
            if "не существует" in error_msg:
                print(f"Ошибка даты: {error_msg}\n")
            else:
                print("Ошибка ввода: Пожалуйста, используйте только целые числа.\n")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}\n")



if __name__ == "__main__":
    main()