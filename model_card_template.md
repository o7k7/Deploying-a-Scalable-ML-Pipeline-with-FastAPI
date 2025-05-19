# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

- Model Class: LogisticRegression(scikit-learn)
- Training Date: 19/05/2025
- Version: 1.0
- Developer: Orhun Kupeli
- Libraries: pandas=2.2.2, scikit-learn=1.5.1
- Contact: orhunkupeli@gmail.com

## Intended Use
The main purpose of this model is to predict whether individuals' annual income will be above a certain threshold (for example, $50,000) based on their demographic and employment data.
Primary intended users: An analytical tool for social scientists, policymakers, and an indicator for marketing analysts.
Out-of-scope: Providing financial recommendations.

## Training Data
https://archive.ics.uci.edu/dataset/20/census+income

Attributes include demographic information (age, education, marital status, race, gender, home country) and employment-related data (working class, occupation).

Target variable: "salary", usually divided into two categories: ">50K" and "<=50K".
## Evaluation Data

The evaluation was done on a test set consisting of 20% of the original census.csv dataset, which was separated before training. The test data was processed using the same OneHotEncoder and LabelBinarizer that were trained on the training data.
## Metrics
Precision: 0.7358 | Recall: 0.2895 | F1: 0.4156

## Ethical Considerations
In case, the model is used to allocate employment, credit, or other important opportunities, it could lead to discrimination because of existing biases.

## Caveats and Recommendations
The model is specific to the census.csv data it was trained on. It cannot be directly generalized to different populations, time periods, or geographic regions.
