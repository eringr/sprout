
.PHONY: test
test:
	python3 -m unittest

.PHONY: example
example:
	./bin/sprout -C examples/hello
