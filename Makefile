
.DEFAULT_GOAL := run

.PHONY: setup
setup:
	@bash scripts/virtualenv-runner.sh setup

.PHONY: test
test:
	@bash scripts/virtualenv-runner.sh test

.PHONY: coverage
coverage:
	@bash scripts/virtualenv-runner.sh coverage

.PHONY: repl
repl:
	@bash scripts/virtualenv-runner.sh repl

.PHONY: run
run:
	@bash scripts/virtualenv-runner.sh run

.PHONY: todo
todo:
	@grep -rF TODO monochat_beta tests

.PHONY: ssh
ssh:
	@gcloud compute ssh --project={YOUR_PROJECT_NAME} --zone={YOUR_ZONE} {YOUR_INSTANCE_NAME}

