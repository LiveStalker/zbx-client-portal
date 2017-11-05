VENV_PATH=./.env

# Create virtual environment
.PHONY: create_venv
create_venv:
	mkdir -p $(VENV_PATH)
	virtualenv -p python3 $(VENV_PATH)
	$(VENV_PATH)/bin/pip install -r requirements/dev.txt
