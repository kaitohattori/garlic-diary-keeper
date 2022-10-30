install-dependencies: ## Install dependencies
	pip install -r requirements.txt

lint: ## Run lint
	flake8 ./

run: ## Run app
	python src/garlic_diary_keeper/main.py

help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
