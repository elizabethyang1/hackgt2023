const questions = [
    {
        information: 'Welcome!',
        question: 'Are you ready?',
        answers: [
            { text: "Yes", correct: true },
            { text: "No", correct: false }
        ]
    },
    {
        information: 'Income is the money you earn or receive regularly, typically in exchange for your time, skills, or investments. It encompasses all the financial resources flowing into your life. For most people, income primarily comes from employment, where they receive wages or a salary for their work. However, income can take various forms, including rental income from properties, dividends from investments, interest from savings, and even government benefits. Understanding and managing your income is a fundamental aspect of personal finance. It allows you to cover your living expenses, save for the future, and pursue your financial goals, making it a vital component of your overall financial well-being.',
        question: 'When it comes to creating a budget based on your income, which of the following best represents your financial priorities?',
        answers: [
            { text: "Covering essential living expenses (rent/mortgage, utilities, groceries)", correct: false },
            { text: "Building an emergency fund and saving for the future.", correct: false },
            { text: " Paying off debts and loans.", correct: false },
            { text: "All of the above.", correct: true }
        ]
    },{
        information:'Spending is the act of using ones financial resources to purchase goods, services, or investments. It can be categorized into several types, including essential spending, which covers necessities like housing and groceries, discretionary spending for non-essential items like entertainment and dining out, and investment spending to grow wealth through purchases such as stocks or real estate. Understanding these spending types is crucial for managing ones finances effectively and achieving financial goals.',
        question: 'When assessing your personal spending habits, which of the following best describes your approach to discretionary spending?',
        answers: [
            {text: "I carefully budget and track my discretionary spending to ensure it aligns with my financial goals.", correct: true},
            {text: "I occasionally always on discretionary items but try to cut back when my card maxes out.", correct: false},
            {text: "I often overspend on discretionary items and struggle to control this aspect of my finances.", correct: false},
            {text: "I don't pay much attention to discretionary spending; I need to evaluate it further.", correct: true}
        ]},{
        information:'Savings are the cornerstone of financial security and achieving your dreams. Whether it is building an emergency fund for unexpected expenses, saving for a down payment on a home, or planning for retirement, setting clear financial goals is essential. By consistently setting aside a portion of your income and directing it toward these goals, you are not only securing your future but also creating a path to realize your aspirations. Savings and goals are the building blocks of a financially stable and fulfilling life, allowing you to turn your dreams into reality.',
        question: 'When setting financial goals and planning your savings, which of the following are essential considerations?',
        answers: [
            {text: "Clearly defining your financial objectives.", correct: false},
            {text: "I occasionally always on discretionary items but try to cut back when my card maxes out.", correct: false},
            {text: "Establishing a timeline for achieving each goal.", correct: true},
            {text: "Regularly monitoring and adjusting your savings plan.", correct: true}
        ]},{
            information:'Savings are the cornerstone of financial security and achieving your dreams. Whether it is building an emergency fund for unexpected expenses, saving for a down payment on a home, or planning for retirement, setting clear financial goals is essential. By consistently setting aside a portion of your income and directing it toward these goals, you are not only securing your future but also creating a path to realize your aspirations. Savings and goals are the building blocks of a financially stable and fulfilling life, allowing you to turn your dreams into reality.',
            question: 'When setting financial goals and planning your savings, which of the following are essential considerations?',
            answers: [
                {text: "Clearly defining your financial objectives.", correct: false},
                {text: "I occasionally always on discretionary items but try to cut back when my card maxes out.", correct: false},
                {text: "Establishing a timeline for achieving each goal.", correct: true},
                {text: "Regularly monitoring and adjusting your savings plan.", correct: true}
            ]}
];

const questionElement = document.getElementById('question');
const informationElement = document.getElementById('information');
const answerButtons = document.getElementById('answerBtn');
const nextButtonContainer = document.getElementById('nextButtonContainer');
const nextButton = document.getElementById('nextBtn');

let curQuestionIdx = 1;
let score = 0;

function startQuiz() {
    curQuestionIdx = 0;
    score = 0;
    showQuestion();
}

function showQuestion() {
    answerButtons.innerHTML = '';
    nextButtonContainer.style.display = 'none';
    let currInfo = questions[curQuestionIdx].information;
    let currQuestion = questions[curQuestionIdx];
    let questNum = curQuestionIdx + 1;
    questionElement.innerHTML = questNum + '. ' + currQuestion.question;
    informationElement.innerHTML = currInfo;

    currQuestion.answers.forEach((answer, index) => {
        const button = document.createElement('button');
        button.innerHTML = answer.text;
        button.classList.add('btn');
        button.id = 'btn' + (index + 1);
        button.addEventListener('click', () => checkAnswer(answer.correct));
        answerButtons.appendChild(button);
    });
}

function checkAnswer(correct) {
    if (correct) {
        score++;
        nextButtonContainer.style.display = 'block'; // Next button after a correct answer
    } else {
        nextButtonContainer.style.display = 'none';
    nextButton.addEventListener('click', showNextQuestion);
}}


function showNextQuestion() {
    if (curQuestionIdx < questions.length) {
        showQuestion(curQuestionIdx);
        curQuestionIdx++;
    } else { // last page
        showEndScreen();
        
    }
}
function showEndScreen() {

    // Hide existing elements
    questionElement.style.display = 'none';
    informationElement.style.display = 'none';
    answerButtons.style.display = 'none';
    nextButton.style.display = 'none';
  
    // Redirect to the new page
    window.location.href = 'result.html';
}
startQuiz();