import datetime
import json


class Note:
    def __init__(self, id, title, body, timestamp):
        self.id = id
        self.title = title
        self.body = body
        self.timestamp = timestamp

class NoteManager:
    def __init__(self):
        self.notes = []

    def load_notes(self):
        try:
            with open('notes.json', 'r') as file:
                notes_data = json.load(file)
                self.notes = [Note(n['id'], n['title'], n['body'], n['timestamp']) for n in notes_data]
        except FileNotFoundError:
            self.notes = []

    def save_notes(self):
        notes_data = [{'id': note.id, 'title': note.title, 'body': note.body, 'timestamp': note.timestamp} for note in self.notes]
        with open('notes.json', 'w') as file:
            json.dump(notes_data, file)

    def create_note(self, title, body):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        note_id = len(self.notes) + 1
        note = Note(note_id, title, body, timestamp)
        self.notes.append(note)
        self.save_notes()

    def edit_note(self, note_id, new_title, new_body):
        for note in self.notes:
            if note.id == note_id:
                note.title = new_title
                note.body = new_body
                note.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_notes()
                return

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.id != note_id]
        self.save_notes()

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def get_all_notes(self):
        return self.notes

# Пример использования
note_manager = NoteManager()
note_manager.load_notes()

while True:
    print("1. Создать заметку")
    print("2. Редактировать заметку")
    print("3. Удалить заметку")
    print("4. Вывести список всех заметок")
    print("5. Вывести заметку по ID")
    print("6. Выйти")
    choice = input("Выберите действие: ")

    if choice == "1":
        title = input("Введите заголовок заметки: ")
        body = input("Введите текст заметки: ")
        note_manager.create_note(title, body)
        print("Заметка создана.")

    elif choice == "2":
        note_id = int(input("Введите ID заметки, которую хотите отредактировать: "))
        note = note_manager.get_note_by_id(note_id)
        if note:
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новый текст заметки: ")
            note_manager.edit_note(note_id, new_title, new_body)
            print("Заметка отредактирована.")
        else:
            print("Заметка с указанным ID не найдена.")

    elif choice == "3":
        note_id = int(input("Введите ID заметки, которую хотите удалить: "))
        note = note_manager.get_note_by_id(note_id)
        if note:
            note_manager.delete_note(note_id)
            print("Заметка удалена.")
        else:
            print("Заметка с указанным ID не найдена.")

    elif choice == "4":
        notes = note_manager.get_all_notes()
        if len(notes) > 0:
            for note in notes:
                print(f"ID: {note.id}, Заголовок: {note.title}, Дата/время создания: {note.timestamp}")
        else:
            print("Список заметок пуст.")

    elif choice == "5":
        note_id = int(input("Введите ID заметки, которую хотите вывести: "))
        note = note_manager.get_note_by_id(note_id)
        if note:
            print(f"ID: {note.id}, Заголовок: {note.title}, Текст: {note.body}, Дата/время создания: {note.timestamp}")
        else:
            print("Заметка с указанным ID не найдена.")

    elif choice == "6":
        break

    else:
        print("Неверный выбор. Попробуйте еще раз.")

    print()