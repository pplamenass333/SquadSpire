

class Review:
    def __init__(self, username, rating, comment):
        self.__username = username
        self.__rating = rating
        self.__comment = comment

        self.__is_edited = False

    #  getters
    def username(self):
        return self.__username

    def rating(self):
        return self.__rating

    def comment(self):
        return self.__comment

    def is_edited(self):
        return self.__is_edited

    #  methods
    def edit_comment(self, new_comment):
        self.__comment = new_comment

        self.__is_edited = True