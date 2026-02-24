def process_question(question):
    question = question.lower()

    relationships = {
        "father of": ("father_of", "father"),
        "mother of": ("mother_of", "mother"),
        "brother of": ("brother_of", "brother"),
        "sister of": ("sister_of", "sister"),
        "grandfather of": ("grandfather_of", "grandfather"),
        "grandmother of": ("grandmother_of", "grandmother"),
        "aunt of": ("aunt_of", "aunt"),
        "uncle of": ("uncle_of", "uncle"),
        "ancestor of": ("ancestor_of", "ancestor")
    }

    for phrase, (predicate, label) in relationships.items():
        if phrase in question:
            person = extract_name(question)
            query = f"{predicate}(X, {person})"
            result = list(prolog.query(query))

            if result:
                answers = [r["X"].capitalize() for r in result]
                answer_text = ", ".join(answers)
                return f"{answer_text} is {person.capitalize()}'s {label}."
            else:
                return f"No {label} found for {person.capitalize()}."

    return "Sorry, I don't understand the question."
