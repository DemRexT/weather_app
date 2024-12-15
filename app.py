import tkinter as tk
from request_weather import get_weather

# Создаем основное окно
root = tk.Tk()

# Устанавливаем иконку
# icon = tk.PhotoImage(file="image/main.png")
# root.iconphoto(True, icon)

# Устанавливаем размер окна
root.geometry("500x400")


# Функция для получения погоды
def weather():
    data = city.get()
    result_weather = get_weather(data)
    result.config(text=result_weather)

# Устанавливаем заголовок окна
root.title("Погода")

# Контейнер для выравнивания всех элементов по центру
frame = tk.Frame(root, bg="lightblue")
frame.pack(fill="both", expand=True)

# Создаем и выравниваем метку с вопросом
label = tk.Label(frame, text="В каком городе хотите узнать погоду?", bg="lightblue", font=("Arial", 14))
label.pack(pady=10)  # Отступ сверху и снизу

# Создаем поле для ввода данных (Entry)
city = tk.Entry(frame, font=("Arial", 14))
city.pack(pady=10)

# Создаем кнопку
button = tk.Button(frame, text="Узнать погоду", command=weather, font=("Arial", 14))
button.pack(pady=10)

# Создаем метку для отображения результата
result = tk.Label(frame, text="", bg="lightblue", font=("Arial", 14))
result.pack(pady=10)



# Запускаем главный цикл приложения
root.mainloop()
