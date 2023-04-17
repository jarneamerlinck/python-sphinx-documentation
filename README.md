# Python-sphinx-documentation

Template to document code with sphinx.
install package ```pip install packagename_jarne```

## Create documentation

1. Update files to fit the new package

- Change ```packagename_jarne``` to the new packagename
- Change version in ```packagename_jarne/version```
- Update ```setup.py```
- Update sources for Sphinx
  - ```docs/source/conf.py```
  - rst files


1. Install package with conda

```conda env create -f environment.yml```

2. Make documentation

- ```conda env create -f environment_build.yml; conda activate conda-env-name-build;cd docs;make html;cd ..```
- ```make html```
  - alternatives ```make help```

## Add new python files

1. Add files in package folder ```packagename_jarne``` (or the new name)
2. Add links to the python files in ```docs/source/```
3. Make [Documentation](#create-documentation) (see above)

## Upload to pipy requirements

- add ```PYPI_TOKEN``` to github secrets
