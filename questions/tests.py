from django.test import TestCase
from questions.models import Question, Poll


class QuestionViewTest(TestCase):

    def test_question_view(self):
        Question.objects.create(question_text="This a sample question")
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'questions.html')
        self.assertIn("This a sample question", response.content.decode())

    def test_submit_a_poll(self):
        question = Question.objects.create(question_text="This a sample question")
        response = self.client.post('/questions/save_poll/', data={'question_id': question.id,  'ans': 'Y'})
        poll = Poll.objects.first()
        self.assertEqual(1, poll.question_id.id)
        self.assertEqual(1, poll.yes_count)
        self.assertEqual(0, poll.no_count)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], f'/questions/poll_summary/{question.id}')

    def test_summary_view(self):
        pass


class QuestionModelTest(TestCase):

    def test_question_models(self):
        Question.objects.create(question_text="This a sample question")
        count = Question.objects.count()
        self.assertEqual(1, count)


class PollModelTest(TestCase):

    def test_poll_model_creation(self):
        question = Question.objects.create(question_text="This a sample question")
        Poll.objects.create(question_id=question)
        poll = Poll.objects.first()
        self.assertEqual(0, poll.yes_count)
        self.assertEqual(0, poll.no_count)
        self.assertEqual(question, poll.question_id)
        self.assertEqual(question.question_text, poll.question_id.question_text)

    def test_update_values_after_poll(self):
        question = Question.objects.create(question_text="This a sample question")
        Poll.objects.create(question_id=question)

        poll = Poll.objects.first()
        poll.update_count('Y')

        self.assertEqual(1, poll.yes_count)
        self.assertEqual(0, poll.no_count)
        self.assertEqual(question, poll.question_id)
        self.assertEqual(question.question_text, poll.question_id.question_text)

        poll.update_count('Y')
        self.assertEqual(2, poll.yes_count)
        self.assertEqual(0, poll.no_count)
        self.assertEqual(question, poll.question_id)
        self.assertEqual(question.question_text, poll.question_id.question_text)







