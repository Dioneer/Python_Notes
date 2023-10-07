import view
import text
import model

def search_contact():
	find = view.ask_find(text.search_request)
	result = model.search_function(find)
	view.show_notes(result, text.find_result(find))
	return result

def start():
	flag = True
	while flag:
		user_select = view.show_menu(text.main_menu)
		match user_select:
			case 1:
				model.open_file()
				view.print_msg(text.load_successfull)
			case 2:
				notes = model.your_notes
				view.show_notes(notes, text.empty_notes)
			case 3:
				model.save_file()
				view.print_msg(text.save_successfull)
			case 4:
				new_note = view.add_note(text.new_note)
				view.print_msg(text.added_successfull(new_note[1]))
				model.add_contact(new_note)
			case 5:
				search_contact()
			case 6:
				res = search_contact()
				if res!=[{}]:
					change_text = view.ask_change(text.change_note)
					model.change(res, change_text)
					view.print_msg(text.change_result)
				else:
					view.print_msg(text.search_notfind)
			case 7:
				res = search_contact()
				if res!=[{}]:
					model.delete_text(res)
					view.print_msg(text.delete_result)
				else:
					view.print_msg(text.search_notfind)
			case 8:
				if model.your_notes != model.original_notes:
					if view.ask_find(text.save_note) == "y":
						model.save_file()
						view.print_msg(text.save_successfull)
				view.print_msg(text.good_bay)
				return
			