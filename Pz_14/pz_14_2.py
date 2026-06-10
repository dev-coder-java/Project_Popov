from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x600")
root.configure(bg="#f0f0f0")
root.title("Анализ улова рыбака")


Label(root, text="Анализ рыбной ловли",
      font=("Arial", 16, "bold"), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=(15, 5))

Label(root, text="Отметьте рыбу, которую поймал рыбак",
      font=("Arial", 10), bg="#f0f0f0").grid(row=1, column=0, columnspan=2, pady=(0, 15))

lake_fish = ['карп', 'щука', 'лещ', 'карась', 'окунь']

frame_lake = LabelFrame(root, text="Виды рыб в озере", font=("Arial", 10, "bold"), bg="#f0f0f0")
frame_lake.grid(row=2, column=0, columnspan=2, sticky="ew", padx=20, pady=5)
Label(frame_lake, text=", ".join(fish.capitalize() for fish in lake_fish),
      font=("Arial", 11), bg="#f0f0f0", fg="#333").grid(row=0, column=0, pady=10, padx=10)


fisherman_vars = {fish: BooleanVar() for fish in lake_fish}


frame_fisherman = LabelFrame(root, text="Улов рыбака", font=("Arial", 10, "bold"), bg="#f0f0f0")
frame_fisherman.grid(row=3, column=0, columnspan=2, sticky="ew", padx=20, pady=5)


for i, fish in enumerate(lake_fish):
    cb = Checkbutton(frame_fisherman, text=fish.capitalize(), variable=fisherman_vars[fish],
                     font=("Arial", 10), bg="#f0f0f0", activebackground="#f0f0f0")

    cb.grid(row=i // 3, column=i % 3, sticky="w", pady=8, padx=15)


initial_catch = {'карп', 'щука'}
for fish in initial_catch:
    if fish in fisherman_vars:
        fisherman_vars[fish].set(True)



def calculate_catch():

    caught = {fish for fish, var in fisherman_vars.items() if var.get()}

    uncaught = set(lake_fish) - caught

    def format_fish(fish_set):
        return ', '.join(fish.capitalize() for fish in sorted(fish_set)) if fish_set else 'ничего'

    res = "РЕЗУЛЬТАТЫ АНАЛИЗА\n\n"
    res += f"Рыбак поймал: {format_fish(caught)}\n"
    res += f"Всего поймано уникальных видов: {len(caught)}\n\n"
    res += f"НЕ поймано (осталось в озере): {len(uncaught)}\n"
    res += f"Список: {format_fish(uncaught) if uncaught else 'все виды выловлены'}"

    result_text.delete(1.0, END)
    result_text.insert(END, res)



Button(root, text="Рассчитать улов", bg="#4CAF50", fg="white",
       font=("Arial", 11, "bold"), command=calculate_catch,
       activebackground="#45a049", activeforeground="white").grid(row=4, column=0, columnspan=2, pady=15)


frame_result = LabelFrame(root, text="Результат", font=("Arial", 10, "bold"), bg="#f0f0f0")
frame_result.grid(row=5, column=0, columnspan=2, sticky="ew", padx=20, pady=5)

result_text = Text(frame_result, width=45, height=8, font=("Consolas", 10), bg="#ffffff", fg="#333333")
result_text.grid(row=0, column=0, pady=10, padx=10)


calculate_catch()


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

root.mainloop()