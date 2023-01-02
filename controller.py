import view
from logger import log
import model


@log
def start():
    """Старт"""
    view.greatings()
    while True:
        match view.menu():
            case 0:
                break
            case 1:
                view.print_book(model.get_data())
            case 2:
                model.add_data(view.add_record())
            case 3:
                model.add_data(view.editor(model.get_data_id(view.request_id())))

