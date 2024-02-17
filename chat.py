

class Message:
    def __init__(self, username, message):
        self.__username = username
        self.__message = message

        self.__is_edited = False

    #  getters
    def username(self):
        return self.__username

    def message(self):
        return self.__message

    def is_edited(self):
        return self.__is_edited

    #  methods
    def edit_message(self, new_message):
        self.__message = new_message

        self.__is_edited = True


class Chat:
    def __init__(self):
        self.__message_count = 0

        self.__messages = []

    #  getters
    def message_count(self):
        return self.__message_count

    def message(self, message_id):
        return self.__messages[message_id]

    #  methods
    def send_message(self, message):
        self.__messages.append(message)

        self.__message_count += 1

    def edit_message(self, message_id, new_message):
        self.__messages[message_id].edit_message(new_message)

    def delete_message(self, message_id):
        self.__messages.pop(message_id)

        self.__message_count -= 1


class PrivateChat(Chat):
    def __init__(self, first_username, second_username):
        self.__first_username = first_username
        self.__second_username = second_username

        super().__init__()

    #  getters
    def first_username(self):
        return self.__first_username

    def second_username(self):
        return self.__second_username


class EventChat(Chat):
    def __init__(self, initiator_username):
        self.__initiator_username = initiator_username
        self.__usernames = []
        self.__users_count = 1

        super().__init__()

    #  getters
    def initiator_username(self):
        return self.__initiator_username

    def users_count(self):
        return self.__users_count

    #  methods
    def add_user(self, username):
        self.__usernames.append(username)

        self.__users_count += 1

    def remove_user(self, username):
        self.__usernames.remove(username)

        self.__users_count -= 1