from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load the trained pipelines
naive_bayes_model = pickle.load(open("naive_bayes_model.pkl", "rb"))
complement_nb_model = pickle.load(open("complement_nb_model.pkl", "rb"))
svm_model = pickle.load(open("svm_model.pkl", "rb"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_text():
    input_text = request.form['input_text']
    if input_text.strip():
        # Predictions from all classifiers
        prediction_nb = naive_bayes_model.predict([input_text])[0]
        prediction_svm = svm_model.predict([input_text])[0]
        prediction_cnb = complement_nb_model.predict([input_text])[0]

        result = {
            "Naive Bayes Prediction": prediction_nb,
            "SVM Prediction": prediction_svm,
            "Complement Naive Bayes Prediction": prediction_cnb
        }
        return jsonify(result)
    return jsonify({"error": "No text provided!"})

if __name__ == '__main__':
    app.run(debug=True)
