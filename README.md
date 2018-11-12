# scwg2018_python_neuroimaging
Scientific-Compute Working Group Workshop on performing analysis of neuroimaging data in Python

### Developed by
- Jerry Jeyachandra (https://github.com/jerdra)
- Michael Joseph (https://github.com/josephmje)

## Setting up the tutorial environment

### Getting workshop material
Go to the directory of your choice and: 
```
git clone https://github.com/jerdra/scwg2018_python_neuroimaging.git 
```

### Setting up Python environment
We use python version 3.6.0, but any newer version should also work (Python 2 versions haven't been tested). There are many methods to setting up a python environment but we'd recommend using some sort of virtual environment as to not break your system python install. Two methods (of many) are listed below: 

#### Method 1: Setting up conda environment (easiest)
For easy set-up we recommend [Anaconda](https://www.anaconda.com/download/) to manage python packages for scientific computing. Once installed, setting up the python environment can be done quite easily: 
```
cd scwg2018_python_neuroimaging
conda create -p ./scwg2018_nilearn
source activate $(pwd)/scwg2018_nilearn
conda install numpy scipy scikit-learn matplotlib jupyter ipykernel nb_conda 
conda install -c conda-forge awscli
pip install nilearn nibabel

```
#### Method 2: Using pyenv (my favourite)
An alternative method uses [pyenv](https://github.com/pyenv/pyenv) with [pyenv virtualenv](https://github.com/pyenv/pyenv-virtualenv). This is a favourite because it seamlessly integrates multiple python versions and environments into your system while maintaining use of pip (instead of conda). 
```
cd scwg2018_python_neuroimaging
pyenv virtualenv 3.6.0 scwg2018_nilearn 
echo scwg2018_nilearn > .python-version
pip install --requirement requirements.txt
```

## Acquiring the data
This tutorial uses data derived from the **UCLA Consortium for Neuropsychiatric Phenomics LA5c Study [1]**. 

To acquire the data we use [Amazon AWS S3](https://aws.amazon.com/). You can set up an account using the link. Then you'll need to set up the **awscli** python tool using your AWS account credentials (more info: [Amazon AWS CLI](https://aws.amazon.com/cli/))

To download (**warning: large download size!**) the subset of the data used for the tutorial:

```
cd scwg2018_python_neuroimaging
cat download_list | xargs -I '{}' aws s3 sync --no-sign-request s3://openneuro/ds000030/ds000030_R1.0.5/uncompressed/derivatives/fmriprep/{} ./data
```
Finally open up the jupyter notebook to explore the tutorials:
```
cd scwg2018_python_neuroimaging

#Include below line if using anaconda environment
source activate $(pwd)/scwg2018_nilearn

jupyter notebook
```

**Reference** 

[1] Gorgolewski KJ, Durnez J and Poldrack RA. Preprocessed Consortium for Neuropsychiatric Phenomics dataset [version 2; referees: 2 approved]. F1000Research 2017, 6:1262
(https://doi.org/10.12688/f1000research.11964.2)





