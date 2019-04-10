
---
title: "Applying Parcellations to Resting State Data"
teaching: 30
exercises: 15
questions:
- "How can we reduce amount of noise-related variance in our data?"
- "How can we frame our data as a set of meaningful features?"
objectives:
- "Learn about the utility of parcellations as a data dimensionalty reduction tool"
- "Understand what the tradeoffs are when using parcellations to analyze your data"
keypoints:
- "Parcellations group voxels based on criteria such as similarities, orthogonality or some other criteria"
- "Nilearn stores several standard parcellations that can be applied to your data"
- "Parcellations are defined by assigning each voxel a parcel 'membership' value telling you which group the parcel belongs to" 
- "Parcellations provide an interpretative framework for understanding resting state data. But beware, some of the techniques used to form parcellations may not represent actual brain functional units!"
---

# Introduction
## What is a Brain Atlas or Parcellation? 
A brain atlas/parcellation is a voxel-based labelling of your data into "structural or functional units". In a parcellation schema each voxel is assigned a numeric (integer) label corresponding to the structural/functional unit that the particular voxel is thought to belong to based on some criteria. You might wonder why someone would simply *average together a bunch of voxels* in a way that would reduce the richness of the data. This boils down to a few problems inherit to functional brain imaging:

1. Resting state data is noisy, averaging groups of "similar" voxels reduces the effect of random noise effects
2. Provide an interpretative framework to functional imaging data. For example one parcellation group might be defined as the Default Mode Network which is thought to be functionally significant. So averaging voxels together belonging to the Default Mode Network provides an average estimate of the Default Mode Network signal. In addition the discovery of the Default Mode Network has yielded important insights into the organizational principles of the brain.
3. Limit the number of statistical tests thereby reducing potential Type I errors without resorting to strong statistical correction techniques that might reduce statistical power. 
4. A simpler way to visualize your data, instead of 40x40x40=6400 data points, you might have 17 or up to 200; this is still significantly less data to deal with!


## Applying a Parcellation to your Data
Since the parcellation of a brain is defined (currently) by spatial locations, application of an parcellation to fMRI data only concerns the first 3 dimensions; the last dimension (time) is retained. Thus a parcellation assigns every voxel (x,y,z) to a particular parcel ID (an integer). 


Nilearn supports a large selection of different atlases that can be found [here](http://nilearn.github.io/modules/reference.html#module-nilearn.datasets). For information about how to select which parcellation to use for analysis of your data we refer you to Arslan et al. 2018. 




