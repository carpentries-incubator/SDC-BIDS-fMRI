---
title: "Preprocessing fMRI Data"
teaching: 30
exercises: 0
questions:
- "What are the standard preprocessing steps?"
- "What existing pipelines help with preprocessing?"
objectives:
- "Understand the common preprocessing steps"
keypoints:
- "fmriprep takes care of several of the preprocessing steps"
---

## Preprocessing Steps

### T1w Preprocessing

### Despiking

### Motion Correction

### Slice Timing Correction

### Susceptibility Distortion Correction

### Artifact and Structured Noise Removal

### Volume Censoring (Scrubbing)

### Bandpass Filtering

### Spatial Smoothing

### Normalization

### Using fmriprep
[fmriprep](https://fmriprep.readthedocs.io/en/stable/) is a package developed by the Poldrack lab to do the minimal preprocessing of fMRI data required. It covers brain extraction, motion correction, field unwarping, and registration. It uses a combination of well-known software packages (e.g., FSL, SPM, ANTS, AFNI) and selects the 'best' implementation of each preprocessing step.
Once installed, `fmriprep` can be invoked from the command line. We can even run it inside this notebook! The following command should work after you remove the 'hashtag' `#`.
However, running fmriprep takes quite some time (we included the hashtag to prevent you from accidentally running it). You'll most likely want to run it in parallel on a computing cluster.
