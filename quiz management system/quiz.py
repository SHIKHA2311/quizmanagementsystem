# # Interactive quiz taking
# # - Score tracking and result storage
import random

def quiz(conn):
    cur = conn.cursor()
    user = input("Enter your name: ")
    ques_count = int(input("Enter how many questions you want to answer: "))
    score = 0

    # Insert initial record
    qry = '''INSERT INTO leaderboard (name, score, question, percentage) VALUES (?, ?, ?, ?)'''
    cur.execute(qry, (user, score, ques_count, 0.0))
    conn.commit()

    # Fetch all questions
    cur.execute("SELECT question, a, b, c, d, correct FROM questions")
    all_questions = cur.fetchall()

    # Adjust quiz length if needed
    if ques_count > len(all_questions):
        print(f"Only {len(all_questions)} questions available. Adjusting quiz length.")
        ques_count = len(all_questions)

    questions = random.sample(all_questions, ques_count)

    for i, q in enumerate(questions, start=1):
        print(f"\nQ{i:<2} {q[0]:<60}")
        print(f"a) {q[1]:<20} b) {q[2]:<20}")
        print(f"c) {q[3]:<20} d) {q[4]:<20}")

        # Valid input loop
        while True:
            ans = input("Your answer (a/b/c/d): ").strip().lower()
            if ans in ['a', 'b', 'c', 'd']:
                break
            print("Invalid input. Please enter a, b, c, or d.")

        # Map choice to actual answer
        choice_map = {'a': q[1], 'b': q[2], 'c': q[3], 'd': q[4]}
        selected_answer = choice_map[ans]

        if selected_answer.lower() == q[5].lower():
            score += 1
            print("Correct!")
        else:
            print(f" Wrong! Correct answer was: {q[5]}")

    percentage = (score / ques_count) * 100
    cur.execute("UPDATE leaderboard SET score = ?, percentage = ? WHERE name = ?", (score, percentage, user))
    conn.commit()
