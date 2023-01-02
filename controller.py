import views
import model
from logger import log


@log
def start():
    views.greetings()
    while True:
        match views.show_menu():
            case 0:
                break
            case 1:
                views.show_people(model.get_people())
            case 2:
                data = views.show_create_data()
                model.create_data(data)
            case 3:
                views.show_people(model.get_people())
                number, item = views.show_upd_data()
                model.update_data(number, item)
            case 4:
                views.show_people(model.get_people())
                num = views.show_del_data()
                model.del_data(num)

