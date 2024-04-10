LeU Documentation
=======================================

LeU Documentation is based on ReadTheDocs and GitHub. When push/merge on master is done, new documentation version is generated on ReadTheDocs and can be accessed using this link:

https://leu.readthedocs.io/it/latest/

On local machine follow this steps to clone repository and genrate documentation:

- clone repository:
  .. code-block:: console
    git clone https://github.com/kemosh/leu
- install python requirements:
  pip install -r requirements.txt
- run sphinx:
  - cd docs
  - make html

