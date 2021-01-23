.PHONY: format genex install

format:
	@black -l 79 ./examples

genex:
	@source "venv/bin/activate"
	@for i in examples/*.py; do python $$i; done

install:
	@mkdir ~/.matplotlib/stylelib || \
		echo "Directory already exists. Skip creation"
	@rm ~/.matplotlib/stylelib/textbook.mplstyle || \
		echo "Dir empty. Skipping delete"
	@cp ./style/textbook.mplstyle ~/.matplotlib/stylelib/textbook.mplstyle && \
		echo "File successfully copied"

