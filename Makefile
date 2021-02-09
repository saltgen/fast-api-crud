run-db:
	docker run -d --name my_postgres -v postgres_data:/var/lib/postgresql/data -p 5432:5432 -e POSTGRES_PASSWORD=postgres postgres
