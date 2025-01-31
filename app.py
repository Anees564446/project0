from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image_search')
def image_search():
    return render_template('image_search.html')

@app.route('/advanced_search')
def advanced_search():
    return render_template('advanced_search.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    return redirect(f"https://www.google.com/search?q={query}")

@app.route('/search_images', methods=['GET'])
def search_images():
    query = request.args.get('query')
    return redirect(f"https://www.google.com/search?hl=en&tbm=isch&q={query}")

@app.route('/advanced_search_results', methods=['GET'])
def advanced_search_results():
    all_words = request.args.get('all_words')
    exact_phrase = request.args.get('exact_phrase')
    any_words = request.args.get('any_words')
    none_words = request.args.get('none_words')

    query = f"all these words:{all_words} exact phrase:{exact_phrase} any of these words:{any_words} none of these words:{none_words}"
    return redirect(f"https://www.google.com/search?q={query}")

@app.route('/lucky', methods=['GET'])
def lucky():
    query = request.args.get('query')
    return redirect(f"https://www.google.com/search?btnI&q={query}")

if __name__ == '__main__':
    app.run(debug=True)
