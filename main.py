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
                    results = quiz_engine.run_quiz(session_questions)
                    quiz_engine.display_results(results)
                    all_results.append(results)
                    #print(session_questions)
                elif choice == 2:
                    print(all_results)
                    if all_results:
                        print(f"du hast {len(all_results)} Quizzes gemacht")

                        for i, result in enumerate(all_results,1):
                            all_percent = (result["answered"]/result["total"]) * 100
                            print(f"{i}. {result["answered"]} von {result['total']} richtig ({all_percent:.0f}%) ")

                        print(f"Gesamtpunkte: {sum(result["points"] for result in all_results)}"
                              f"\n")

                    else:
                        print("du hast noch kein quiz gemacht")
                elif choice == 3:
                    print("Beehren sie uns bald wieder")
                    break


        except ValueError :
            print(f"nur die zulässigen optionen")



        # ...

if __name__ == '__main__':
    main()