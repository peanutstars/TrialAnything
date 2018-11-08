
DATE        := $(shell date +%Y%m%d-%H%M%S)
REQUIRE_TXT := requirements.txt


all:


clean:
	@find $(PROJECT_ROOT) -name __pycache__ -exec rm -rf {} \;

tar: clean
	@(cd $(PROJECT_ROOT)/.. ; tar czvf pystagram-$(DATE).tgz pystagram)

freeze:
	@$(VIRTUAL_ENV)/bin/pip freeze > $(REQUIRE_TXT)

setup:
	@$(VIRTUAL_ENV)/bin/pip install -r $(REQUIRE_TXT)


.PHONY: clean tar freeze
