from flask import Flask, render_template, request
from pyswip import Prolog
import re

app = Flask(__name__)

# Load Prolog knowledge base
prolog = Prolog()
prolog.consult("familytree.pl")


def extract_name(question):
    words = question.lower().split()
    return words[-1].replace("?", "")


def process_question(question):
    question = question.lower()

    if "father of" in question:
        person = extract_name(question)
        query = f"father_of(X, {person})"
        result = list(prolog.query(query))
        if result:
            name = result[0]["X"]
            return f"{name.capitalize()} is {person.capitalize()}'s father."
        else:
            return "I don't know the father."

    elif "mother of" in question:
        person = extract_name(question)
        query = f"mother_of(X, {person})"
        result = list(prolog.query(query))
        if result:
            name = result[0]["X"]
            return f"{name.capitalize()} is {person.capitalize()}'s mother."
        else:
            return "I don't know the mother."

    elif "brother of" in question:
        person = extract_name(question)
        query = f"brother_of(X, {person})"
        result = list(prolog.query(query))
        if result:
            name = result[0]["X"]
            return f"{name.capitalize()} is {person.capitalize()}'s brother."
        else:
            return "No brother found."

    else:
        return "Sorry, I don't understand the question."


@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]
        answer = process_question(question)
    return render_template("index.html", answer=answer)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)