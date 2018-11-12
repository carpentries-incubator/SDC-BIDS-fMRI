# scwg2018_python_neuroimaging
Scientific-Compute Working Group Workshop on performing analysis of neuroimaging data in Python
Developed by Jerry Jeyachandra and Michael Joseph

### Setting up the tutorial environment

#### Getting workshop material
Go to the directory of your choice and: 
```
git clone https://github.com/jerdra/scwg2018_python_neuroimaging.git 
```

#### Setting up Python environment
We use python version 3.6.0, but any newer version should also work well! Any python version below 3 has not been tested. There are many methods to setting up a python environment but we'd recommend using some sort of virtual environment as to not break your system python install. Two methods (of many) are listed below: 

##### Method 1: Setting up conda environment (easiest)
This tutorial uses [Anaconda](https://www.anaconda.com/download/) to manage python packages for scientific computing. To set up: 
```
cd scwg2018_python_neuroimaging
conda create -p ./scwg2018_nilearn
source activate $(pwd)/scwg2018_nilearn
conda install numpy scipy scikit-learn matplotlib jupyter ipykernel nb_conda 
conda install -c conda-forge awscli
pip install nilearn nibabel

```
##### Method 2: Using pyenv (my favourite)
This set-up assumes you've already set up [pyenv](https://github.com/pyenv/pyenv) with [pyenv virtualenv](https://github.com/pyenv/pyenv-virtualenv):
```
cd scwg2018_python_neuroimaging
pyenv virtualenv 3.6.0 scwg2018_nilearn 
echo scwg2018_nilearn > .python-version
pip install --requirement requirements.txt
```

#### Acquiring the data
This tutorial uses data derived from the **UCLA Consortium for Neuropsychiatric Phenomics LA5c Study**. 

**Reference** 

Gorgolewski KJ, Durnez J and Poldrack RA. Preprocessed Consortium for Neuropsychiatric Phenomics dataset [version 2; referees: 2 approved]. F1000Research 2017, 6:1262
(https://doi.org/10.12688/f1000research.11964.2)

To acquire the data we use [Amazon AWS CLI](https://aws.amazon.com/cli/). You can set up and configure the **awscli** python tool using instructions from here: https://aws.amazon.com/. 

To download (**be aware of large download size!**) the subset of the data used for the tutorial:

```
cd scwg2018_python_neuroimaging
cat download_list | xargs -I '{}' aws s3 sync --no-sign-request s3://openneuro/ds000030/ds000030_R1.0.5/uncompressed/derivatives/fmriprep/{} ./data
```
Finally open up the jupyter notebook to explore the tutorial:
```
cd scwg2018_python_neuroimaging
#If using anaconda
source activate $(pwd)/scwg2018_nilearn
jupyter notebook
```





