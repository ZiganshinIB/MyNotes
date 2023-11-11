from datetime import datetime

def save_note(title: str, body:str) -> bool:
    header = "__H__"
    sep='_!_SEP_!_'
    end='(*)END(*)'
    if title.startswith(header) or (sep in title) or (sep in body):
        return False
    with open("notes.txt", mode='a+', encoding="utf-8") as file:
        file.write(f"{header}{title}{sep}{body}{sep}{str(datetime.now())}{end}\n")
    return True



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
        case "get":
            #notes:list = get_notes()
            #print(notes)
        case "exit":
            break;




