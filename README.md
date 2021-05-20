# Heart Disease Analysis

This is a Django app, which contains a dashboard visualizing the data from [four databases: Cleveland, Hungary, Switzerland, and Long Beach V](https://www.kaggle.com/johnsmith88/heart-disease-dataset). In addition to the dashboard, we have trained and tested five different machine learning classifiers on the data: random forest, logistic regression, naive bayes, support vector machine and a feedforward neural network. The training and test results are found in the Django app under the Symptom Checker tab. The classifier with the highest test accuracy (feedforward neural network) is deployed on the webapp. 

## Deployed Webapp

[Heart Disease Analysis](https://heart-attack-analysis.herokuapp.com/)

## Running Locally

Make sure you have Python 3.9 [installed locally](https://docs.python-guide.org/starting/installation/). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/toddgraham121/cs510-heart-attack-analysis/
$ cd heart-attack-analysis

$ python3 -m venv heart-attack-analysis
$ pip install -r requirements.txt

$ createdb python_heart-attack-analysis

$ python manage.py migrate
$ python manage.py collectstatic
```
On Mac:
```
$ heroku local
```
On Windows:
```
$ heroku local web -f Procfile.windows
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku main

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
