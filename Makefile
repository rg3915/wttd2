migrate:
	python manage.py makemigrations
	python manage.py migrate

test:
	python manage.py test -n

heroku_push:
	git push heroku master --force

heroku_migrate:
	heroku run python manage.py migrate

selenium_subscription:
	python eventex/subscriptions/tests/selenium/selenium_subscription.py

dumpdata:
	manage dumpdata --indent 4 subscriptions

backup:
	python manage.py dumpdata subscriptions --format=json --indent=2 > fixtures.json
