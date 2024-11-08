import os.path

# Получение текущего рабочего каталога
current_dir = os.getcwd()
print("Текущий рабочий каталог:", current_dir)

# Получение списка файлов и директорий в текущем рабочем каталоге
files = os.listdir(current_dir)
print("Список файлов и директорий:", files)

# Получение абсолютного пути к текущему рабочему каталогу
abs_path = os.path.abspath(current_dir)
print("Абсолютный путь к текущему рабочему каталогу:", abs_path)

# Создание относительного пути к директории "data"
relative_path = "data"

# Объединение текущего рабочего каталога и относительного пути
full_path = os.path.join(current_dir, relative_path)
print("Полный путь к директории \"data\":", full_path)

# Проверка существования директории "data"
if os.path.exists(full_path):
    print("Директория \"data\" существует.")
    # Получение списка файлов и директорий в директории "data"
    data_files = os.listdir(full_path)
    print("Список файлов и директорий в директории \"data\":", data_files)
else:
    print("Директория \"data\" не существует.")
