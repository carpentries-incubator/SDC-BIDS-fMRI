# scwg2018_python_neuroimaging
Scientific Computing Working Group Workshop on performing analysis of neuroimaging data in Python

### Developed by
- Jerry Jeyachandra (https://github.com/jerdra)
- Michael Joseph (https://github.com/josephmje)

## Setting up the tutorial environment

### Getting workshop material
To get the workshop material on this page you'll need a (very) useful piece of software called <code>git</code>. The process of installing git depends heavily on whether you're using MacOS, Windows or Linux. Follow the instructions in the link below to set up <code>git</code> on your PC:

[Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

Once you've installed <code>git</code>, open up your terminal and do the following:

```
git clone https://github.com/jerdra/scwg2018_python_neuroimaging.git
```

### Setting up Python environment
We use python version 3.6.0, but any newer version should also work (Python 2 versions haven't been tested). There are many methods to setting up a python environment but we'd recommend using some sort of virtual environment as to not break your system python install. Two methods (of many) are listed below:

#### Method 1: Setting up conda environment (easiest) [Windows, Linux, MacOS]
For easy set-up we recommend [Anaconda](https://www.anaconda.com/download/) to manage python packages for scientific computing. Once installed, setting up the python environment can be done quite easily:

##### Windows
1. Install Anaconda 
2. Open the Anaconda Navigator
3. Click on Environments on the right pane
4. Click create then type in 'scwg2018_python_neuroimaging' 
5. In the scwg2018_python_neuroimaging entry click the play button then 'Open Terminal' 
6. In terminal type: 
```
conda install numpy pandas scipy scikit-learn matplotlib jupyter ipykernel nb_conda
conda install -c conda-forge awscli
pip install nilearn nibabel
```
7. Close the terminal, click on the play button again and open Jupyter Notebook
8. Navigate to scwg2018_python_neuroimaging folder you cloned on git. 
9. Done!

##### Linux and MacOS

After installing Anaconda, open terminal and type: 

```
cd scwg2018_python_neuroimaging
conda create -p ./scwg2018_nilearn
source activate $(pwd)/scwg2018_nilearn
conda install numpy pandas scipy scikit-learn matplotlib jupyter ipykernel nb_conda
conda install -c conda-forge awscli
pip install nilearn nibabel

```
#### Method 2: Using pyenv (my favourite) [Linux, MacOS]
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
```
aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: ca-central-1
Default output format [None]: ENTER
```
To download (**warning: large download size!**) the subset of the data used for the tutorial:

```
cd scwg2018_python_neuroimaging

# download T1w scans
cat ../download_list | \
  xargs -I '{}' aws s3 sync --no-sign-request \
  s3://openneuro/ds000030/ds000030_R1.0.5/uncompressed/{}/anat \
  ../data/ds000030/{}/anat

# download resting state fMRI scans
cat ../download_list | \
  xargs -I '{}' aws s3 sync --no-sign-request \
  s3://openneuro/ds000030/ds000030_R1.0.5/uncompressed/{}/func \
  ../data/ds000030/{}/func \
  --exclude '*' \
  --include '*task-rest_bold*'

# download fmriprep preprocessed anat data
cat ../download_list | \
  xargs -I '{}' aws s3 sync --no-sign-request \
  s3://openneuro/ds000030/ds000030_R1.0.5/uncompressed/derivatives/fmriprep/{}/anat \
  ../data/ds000030/derivatives/fmriprep/{}/anat

# download fmriprep preprocessed func data
cat ../download_list | \
  xargs -I '{}' aws s3 sync --no-sign-request \
  s3://openneuro/ds000030/ds000030_R1.0.5/uncompressed/derivatives/fmriprep/{}/func \
  ../data/ds000030/derivatives/fmriprep/{}/func \
  --exclude '*' \
  --include '*task-rest_bold*'
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
