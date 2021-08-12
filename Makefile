#@IgnoreInspection BashAddShebang

.PHONY: shell run test coverage lint lint-fix makemigrations emptymigration dumpdata migrate mysql

run:
	docker-compose up

test:
	./runner.py coverage run --source='.' manage.py test --noinput --failfast

coverage: test
	coverage report & coverage html --fail-under=100

html:
	open htmlcov/index.html

lint:
	flake8

lint-fix:
	yapf -r -i *

makemigrations:
	docker exec -t --interactive achievements-backend_web_1 python manage.py makemigrations achievements 

emptymigration:
	docker exec -t --interactive achievements-backend_web_1 python manage.py makemigrations achievements --emptymigration

dumpdata:
	docker exec -t --interactive achievements-backend_web_1 python manage.py dumpdata achievements > achievements/fixtures/fixture.json

migrate:
	docker exec -t --interactive achievements-backend_web_1 python manage.py migrate

shell:
	docker exec -t --interactive achievements-backend_web_1 python manage.py shell

postgres:
	# Just runs the database image
	docker-compose up db

reset:
	# Deletes the database image
	docker rm -f -v achievements-backend_db_1	

backend_attach:
	docker attach achievements-backend_web_1

docker_build:
	docker-compose build