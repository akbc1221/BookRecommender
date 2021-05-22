from flask import Flask, render_template
import pandas as pd
from utils import recommender

app = Flask(__name__)

df = pd.read_json('result.json')

@app.route("/")
def home():
    N = 9
    random_samples = df.sample(N)
    random_samples = [dict(random_samples.iloc[i]) for i in range(N)]
    return render_template('index.html', books=random_samples)


@app.route('/output/<bookTitle>')
def output(bookTitle):
    result = dict(df[df['title']==bookTitle].squeeze())
    recommended_book= recommender(df, result['genre'])
    return render_template('output.html', result=result, recommended_book=recommended_book)


if __name__ == "__main__":
    app.run(debug = True)