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


