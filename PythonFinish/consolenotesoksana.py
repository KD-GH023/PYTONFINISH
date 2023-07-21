import json
import os
import datetime

NOTES_FILE = "notes.json"


def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    return []


def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)


def add_note(title, msg):
    notes = load_notes()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "msg": msg,
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": None,
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")


def list_notes(filter_date=None):
    notes = load_notes()
    if filter_date:
        notes = [note for note in notes if note["created_at"].startswith(filter_date)]

    if not notes:
        print("Заметки не найдены.")
    else:
        for note in notes:
            print(f"{note['id']}: {note['title']}")
            print(note["msg"])
            print(f"Создано: {note['created_at']}")
            if note["updated_at"]:
                print(f"Обновлено: {note['updated_at']}")
            print("-" * 20)


def edit_note(note_id, title, msg):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = title
            note["msg"] = msg
            note["updated_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break
    else:
        print("Заметка с указанным идентификатором не найдена.")
        return

    save_notes(notes)
    print("Заметка успешно отредактирована.")


def delete_note(note_id):
    notes = load_notes()
    notes = [note for note in notes if note["id"] != note_id]
    if len(notes) == len(load_notes()):
        print("Заметка с указанным идентификатором не найдена.")
        return

    save_notes(notes)
    print("Заметка успешно удалена.")


def help_info():
    print("Доступные команды:")
    print("add - Добавить новую заметку")
    print("list - Показать список заметок (можно указать дату для фильтрации)")
    print("edit - Редактировать заметку по идентификатору")
    print("delete - Удалить заметку по идентификатору")
    print("help - Показать список команд")


def main():
    help_info()

    while True:
        print("Введите команду:")
        command = input().strip().lower()

        if command == "add":
            title = input("Введите заголовок заметки: ")
            msg = input("Введите тело заметки: ")
            add_note(title, msg)

        elif command == "list":
            filter_date = input("Введите дату (гггг-мм-дд) для фильтрации или нажмите Enter для вывода всех заметок: ")
            list_notes(filter_date)

        elif command == "edit":
            note_id = int(input("Введите идентификатор заметки, которую хотите отредактировать: "))
            title = input("Введите новый заголовок заметки: ")
            msg = input("Введите новое тело заметки: ")
            edit_note(note_id, title, msg)

        elif command == "delete":
            note_id = int(input("Введите идентификатор заметки, которую хотите удалить: "))
            delete_note(note_id)

        elif command == "help":
            help_info()

        elif command == "exit":
            break

        else:
            print("Неверная команда.")


if __name__ == "__main__":
    main()
