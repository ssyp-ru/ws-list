add_submodules_from_readme:
	python3 scripts/add_submodules.py --exclude ssyp18-ws07

download_project_backup:
	git submodule update --init --remote