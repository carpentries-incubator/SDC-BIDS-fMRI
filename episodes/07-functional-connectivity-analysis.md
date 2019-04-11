---
title: "Functional Connectivity Analysis"
teaching: 30
exercises: 15
questions:
- "How can we estimate brain functional connectivity patterns from resting state data?"
objectives:
- "Use parcellations to reduce fMRI noise and speed up computation of functional connectivity"
- "
keypoints:
- "MR images are essentially 3D arrays where each voxel is represented by an (i,j,k) index"
- "Nilearn is Nibabel under the hood, knowing how Nibabel works is key to understanding Nilearn"
---

# Introduction

Now we have an idea of three important components to analyzing neuroimaging data:

1. Data manipulation
2. Cleaning and confound regression
3. Parcellation and signal extraction

In this notebook the goal is to integrate these 3 basic components and perform a full analysis of group data using **Intranetwork Functional Connectivity (FC)**. 

Intranetwork functional connectivity is essentially a result of performing correlational analysis on mean signals extracted from two ROIs. Using this method we can examine how well certain resting state networks, such as the **Default Mode Network (DMN)**, are synchronized across spatially distinct regions. 

ROI-based correlational analysis forms the basis of many more sophisticated kinds of functional imaging analysis.

## PART A NECESSARY?
## Lesson Outline

The outline of this lesson is divided into two parts. The first part directly uses what you've learned and builds upon it to perform the final functional connectivity analysis on group data. 

The second part shows how we can use Nilearn's convenient wrapper functionality to perform the same task with *significantly less effort*. 

#### Part A: Manual computation 
1. Functional data cleaning and confound regression
2. Applying a parcellation onto the data
3. Computing the correlation between two ROI time-series


#### Part B: Using Nilearn's high-level features
1. Using NiftiLabelsMasker to extract cleaned time-series
2. Computing the correlation between two ROI time-series
3. Performing analysis on all subjects
4. Visualization of final results

## Using Nilearn's High-level functionality to compute correlation matrices

Nilearn has built in functionality for applying a parcellation to a functional image, cleaning the data, and computng the mean all in one step. First let's get our functional data and our parcellation file:

~~~
import os
from nilearn import signal as sgl
from nilearn import image as img
from nilearn import plotting as plot
from nilearn import datasets
import nibabel as nib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import bids
%matplotlib inline
~~~
{: .language-python}


First let's grab the data that we want to perform our connectivity analysis on using PyBIDS:

~~~
layout = bids.layout.BIDSLayout('../data/ds000030/')
subjets = layout.get_subjects()
~~~
{: .language-python}

Now that we have a list of subjects to peform our analysis on, let's load up our parcellation template file:

~~~
#Load separated parcellation
parcel_file = '../resources/rois/yeo_2011/Yeo_JNeurophysiol11_MNI152/relabeled_yeo_atlas.nii.gz' 
yeo_7 = img.load_img(parcel_file)
~~~
{: .language-python}

With all our files loaded, we first create a `input_data.NiftiLabelsMasker` object.

~~~
from nilearn import input_data


masker = input_data.NiftiLabelsMasker(labels_img=yeo_7,
                                      standardize=True,
                                      memory='nilearn_cache',
                                      verbose=1,
                                      detrend=True,
                                     low_pass = 0.08,
                                     high_pass = 0.009,
                                     t_r=2)
~~~
{: .language-python}

The `input_data.NiftiLabelsMasker` object is a wrapper that applies parcellation, cleaning and averaging to an functional image. For example let's apply this to our first subject: 


~~~
~~~
