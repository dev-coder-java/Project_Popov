#Приложение РАСПРЕДЕЛЕНИЕ ДОПОЛНИТЕЛЬНЫХ ОБЯЗАННОСТЕЙ для
#некоторой организации. БД должна содержать таблицу Обязанности со следующей
#структурой записи: ФИО работника, вид дополнительной работы, сумма оплаты, срок.
import sqlite3 as sq
from data import abiturients_data

with sq.connect('duties.db') as con:
    cursor = con.cursor()

    cursor.execute("DROP TABLE IF EXISTS Обязанности")
    cursor.execute("""CREATE TABLE IF NOT EXISTS Обязанности (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fio TEXT NOT NULL,
        work_type TEXT NOT NULL,
        payment REAL NOT NULL,
        deadline TEXT NOT NULL
    )""")

    cursor.executemany("INSERT INTO Обязанности VALUES (NULL, ?, ?, ?, ?)", abiturients_data)

    def print_table(title_text):
        print('\n', title_text)
        print(f"{'ID':<4} {'ФИО работника':<25} {'Вид работы':<35} {'Оплата':<10} {'Срок'}")
        cursor.execute("SELECT * FROM Обязанности ORDER BY id")
        for row in cursor.fetchall():
            id_, fio, work, pay, dead = row
            print(f"{id_:<4} {fio:<25} {work:<35} {pay:<10.2f} {dead}")

    print_table("Исходное содержимое таблицы Обязанности")

    print("\n 1. Работники с оплатой более 10000:")
    cursor.execute("SELECT fio, work_type, payment FROM Обязанности WHERE payment > 10000")
    for row in cursor.fetchall():
        print(f" - {row[0]} ({row[1]}) - {row[2]:.2f} руб.")

    print("\n 2. Работники со сроком выполнения в 2027 году:")
    cursor.execute("SELECT fio, deadline FROM Обязанности WHERE deadline LIKE '2027%'")
    for row in cursor.fetchall():
        print(f" - {row[0]} (Срок: {row[1]})")

    print("\n 3. Работники, чья работа связана с IT или порталом:")
    cursor.execute("SELECT fio, work_type FROM Обязанности WHERE work_type LIKE '%IT%' OR work_type LIKE '%портал%'")
    for row in cursor.fetchall():
        print(f" - {row[0]} ({row[1]})")

    cursor.execute("UPDATE Обязанности SET payment = 15000.00 WHERE work_type = 'Мониторинг IT-оборудования'")
    cursor.execute("UPDATE Обязанности SET deadline = '2027-06-01' WHERE fio LIKE '%Иванов%'")
    cursor.execute("UPDATE Обязанности SET work_type = 'Координация логистики и склада' WHERE fio LIKE '%Федорова%'")

    print_table("Таблица после проведения 3-х операций редактирования")

    cursor.execute("DELETE FROM Обязанности WHERE fio LIKE '%Морозов%'")
    cursor.execute("DELETE FROM Обязанности WHERE id = 8")
    cursor.execute("DELETE FROM Обязанности WHERE payment <= 5000.00")

    print_table("Итоговая таблица после проведения 3-х операций удаления")