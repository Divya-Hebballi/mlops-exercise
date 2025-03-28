import json
import os
import app  # Assuming app.py contains the main function

def test_model_file_created():
    # Ensure the model file is created
    app.main()  # Assuming the main function trains the model
    assert os.path.exists('models/model.pkl')

def test_model_score():
    # Get the current model's score
    score = app.main()  # Assuming the main function returns the model's score
    assert isinstance(score, float)
    assert 0.0 <= score <= 1.0

    # Load the model scores from the JSON file
    with open('model_scores.json', 'r') as f:
        model_scores = json.load(f)

    # Get the latest score from the JSON file
    latest_score = model_scores[-1]['score']

    # Compare the current score with the latest score
    assert score >= latest_score