from flask import Flask, jsonify
import random

app = Flask(__name__)

def get_random_quote():
    # Read quotes from the text file
    with open('quotes.txt', 'r') as file:
        quotes = file.readlines()
    
    # Strip newline characters from each quote
    quotes = [quote.strip() for quote in quotes]
    
    # Select a random quote from the list
    random_quote = random.choice(quotes)

    return random_quote

@app.route('/random-quote')
def random_quote():
    quote = get_random_quote()
    return jsonify({'quote': quote})

if __name__ == '__main__':
    app.run(debug=True)
