install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	py -m pip install dist/werewolf_gendiff-0.1.0-py3-none-any.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

gendif:
	poetry run gendiff
