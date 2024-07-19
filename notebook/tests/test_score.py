from nbresult import ChallengeResultTestCase

class TestScore(ChallengeResultTestCase):
    def test_score_multiple(self):
        self.assertEqual(self.result.multiple, 23)

    def test_score_sum_square(self):
        self.assertEqual(self.result.sum_square, 25164150)

    def test_score_sundays(self):
        self.assertEqual(self.result.sundays, 171)
