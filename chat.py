

class Message:
    def __init__(self, username, message):
        self.__username = username
        self.__message = message

    def username(self):
        return self.__username

    def message(self):
        return self.__message

    def edit_message(self, new_message):
        self.__message = new_message


class Chat:
    def __init__(self):
        self.__message_count = 0

        self.__messages = []

    def add_message(self, message):
        self.__messages.append(message)

        self.__message_count += 1

    def edit_message(self, message_id, new_message):
        self.__messages[message_id].edit_message(new_message)

    def delete_message(self, message_id):
        self.__messages.pop(message_id)


class PrivateChat(Chat):
    def __init__(self, first_username, second_username):
        self.__first_username = first_username
        self.__second_username = second_username

        super().__init__()


class EventChat(Chat):
    def __init__(self, initiator_username):
        self.__initiator_username = initiator_username
        self.__usernames = []

        super().__init__()

    def add_user(self, username):
        self.__usernames.append(username)

    def remove_user(self, username):
        self.__usernames.remove(username)