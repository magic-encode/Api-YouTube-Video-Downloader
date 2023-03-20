psql-up:
	docker pull postgres

psql-run:
	docker run --name my-postgres -e POSTGRES_USER=postgresql -e POSTGRES_PASSWORD=password -e POSTGRES_DB=postgres -p 5432:5432 -d postgres

celery-run:
	celery -A mysite worker -l info -c 4

celery-run-mac:
	celery -A mysite worker -l info --polo=solo

celery-log:
	sudo journalctl -u celery

nginx-log:
	sudo tail -F /var/log/nginx/error.log
