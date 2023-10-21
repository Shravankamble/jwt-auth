tests: ./tests/test_api.py
	pytest -s -v

build: ./Dockerfile
	docker build -t fapi:v1 .

run: ./main.py
	uvicorn main:app --reload
