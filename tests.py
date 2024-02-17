import unittest

from enum import Enum, auto
from review import Review
import user

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

if __name__ == '__main__':
    unittest.main()
