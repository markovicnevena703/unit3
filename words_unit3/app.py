from flask import Flask, render_template


app = Flask(__name__)

@app.route("/words/<string:given_word>")
def words(given_word):
    s = given_word.upper()
    f = open("words.txt", "r")
    words_list = f.read().splitlines()
    l = []

    for word in words_list:
        if sorted(s) == sorted(word):
            l.append(word)
    
   

    return render_template('anagrams.html', given_word = given_word, l = l)