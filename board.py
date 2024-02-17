import event
import user
import chat


class Board:
    def __init__(self):
        def download_from_server(self):
            pass

        #   if the jango server has saved the board
        #
        #   if 
        #       download_from_server()
        #   else
        self.events = []
        self.users = []
        self.private_chats = {}

    def upload_to_server(self):
            pass

    #   create methods
    def create_event(self, title, initiator_username, criteria, categories, total_people_required):
        self.events.append(Event(title, initiator_username, criteria, categories, total_people_required))

    def create_user(self, name, age, gender, description, hobbies, interests):
        self.users.append(User(name, age, gender, description, hobbies, interests))

    def create_private_chat(self, first_username, second_username):
        if first_username < second_username:
            first_username, second_username = second_username, first_username

        self.private_chats.append(PrivateChat(first_username, second_username))

    #   methods