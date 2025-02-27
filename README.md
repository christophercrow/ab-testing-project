README.md

# A/B Testing and Experimentation Project

This repository implements a robust A/B testing framework to evaluate the impact of targeted UI modifications on user behavior. The project uses Python for data extraction, SQL for querying a PostgreSQL database, and Statsmodels for statistical analysis.

## Project Structure

- **data/**: Contains raw or sample datasets.
- **notebooks/**: Jupyter notebooks for exploratory analysis.
- **src/**: Source code modules.
  - `data_extraction.py`: Handles database connections and data retrieval.
  - `analysis.py`: Contains functions for running statistical tests.
  - `experiment.py`: Main script to run the entire pipeline.
- **tests/**: Contains unit tests for the project.
- **requirements.txt**: Python dependencies.
- **.gitignore**: Files/folders to ignore in Git.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ab-testing-project.git
   cd ab-testing-project

Set up the virtual environment and install dependencies:

	python3 -m venv venv
	source venv/bin/activate  # On Windows: venv\Scripts\activate
	pip install -r requirements.txt

Configure your database connection in src/data_extraction.py.

Run the experiment:

	python src/experiment.py
