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


Question 1 b)
Based on the OLS regression results, the estimated Average Treatment Effect (ATE) of participating in the carbon offset program is:
τ̂ = 4.79
The p-value for τ̂ is 0.027, which indicates that the estimated ATE is statistically significant at the 5% level.
This suggests that, after controlling for sustainability spending, corporations that participated in the carbon offset program have, on average, an engagement score 4.79 points higher than those that did not participate.

Question 1 c)
The estimated ATE (τ̂) can be interpreted as a causal effect under the following assumptions of the Rubin Causal Model:
Unconfoundedness (Ignorability): There are no unobserved confounders that affect both the treatment assignment (W) and the outcome (Y_obs). In other words, after controlling for sustainability spending (X), the treatment assignment is as good as random.
Linearity of the Model: The relationship between the outcome, treatment, and covariate is correctly specified as linear.
Stable Unit Treatment Value Assumption (SUTVA): There is no interference between units (one corporation's treatment status does not affect another's outcome), and only one version of the treatment exists.
Under these assumptions, τ̂ provides an unbiased estimate of the causal effect of the carbon offset program on stakeholder engagement.
