main_menu = [
	"Меню:",
	"Загрузить заметки",
	"Показать заметки",
	"Сохранить заметки",
	"Добавить заметку",
	"Найти заметку",
	"Редактировать заметку",
	"Удалить заметку",
	"Выход",
]
menu_error = f'Ошибка ввода! Ведите число от 1 до {len(main_menu)-1}. Попробуйте еще раз ввести число.'
empty_notes = f'Список заметок пуст или не открыт'
load_successfull= f'Заметки загружены'
new_note = ["Введите заголовок: ",
              "Введите сообщение: "]
save_successfull = f"Файл успешно сохранен"
search_request = "Что искать(заголовок или часть сообщения)?"
search_notfind = "Запрашиваемый объект не найден"
change_note = ["Введите новый заголовок (или Enter - оставить без изменений): ",
                  "Введите новое сообщение (или Enter - оставить без изменений): "]
change_result = f"Заметка успешно изменена"

delete_note = 'Введите введите заголовок или часть текста заметки, которую хотите удалить: '
save_note = "У вас есть несохраненные изменения. Сохранить? (y/n): "
delete_result = f'Заметка успешно удалена'
good_bay = "До свидания!"


def added_successfull(name: str) -> str:
    title = name.get("title")
    return f"Заметка {str(title)} успешно создана"


def find_result(res: str) -> str:
    return f'Заметки, содержащие {res} не найдены'
