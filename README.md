# my-spanish-tracker-api

A dictionary of 10,000 words and growing. Take a quiz to get an estimate of vocab knowledge and track your learning.


alembic upgrade head
python initial_data.py

git push heroku main
heroku run alembic upgrade head
heroku run python initial_data.py
