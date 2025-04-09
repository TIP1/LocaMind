# Params
VENV = .venv
PYTHON = python3
PYTHON_DIR = /Applications/Python 3.11
PIP = $(VENV)/bin/pip

# Creating a virtual environment
venv:
	@if [ ! -d "$(VENV)" ]; then \
		echo "📦 Creating a virtual environment..."; \
		$(PYTHON) -m venv $(VENV); \
		echo "✅ A virtual environment has been created."; \
	else \
		echo "⚠️The virtual environment already exists."; \
	fi

# Activating the virtual environment
activate:
	@echo "🔗 To activate the virtual environment, run the command:"
	@echo "source $(VENV)/bin/activate"

# Deactivating the virtual environment
deactivate:
	@echo "🔌 To deactivate the virtual environment, run the command:"
	@echo "deactivate"

# Installing dependencies
install: venv
	@echo "📥 Installing dependencies in a virtual environment..."
	@$(PIP) install --upgrade pip
	@$(PIP) install -r requirements.txt
	@echo "✅ Dependencies are installed."

.PHONY: env
# Creating an .env file
create-env:
	cp env .env
	@if [ -f .env ]; then \
		echo "✅ An .env has been created."; \
	else \
		echo "⚠️The creating of .env file was failed!"; \
	fi

# Deleting an .env file
delete-env:
	@if [ -f .env ]; then \
		rm -rf .env; \
		echo "✅ An .env has been deleted."; \
	else \
		echo "⚠️The .env file already deleted."; \
	fi

# Launching the app
run: install
	@echo "🚀 Launching the app..."
	@$(PYTHON) main.py

# Cleaning up the environment
clean:
	@echo "🧹 Deleting the virtual environment..."
	rm -rf $(VENV)
	@echo "✅ Cleaning is complete."

# Update certificates
certificate:
	@echo "🧹 Installing certificates..."
	@"$(PYTHON_DIR)/Install Certificates.command"
	@echo "✅ The installation is complete."


#DOCKER CMDS:

#Build docker images
build:
	@echo "Building Docker images..."
	docker-compose build

#Up Docker containers
up:
	@echo "Starting Docker containers..."
	docker-compose up -d

#Clean docker environment
docker_clean:
	@echo "Cleaning up Docker environment..."
	docker-compose down -v

restart:
	@echo "Restarting Docker containers..."
	docker-compose down -v
	docker-compose up -d

stresstest:
	@echo "Staring do heavy work...."
	$(PYTHON) client/client.py