
all: build


help:
	    @echo "    clean"
			@echo "        Remove executable."
	    @echo "    clean-pyc"
			@echo "        Remove python artifacts."
			@echo "    clean-build"
			@echo "        Remove build artifacts."
			@echo "    build"
			@echo "        Create executable"
			@echo '    run'
			@echo '        Run the program.'

clean:
			rm conta-caminhos

clean-pyc:
	    find . -name '*.pyc' -exec rm --force {} +
			find . -name '*.pyo' -exec rm --force {} +
			find . -name '*~' -exec rm --force  {} +

clean-build:
	    rm --force --recursive build/
			rm --force --recursive dist/
			rm --force --recursive *.egg-info

build:
			@echo "Inicializando..."
			@cp cria_conta-caminhos.py conta-caminhos
			@chmod +x conta-caminhos
			@echo "Finalizando..."

run:
	    python cria_conta-caminhos.py

