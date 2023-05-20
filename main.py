from flask import Flask, render_template
import pandas as pd

my_app = Flask(__name__)
df = pd.read_csv("dictionary.csv")

@my_app.route("/")
def home_page():
    return render_template("home.html")


@my_app.route("/app/v1/<word>")
def translator_page(word):
    definition = df.loc[df['word'] == word]["definition"].squeeze()
    result_dictionary = {"word": word, "definition": definition}
    return result_dictionary


if __name__ == "__main__":
    my_app.run(debug=True, port=5001)
