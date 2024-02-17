

class User:
    def __init__(self, name, age, gender, profile_picture, description, hobbies, interests):
        self.name = name
        self.age = age
        self.gender = gender
        self.profile_picture = profile_picture
        self.description = description
        self.hobbies = hobbies
        self.interests = interests
        
        self.history = []
        self.reviews = []
        self.friends = []

    def add_event_to_history(self, event):
        self.history.append(event)

    def add_review(self, review):
        self.reviews.append(review)

    def add_friend(self, username):
        self.friends.append(username)