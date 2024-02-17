from enum import Enum, auto


class Gender(Enum):
    MALE = auto()
    FEMALE = auto()
    OTHER = auto()


class User:
    def __init__(self, name, age, gender, description, hobbies, interests):
        self.name = name
        self.age = age
        self.gender = gender
        self.description = description
        self.hobbies = hobbies
        self.interests = interests

        self.__history = []
        self.__reviews = []
        self.__friends = []

    #  getters
    def history(self):
        return self.__history

    def reviews(self):
        return self.__reviews

    def friends(self):
        return self.__friends

    #  methods
    def add_event_to_history(self, event):
        self.history.append(event)

    def add_review(self, review):
        self.reviews.append(review)

    def remove_review(self, review_id):
        self.reviews.pop(review_id)

    def add_friend(self, username):
        self.friends.append(username)

    def remove_friend(self, username):
        self.friends.remove(username)