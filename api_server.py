from flask import Flask, request, jsonify
from credit_scoring import CreditScoringSystem

app = Flask(__name__)
scoring_system = CreditScoringSystem()

@app.route('/api/credit-score', methods=['POST'])
def credit_score():
    user_data = request.json
    # You need to implement calculate_credit_score in your class
    score = scoring_system.calculate_credit_score(user_data)
    return jsonify({'credit_score': score})

if __name__ == '__main__':
    app.run(port=5000, debug=True)