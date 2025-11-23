import sqlite3
import webbrowser
def init_db():
    conn = sqlite3.connect('lessons.db')
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        module_name TEXT,
        title TEXT,
        url TEXT
    )
    """)
    conn.commit()
    conn.close()

def add_video():
    module = input("Введите название модуля (Module1 / Module2 / Module3): ")
    title = input("Введите название видео")
    url = input("Введите ссылку на Youtube")

    conn = sqlite3.connect("lessons.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO videos (module_name, title, url) VALUES (?, ?, ?)",
        (module, title, url))
    
    conn.commit()
    conn.close()

    print("\n Ваше видео успешно добавлено!\n")

def show_module_videos():
    module = input("Введите модуль (Module1 / Module2 / Module3): ")

    conn = sqlite3.connect("lessons.db")
    cur = conn.cursor()

    cur.execute("SELECT id, title, FROM videos WHERE module_name = ?", (module,))
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("\nВ этом модуле пока нет ссылок\n")
        return
    
    print(f"\nВидео из {module}: \n")
    for row in rows:
        print(f"{row[0]}. {row[1]}")
    video_id = int(input('\nВведите ID видео, которое хотите открыть:'))
    open_video(video_id)
def open_video(video_id):
    conn = sqlite3.connect("lessons.db")
    cur = conn.cursor()

    cur.execute("SELECT url FROM videos WHERE id = ?", (video_id,))
    video = cur.fetchone()
    conn.close()

    if video:
        link = video[0]
        print('\nОткрываю ссылку...\n')
        webbrowser.open(link)
    
    else:
        print('Видео не найдено')

def main():
    init_db()

    while True:
        print("""
===============
    УРОК-БОТ (консоль)
===============
1. Добавить ссылку (админ)
2. Выбрать модуль и открыть видео
3. Выйти
""")
        
        choice = input('Ваш выбор:')

        if choice == "1":
            add_video()
        elif choice == "2":
            show_module_videos()
        elif choice == "3":
            print("Выход...")
            break
        else:
            print("Неверный выбор, попробуйте снова")

if __name__ == "__main__":
    main()
