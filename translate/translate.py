from flask import Flask, request, render_template
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    lang = request.form['lang']

    if lang == 'en_to_nl':
        translated = GoogleTranslator(source='en', target='nl').translate(text)
    else:  # Assume 'nl_to_en'
        translated = GoogleTranslator(source='nl', target='en').translate(text)

    return render_template('index.html', translated_text=translated)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Adjust the host and port as needed