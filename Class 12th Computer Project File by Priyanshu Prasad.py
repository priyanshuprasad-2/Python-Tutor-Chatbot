import random

def chatbot():
    print("**** Welcome to the Python Chatbot Tutor! ****")
    print("Hello there, I'm Priyanshu, your friendly AI assistant.")
    name = input("Please enter your name: ")
    print(f"That's great to meet you, {name}! How can I assist you today?")

    studied_topics = []  # to track studied topics

    # Load topics from file once, at the very beginning
    with open('class11_python_topics.txt', 'r') as file:
        content = file.read()
    topics = content.split("Topic:")

    while True:
        user_input = input("Enter a Python topic (or 'exit' to quit): ").lower()

        if user_input == 'exit':
            print(f"**** Thank you {name}, for using the Python Chatbot Tutor. ****")

            if studied_topics:  # offer quiz only if some topics were studied
                choice = input("Do you want to take a quiz on what you studied? (yes/no): ").lower()
                if choice == "yes":
                    take_quiz(studied_topics, name)
            print("Goodbye!")
            break

        found = False
        for topic in topics:
            if user_input in topic.lower():
                print(f"\nWow, {user_input} is an interesting topic! Let's make it crystal clear for you.\n")
                print("Topic:" + topic.strip())   # show content
                studied_topics.append(user_input)  # track studied topic
                found = True
                break

        if not found:
            print("Sorry, I couldn't find information about that topic. Please try again.")


def take_quiz(studied_topics, name):
    quiz_bank = {
        "string": [
            ("Which symbol is used to enclose strings in Python?", "quotes"),
            ("Which function is used to find length of a string?", "len"),
            ("Is a string mutable or immutable in Python?", "immutable")
        ],
        "list": [
            ("Which brackets are used to define a list?", "square"),
            ("Which method adds an element at the end of a list?", "append"),
            ("Are lists mutable or immutable?", "mutable")
        ],
        "tuple": [
            ("Which brackets are used to define a tuple?", "parentheses"),
            ("Are tuples mutable or immutable?", "immutable"),
            ("Which function returns index of a value in tuple?", "index")
        ],
        "dictionary": [
            ("Dictionaries store data in form of?", "key-value pairs"),
            ("Which method returns all keys of dictionary?", "keys"),
            ("Are dictionary keys mutable or immutable?", "immutable")
        ],
        "if else program": [
            ("Which keyword is used for condition checking?", "if"),
            ("Which keyword provides alternative when condition is false?", "else"),
            ("Which keyword allows multiple conditions?", "elif")
        ],
        "loops": [
            ("Which keyword is used to stop a loop?", "break"),
            ("Which loop runs until a condition becomes false?", "while"),
            ("Which statement skips current iteration?", "continue")
        ],
        "function": [
            ("Which keyword is used to define a function?", "def"),
            ("Which keyword is used to return value from function?", "return"),
            ("Which keyword is used for anonymous functions?", "lambda")
        ]
    }

    # pick only questions from studied topics
    questions = []
    for topic in studied_topics:
        if topic in quiz_bank:
            questions.extend(quiz_bank[topic])

    if not questions:
        print("\nSorry, no quiz questions available for studied topics.")
        return

    print("\n**** QUIZ TIME ****")
    score = 0
    random.shuffle(questions)

    for q, ans in questions[:5]:  # ask max 5 questions
        user_ans = input(q + " ").lower().strip()
        if ans in user_ans:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {ans}")

    print(f"\n{name}, your final score is {score}/{min(5, len(questions))}")

    if score == 5:
        print("Excellent! You mastered the topics.")
    elif score >= 3:
        print("Good job! Just a little more practice needed.")
    else:
        print("Needs improvement. Review the topics again.")


chatbot()
