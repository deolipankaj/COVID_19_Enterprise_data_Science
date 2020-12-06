eds
==============================

enyterprise data science project on COVID-19 data

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------
	Applied Data science Project.
	
	Dataset used - John Hopkins Dataset
	Libraries used - Plotly, Scikit learn
	
	Language used - Python
	
	About the project: An analysis of the corona cases of different countries around the globe, the doubling rate associated and the general trend.
			    Alongwith this, implementation of SIR (Susceptible population, Infectious population and Recovered population) for Germany


	How to use the contents:
	
	1. To run the dynamic dashboard, simply clone then repository -> go to src/visualisation/visualize.py
	2. To run the SIR model for Germany - Run SIR_model.py

# A Sneak peek of the project

1. Timeline Confirmed
<img src="Timeline_confirmed.gif">

2. Timeline Confirmed Filtered
<img src = "Timeline_confirmed_filtered.gif">

3. Timeline Doubling Rate
<img src="Timeline_doubling_rate.gif">

4. Timeline Doubling Rate Filtered
<img src="Timeleine_doubling_rate_filtered.gif">