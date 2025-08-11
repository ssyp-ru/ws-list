add_submodules_from_readme:
	python3 scripts/add_submodules.py

download_project_backup:
	git submodule update --init --remote