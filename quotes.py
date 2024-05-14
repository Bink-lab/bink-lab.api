import os
import sys
import socket
import random

from flask import Flask, jsonify

app = Flask(__name__)

# Function to get a random quote
def get_random_quote():
    # Read quotes from the text file
    with open('quotes.txt', 'r') as file:
        quotes = file.readlines()
    
    # Strip newline characters from each quote
    quotes = [quote.strip() for quote in quotes]
    
    # Select a random quote from the list
    random_quote = random.choice(quotes)

    return random_quote

@app.route("/")
def hello_world():
    version = sys.version_info
    res = (
        "<h1>Hello my friends</h1>"
        f"<h2>{os.getenv('ENV')}</h2></br>"
        f"Running Python: {version.major}.{version.minor}.{version.micro}<br>"
        f"Hostname: {socket.gethostname()}"
    )
    return res

@app.route("/random-quote")
def random_quote():
    quote = get_random_quote()
    return jsonify({'quote': quote})

if __name__ == "__main__":
    app.run(debug=True)
