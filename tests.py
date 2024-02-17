import review

import unittest


class TestReviewClass(unittest.TestCase):

    def test_review_creation(self):
        review = Review("user1", 4, "Great product!")

        self.assertEqual(review.username(), "user1")
        self.assertEqual(review.rating(), 4)
        self.assertEqual(review.comment(), "Great product!")
        self.assertFalse(review.is_edited())

    def test_edit_comment(self):
        review = Review("user2", 3, "Good product!")
        
        self.assertFalse(review.is_edited())
        
        review.edit_comment("Updated comment!")
        
        self.assertEqual(review.comment(), "Updated comment!")
        self.assertTrue(review.is_edited())

if __name__ == '__main__':
    unittest.main()
