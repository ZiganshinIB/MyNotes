from datetime import datetime
header = "__H__"
sep = '_!_SEP_!_'
end = '(*)END(*)'


def save_note(title: str, body: str) -> bool:
    if title.startswith(header) or (sep in title) or (sep in body):
        return False
    with open("notes.txt", mode='a+', encoding="utf-8") as file:
        file.write(f"{header}{title}{sep}{body}{sep}{str(datetime.now())}{end}\n")
    return True


def get_notes():
    notes = []
    cash = ""
    with open("notes.txt", mode='r', encoding="utf-8") as file:
        for line in file.readlines():
            cash += line
            if cash.endswith(end+'\n'):
                if cash.startswith(header):
                    title, body, date_str = (cash[len(header):-(len(end)+1)].split(sep))
                    notes.append({"title": title, 'body': body, 'date': date_str})
                    cash = ""
            else:
                cash += "\n"
                continue
    return notes


def get_notes_date(date_str: str):
    target_date = datetime.strptime(date_str, '%Y-%m-%d')
    notes = []
    cash = ""
    with open("notes.txt", mode='r', encoding="utf-8") as file:
        for line in file.readlines():
            cash += line
            if cash.endswith(end + '\n'):
                if cash.startswith(header):
                    title, body, current_date = (cash[len(header):-(len(end) + 1)].split(sep))
                    if target_date.date() == datetime.strptime(current_date, "%Y-%m-%d %H:%M:%S.%f").date():
                        notes.append({"title": title, 'body': body, 'date': date_str})
                    cash = ""
            else:
                cash += "\n"
                continue
    return notes


while True:
    command = input("Введите команду: ")

    match command:
        case "add":
            title_note = input("Введите заголовок заметки: ")
            body_note = input("Введите тело заметки: ")
            flag: bool = save_note(title_note, body_note)
            if flag:
                print("Заметка успешно сохранена")
            else:
                print("Возникли ошибки ")
        case "get_all":
            notes: list = get_notes()
            for note in notes:
                print(note)
        case "date":
            date = input("Введите Дату в формате %Y-%m-%d: ")
            notes: list = get_notes_date(date)
            for note in notes:
                print(note)
        case "exit":
            break
