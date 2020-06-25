python_cmd := python
pip_cmd := $(python_cmd) -m pip


clean:
	$(pip_cmd) uninstall -y qusetta
	rm -rf dist
	rm -rf build
	rm -rf qusetta.egg-info

install:
	$(pip_cmd) install --upgrade --user pip
	$(pip_cmd) install --user -e .

dev_install:
	$(pip_cmd) install --upgrade --user pip
	$(pip_cmd) install --user -e .
	$(pip_cmd) install --user -r requirements-dev.txt

test:
	$(python_cmd) -m pydocstyle convention=numpy qusetta
	$(python_cmd) -m pytest --cov-report=html --cov=qusetta --cov=tests
	$(python_cmd) setup.py sdist bdist_wheel
	$(python_cmd) -m twine check dist/*

test_codestyle:
	$(pip_cmd) install --upgrade --user pip
	$(pip_cmd) install --user pycodestyle
	$(python_cmd) -m pycodestyle qusetta tests
