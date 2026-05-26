from questions import questions
import quiz_engine
import random

def main() -> None:
    """Hauptprogramm mit Menu"""
    all_results = []

    while True:
        print("\n=== PCEP Quiz ===")
        print("1. Quiz starten")
        print("2. Meine Ergebnisse anzeigen")
        print("3. Beenden")


        try:
            choice = int(input("> "))
            if 1 <= choice <= 3 :

                if choice == 1:
                    session_questions = questions.copy()
                    random.shuffle(session_questions)
                    result = quiz_engine.run_quiz(session_questions)
                    #print(session_questions)

        except ValueError :
            print(f"nur die zulässigen optionen")



        # ...

if __name__ == '__main__':
    main()