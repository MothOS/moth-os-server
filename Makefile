clean:
	@find . -type d -name '__pycache__' -exec rm -rf {} +

format: clean
	@poetry run black moth_os/ tests/

run:
	@poetry run python moth_os/moth_os_server.py $(ARGS)

run-tests:
	@poetry run pytest
