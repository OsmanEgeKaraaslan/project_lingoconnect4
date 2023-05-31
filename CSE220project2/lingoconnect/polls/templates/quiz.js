// quiz.js

function submitQuiz() {
  const q1Input = document.querySelector('input[name="q1"]:checked');
  const q2Input = document.querySelector('input[name="q2"]:checked');

  if (q1Input && q2Input) {
    const q1Answer = q1Input.value;
    const q2Answer = q2Input.value;

    checkAnswer(q1Answer, 'Paris', 'q1');
    checkAnswer(q2Answer, 'Leonardo da Vinci', 'q2');
  } else {
    console.log("Please answer all questions.");
  }
}

function checkAnswer(userAnswer, correctAnswer, questionId) {
  const question = document.getElementById(questionId);

  if (userAnswer === correctAnswer) {
    question.classList.add('correct');
  } else {
    question.classList.add('wrong');
  }
}

// Remove feedback when user changes answer
document.querySelectorAll('input[type="radio"]').forEach((radio) => {
  radio.addEventListener('change', function () {
    const question = this.closest('.question');
    question.classList.remove('correct', 'wrong');
  });
});
