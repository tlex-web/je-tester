
install:
    source ./venv/bin/activate; \
    pip install -r requirements.txt; \

run:
	source ./venv/bin/activate; \
	python3 main.py; \

test:
	source ./venv/bin/activate; \
	python -m pytest; \

coverage:
	source ./venv/bin/activate; \
	coverage run -m pytest; \
	coverage report -m; \
	coverage html; \

