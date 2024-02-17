import chat
import review


class Categories(Enum):
    PARTY = 0
    FESTIVAL = 1
    CONCERT = 2
    FOOTBALL_GAME = 3
    BASKETBALL_GAME = 4


class Criteria(Enum):
    MALE_ONLY = 0
    FEMALE_ONLY = 1
    R18 = 2
    UNDER_30 = 3


class Event:
    def __init__(self, title, initiator_username, criteria, categories, total_people_required):
        self.title = title
        self.__initiator_username = initiator_username
        self.criteria = criteria
        self.categories = categories
        self.__total_people_required = total_people_required

        self.__participant_usernames = []
        self.__participants_count = 0
        self.__reviews = []
        self.__event_chat = EventChat(initiator_username)

    #  getters
    def initiator_username(self):
        return self.__initiator_username

    def total_people_required(self):
        return self.__total_people_required

    def participants_count(self):
        return self.__participants_count

    def remaining_people_required(self):
        return self.__total_people_required - self.__participants_count

    #  methods
    def add_person(self, username):
        self.__participant_usernames.append(username)

        self.__participants_count += 1

    def remove_person(self, username):
        self.__participant_usernames.remove(username)

        self.__participants_count -= 1

    def add_review(self, review):
        self.__reviews.append(review)

    def edit_review(self, review_id, new_comment):
        self.__reviews[review_id].edit_comment(new_comment)

    def delete_review(self, review_id):
        self.__reviews.pop(review_id)

    def send_message(self, message):
        self.__event_chat.send_message(message)

    def edit_message(self, message_id, new_message):
        self.__event_chat.edit_message(message_id, message)

    def delete_message(self, message_id):
        self.__event_chat.delete_message(message_id)