run:
	@python job_finder_package_folder/main.py

run_uvicorn:
	@uvicorn job_finder_package_folder.api:app --reload

install:
	@pip install -e .

test:
	@pytest -v tests
