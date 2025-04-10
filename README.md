# Exercise 2 — DSS5105 Data Science Projects in Practice

## Project Overview
This project implements a Flask API that predicts the stakeholder engagement score of a corporation based on:
- Whether the corporation participated in a carbon offset program (`W`)
- The corporation's sustainability spending (`X`)

The prediction model is built using the Rubin Causal Model framework. A linear regression (OLS) is used to estimate the Average Treatment Effect (ATE) of the carbon offset program.

---

## File Descriptions

| File              | Description                                               |
|------------------|-----------------------------------------------------------|
| `app.py`         | Main Flask application with model training and prediction API. |
| `Dockerfile`     | Configuration file for containerizing the project.        |
| `requirements.txt` | Python dependencies required to run the project.         |

---

## How to Run

### Step 1: Build the Docker Image
```bash
docker build -t my-api .

### Step 2: Run the Docker Container
docker run -p 5000:5000 my-api
## How to Use the API

Send a GET request to the /predict endpoint with parameters:

W = 1 (if participated in the program) or 0 (if not)
X = sustainability spending (in $1000s)

curl "http://localhost:5000/predict?W=1&X=20"


Output：
{
  "W": 1.0,
  "X": 20.0,
  "Predicted Engagement Score": 117.16
}
