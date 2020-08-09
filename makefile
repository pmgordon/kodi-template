TEST_PATH=./tests
MODULE_NAME="source"

test:
	pytest --verbose --color=yes $(TEST_PATH)

coverage:
	pytest -vv --color=yes --cov-report term-missing  --cov=$(MODULE_NAME) $(TEST_PATH)

lint:
	pylint --rcfile=.pylintrc -f colorized */*py */*/*.py

init:
	${HOME}/.pyenv/versions/3.5.4/bin/python3.5 -m venv .pyenv

pipreq:
	pip install -r requirements.txt

kodi-init:
	bash scripts/init.sh

kodi-tail:
	tail -f ~/Library/Logs/kodi.log

kodi-push:
	./scripts/push-local.sh

kodi-deploy:
	./scripts/deploy.sh
	
