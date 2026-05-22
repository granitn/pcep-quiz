questions = [
    {
        'question': "Welcher Datentyp ist 5.0?",
        'options': ["int", "float", "str", "bool"],
        'correct_index': 1,
        'explanation': "5.0 hat einen Dezimalpunkt, daher float",
        'category': "Datentypen",
        'difficulty': 1
    },
    {
        'question': "Was gibt `3 // 2` aus?",
        'options': ["1", "1.5", "2", "Error"],
        'correct_index': 0,
        'explanation': "// ist Floor Division (Ganzzahldivision)",
        'category': "Operatoren",
        "difficulty": 1
    },
    {
        'question': "Was gibt `len('Python')` zurück?",
        'options': ["5", "6", "7", "Error"],
        'correct_index': 1,
        'explanation': "Das Wort 'Python' hat 6 Zeichen",
        'category': "Strings",
        'difficulty': 1
    },
    {
        'question': "Welcher Operator prüft Gleichheit?",
        'options': ["=", "==", "!=", ":="],
        'correct_index': 1,
        'explanation': "== vergleicht zwei Werte",
        'category': "Operatoren",
        'difficulty': 1
    },
    {
        'question': "Was macht `input()`?",
        'options': [
            "Gibt Text aus",
            "Löscht Variablen",
            "Liest Benutzereingaben",
            "Beendet das Programm"
        ],
        'correct_index': 2,
        'explanation': "input() liest Eingaben vom Benutzer",
        'category': "Input/Output",
        'difficulty': 1
    },
    {
        'question': "Welcher Datentyp ist `[1, 2, 3]`?",
        'options': ["tuple", "dict", "list", "set"],
        'correct_index': 2,
        'explanation': "Eckige Klammern erzeugen eine Liste",
        'category': "Datentypen",
        'difficulty': 1
    },
    {
        'question': "Was gibt `bool('')` zurück?",
        'options': ["True", "False", "None", "Error"],
        'correct_index': 1,
        'explanation': "Ein leerer String gilt als False",
        'category': "Boolean",
        'difficulty': 2
    },
    {
        'question': "Was macht `append()` bei Listen?",
        'options': [
            "Entfernt Elemente",
            "Sortiert die Liste",
            "Fügt ein Element hinzu",
            "Kopiert die Liste"
        ],
        'correct_index': 2,
        'explanation': "append() hängt ein Element ans Ende der Liste",
        'category': "Listen",
        'difficulty': 1
    },
    {
        'question': "Was gibt `type(True)` zurück?",
        'options': ["int", "str", "bool", "float"],
        'correct_index': 2,
        'explanation': "True ist vom Typ bool",
        'category': "Datentypen",
        'difficulty': 1
    },
    {
        'question': "Wofür steht `elif`?",
        'options': [
            "Else If",
            "End Loop If",
            "Execute List If",
            "Error Limit If"
        ],
        'correct_index': 0,
        'explanation': "elif bedeutet else if",
        'category': "Kontrollstrukturen",
        'difficulty': 1
    },
    {
        'question': "Was gibt `range(3)` zurück?",
        'options': [
            "0,1,2",
            "1,2,3",
            "[0,1,2]",
            "Error"
        ],
        'correct_index': 0,
        'explanation': "range(3) erzeugt Werte von 0 bis 2",
        'category': "Schleifen",
        'difficulty': 2
    },
    {
        'question': "Welches Zeichen startet einen Kommentar in Python?",
        'options': ["//", "#", "--", "/*"],
        'correct_index': 1,
        'explanation': "# startet einen Kommentar",
        'category': "Syntax",
        'difficulty': 1
    }
]