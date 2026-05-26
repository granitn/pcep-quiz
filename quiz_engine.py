from typing import Optional
import random


def display_question(question: dict, num: int, total: int) -> None:
    question_to_use = question["question"]
    answer_options = question["options"]
    print(f"{question_to_use} ({num}/{total}) ")
    print(f"1 - {answer_options[0]} \U0000Fe34 2 - {answer_options[1]}"
          f"\n3 - {answer_options[2]} \U0000Fe34 4 - {answer_options[3]}")

    #pass


#display_question(questions)



def get_answer(question: dict) -> int:
    """Liest Antwort vom Nutzer (mit Validierung!)"""
    while True:
        try:
            answer = int(input("options 1 - 4"
                               "\n>"))
            if answer > 4 or answer < 1 :
                print("that number was not an option")
            else:
                return answer
        except ValueError:
            print("answer must be a number")


    pass

def check_answer(answer: int, question: dict) -> bool:
    """Prüft ob Antwort richtig ist"""
    check = (answer -1) == question["correct_index"]
    if check:
        return True
    else:
        return False

def run_quiz(questions: list[dict]) -> dict:
    """Durchläuft ein komplettes Quiz"""
    #ergebniss speicher
    results = {
        "points" : 0,
        "missed" : 0,
        "total" : len(questions),
        "run"  : []
    }
    #display_question
    for i, question in enumerate(questions, 1):
        display_question(question, i, len(questions))
    #get_answer
        answer = get_answer(question)
    #check_answer
        is_correct_answer = check_answer(answer, question)
        if is_correct_answer:
            print(f"\U0001F662 Correct \U0001F660"
                  f"\n{"-" * 30}\n")
            results["points"] += 1
        else:
            print(f"wrong answer \U0001F622"
                  f"\n{question["explanation"]}"
                  f"\n{"-" * 30}\n")
            results["missed"] += 1

        results["run"].append(
            {
                "question" : question["question"],
                "is_correct" : is_correct_answer,
                "category" : question.get("category", "Unknown")
            }
        )
    return results





    #desplay_result
    #und an "speicher" hängen
    #pass

def display_results(results: dict) -> None:
    """Zeigt Ergebnisse an"""
    percent = (results["points"] / results["total"]) * 100
    print(f"\U0001F668 Ergebnisse \U0001F668")
    print(f"du hast {results["points"]}/{results["total"]} - {percent:.1f}% ")
