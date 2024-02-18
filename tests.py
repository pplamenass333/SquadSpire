import unittest

from enum import Enum, auto
from review import Review
import user
from event import Event, Categories, Criteria, EventChat

class TestReviewClass(unittest.TestCase):

    def test_review_creation(self):
        review = Review("user1", 4, "Great event!")

        self.assertEqual(review.username(), "user1")
        self.assertEqual(review.rating(), 4)
        self.assertEqual(review.comment(), "Great event!")
        self.assertFalse(review.is_edited())

    def test_edit_comment(self):
        review = Review("user2", 3, "Good event!")

        self.assertFalse(review.is_edited())

        review.edit_comment("Updated comment!")

        self.assertEqual(review.comment(), "Updated comment!")
        self.assertTrue(review.is_edited())


class TestUserClass(unittest.TestCase):

    def test_user_creation(self):
        user = User("Kubrat Ivanov", 33, Gender.MALE, "Sometimes a nice person", ["Reading", "Cooking", "Making skull cups"], ["Hiking", "Photography"])
        self.assertEqual(user.name, "Kubrat Ivanov")
        self.assertEqual(user.age, 33)
        self.assertEqual(user.gender, Gender.MALE)
        self.assertEqual(user.description, "Sometimes a nice person")
        self.assertEqual(user.hobbies, ["Reading", "Cooking", "Making skull cups"])
        self.assertEqual(user.interests, ["Hiking", "Photography"])
        self.assertEqual(user.history(), [])
        self.assertEqual(user.reviews(), [])
        self.assertEqual(user.friends(), [])

    def test_add_event_to_history(self):
        user = User("Kubrat Ivanov", 33, Gender.MALE, "Sometimes a nice person", ["Reading", "Cooking", "Making skull cups"], ["Hiking", "Photography"])
        user.add_event_to_history("Event 1")
        self.assertEqual(user.history(), ["Event 1"])

    def test_add_review(self):
        user = User("Kubrat Ivanov", 33, Gender.MALE, "Sometimes a nice person", ["Reading", "Cooking", "Making skull cups"], ["Hiking", "Photography"])
        review = "Good event!"
        user.add_review(review)
        self.assertEqual(user.reviews(), ["Good event!"])

    def test_remove_review(self):
        user = User("Kubrat Ivanov", 33, Gender.MALE, "Sometimes a nice person", ["Reading", "Cooking", "Making skull cups"], ["Hiking", "Photography"])
        user.add_review("Good event!")
        user.remove_review(0)
        self.assertEqual(user.reviews(), [])

    def test_add_friend(self):
        user = User("Kubrat Ivanov", 33, Gender.MALE, "Sometimes a nice person", ["Reading", "Cooking", "Making skull cups"], ["Hiking", "Photography"])
        user.add_friend("Tervel Pulev")  
        self.assertEqual(user.friends(), ["Tervel Pulev"])

    def test_remove_friend(self):
        user = User("Kubrat Ivanov", 33, Gender.MALE, "Sometimes a nice person", ["Reading", "Cooking", "Making skull cups"], ["Hiking", "Photography"])
        user.add_friend("Tervel Pulev") 
        user.remove_friend("Tervel Pulev")
        self.assertEqual(user.friends(), [])



class TestEventClass(unittest.TestCase):

    def setUp(self):
        self.event = Event("Party", "user1", Criteria.MALE_ONLY, Categories.PARTY, 10)
        self.event.add_person("user2")
        self.review1 = Review("user1", 5, "Great event!")
        self.review2 = Review("user2", 4, "Good event!")
        
    def test_event_creation(self):
        self.assertEqual(self.event.title, "Party")
        self.assertEqual(self.event.initiator_username(), "user1")
        self.assertEqual(self.event.criteria, Criteria.MALE_ONLY)
        self.assertEqual(self.event.categories, Categories.PARTY)
        self.assertEqual(self.event.total_people_required(), 10)
        self.assertEqual(self.event.participants_count(), 1)

    def test_add_person(self):
        self.event.add_person("user3")
        self.assertEqual(self.event.participants_count(), 2)

    def test_remove_person(self):
        self.event.remove_person("user2")
        self.assertEqual(self.event.participants_count(), 0)

    def test_add_review(self):
        self.event.add_review(self.review1)
        self.assertEqual(len(self.event.reviews), 1)

    def test_edit_review(self):
        self.event.add_review(self.review1)
        self.event.edit_review(0, "Updated comment!")
        self.assertEqual(self.event.reviews[0].comment(), "Updated comment!")

    def test_delete_review(self):
        self.event.add_review(self.review1)
        self.event.add_review(self.review2)
        self.event.delete_review(0)
        self.assertEqual(len(self.event.reviews), 1)

    def test_send_message(self):
        self.event.send_message("Hello everyone!")
        self.assertEqual(len(self.event._Event__event_chat.messages), 1)

    def test_edit_message(self):
        self.event.send_message("Hello everyone!")
        self.event.edit_message(0, "Updated message!")
        self.assertEqual(self.event._Event__event_chat.messages[0], "Updated message!")

    def test_delete_message(self):
        self.event.send_message("Hello everyone!")
        self.event.delete_message(0)
        self.assertEqual(len(self.event._Event__event_chat.messages), 0)


if __name__ == '__main__':
    unittest.main()
