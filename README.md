Dependencies
Python 3.7+
Flask 2.1+
SQLite
Docker (for containerization)
docker-compose (for orchestration)


Setup Instructions:
git clone https://github.com/your-username/rule-engine-ast.git
cd rule-engine-ast
version: '3'
services:
  flask:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/app
    depends_on:
      - db
  db:
    image: "nouchka/sqlite3"
    container_name: sqlite-db
docker-compose up --build
http://127.0.0.1:5000
curl -X POST http://127.0.0.1:5000/create_rule -H "Content-Type: application/json" -d '{"rule": "age > 30 AND salary > 50000"}'
python tests.py
