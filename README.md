# Scientific Computing Working Group Workshop on performing analysis of neuroimaging data in Python

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jerdra/SDC-BIDS-fMRI/master)

### Developed by
- Jerry Jeyachandra (https://github.com/jerdra)
- Michael Joseph (https://github.com/josephmje)
- Olivia Stanley (https://github.com/ostanley)
- Jason Kai (https://github.com/kaitj)

## Getting workshop material for SciNet workshops

*** 

### If you're using SciNet's Jupyter System

[Instructions with pictures](https://docs.google.com/document/d/1MyxIMtknK8In_D43--GOdBfqb25KEWX9NMzXYHoMq30/edit?usp=sharing)

Open up a terminal and enter the following:
```bash
  ssh <user>@teach.scinet.utoronto.ca
  module load anaconda3
  source /scinet/course/ss2019/3/6_mripython/setup_workshop
  python -m ipykernel install --user --name mripython_conda
```

Open a new terminal and enter the following:
```bash
  ssh -L 8888:jupyterhub<X>:8000 <user>@teach.scinet.utoronto.ca -N
```

Where `<X>` is a number between 1-6. 

If nothing happens that's great! Now open up your favourite browser and enter the following in your address bar:

```
  https://localhost:8888
```

You're ready to go!

***

### If you're using Binder

Click the following button:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jerdra/SDC-BIDS-fMRI/master)

This will open up a jupyter terminal for you. Then just hit:

- **New** --> **Terminal** 

This will open up a terminal. Once you're in here type the following:

```
./setup_workshop
```

Then leave it running in the background and switch tabs over back to the previous tab (says "Home" on Chrome)



***
***
***

### Getting workshop material for CAMH Workshops

#### Method 1: Downloading directly from the repository 

On the GitHub repo (this page), click the green button that says "Clone or download", then click **Download ZIP**. Once downloaded, extract the ZIP file.

#### Method 2: Using Git

Using this method requires a (very) useful piece of software called <code>git</code>. The process of installing git depends heavily on whether you're using MacOS, Windows or Linux. Follow the instructions in the link below to set up <code>git</code> on your PC:

[Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

Once you've installed <code>git</code>, open up your terminal and do the following:

```
git clone https://github.com/jerdra/SDC-BIDS-fMRI.git
```

This will download the repository directly into your current directory. 

### Setting up Python environment
We use python version 3.6.0, but any newer version should also work (Python 2 versions haven't been tested). There are many methods to setting up a python environment but we'd recommend using some sort of virtual environment as to not break your system python install. Two methods (of many) are listed below:

#### Method 1: Setting up conda environment (easiest) [Windows, Linux, MacOS]
For easy set-up we recommend [Anaconda](https://www.anaconda.com/download/) to manage python packages for scientific computing. Once installed, setting up the python environment can be done quite easily:

##### Windows
1. Install Anaconda Python version 3.7
2. Open **Anaconda Navigator**
3. Click on **Environments** on the left pane
4. Click **Create** then type in <code>SDC-BIDS-fMRI</code>
5. In the <code>SDC-BIDS-fMRI</code> entry click the play button then click **Open Terminal** 
6. In terminal type: 
```
conda install -y numpy pandas scipy scikit-learn matplotlib jupyter ipykernel nb_conda
conda install -y -c conda-forge awscli
pip install nilearn nibabel
./setup_workshop
```
7. Close the terminal, click on the play button again and open **Jupyter Notebook**
8. Navigate to <code>SDC-BIDS-fMRI</code> folder you downloaded earlier.
9. Done!

##### Linux and MacOS

After installing Anaconda, open terminal and type: 

```
cd SDC-BIDS-fMRI
conda create -p ./sdc_bids_fmri
source activate $(pwd)/sdc_bids_fmri
conda install numpy pandas scipy scikit-learn matplotlib jupyter ipykernel nb_conda
conda install -c conda-forge awscli
pip install nilearn nibabel
./setup_workshop
```
#### Method 2: Using pyenv (my favourite) [Linux, MacOS]
An alternative method uses [pyenv](https://github.com/pyenv/pyenv) with [pyenv virtualenv](https://github.com/pyenv/pyenv-virtualenv). This is a favourite because it seamlessly integrates multiple python versions and environments into your system while maintaining use of pip (instead of conda).
```
cd SDC-BIDS-fMRI
pyenv virtualenv 3.6.0 sdc_bids_fmri
echo sdc_bids_fmri > .python-version
pip install --requirement requirements.txt
./setup_workshop
```

Finally open up the jupyter notebook to explore the tutorials:
```
cd SD-BIDS-fMRI

#Include below line if using anaconda environment
source activate $(pwd)/sdc_bids_fmri

jupyter notebook
```

**Reference**

[1] Gorgolewski KJ, Durnez J and Poldrack RA. Preprocessed Consortium for Neuropsychiatric Phenomics dataset [version 2; referees: 2 approved]. F1000Research 2017, 6:1262
(https://doi.org/10.12688/f1000research.11964.2)
