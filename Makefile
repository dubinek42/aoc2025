.PHONY: check lint format typecheck fix code

check: lint format typecheck

lint:
	poetry run ruff check .

format:
	poetry run black --check .

typecheck:
	poetry run mypy .

fix:
	poetry run ruff check --fix .
	poetry run black .

code: fix typecheck
