---
title: "Instructor Notes"
---

## Scope of Lesson

The primary objective of this workshop is to introduce learners to basic fMRI concepts and to demonstrate an end-to-end analysis of functional imaging data using Python. The lessons are designed to walk a learner through each step of the fMRI analysis process with a series of hands-on notebooks.

Although the primary learning path presented is focused in on Resting State connectivity analyses, we recognize that it does not cover the vast scope of functional imaging analyses. As such, this workshop will be updated with modules (i.e task GLM) that will provide learners and instructors with additional learning paths. If you're interested in proposing a sub-module/learning path for this workshop feel free to contact the workshop developers on the GitHub [discussion board for this workshop](https://github.com/carpentries-incubator/SDC-BIDS-fMRI/discussions).

## Learner Pre-requisites

Intro to fMRI analyses is meant to be taught as part of a broader Neuroimaging carpentries lesson. As such, it makes some basic assumptions (although we provide very quick overviews) of concepts taught in the pre-requisite workshop: [Intro to MRI](https://carpentries-incubator.github.io/SDC-BIDS-IntroMRI/). In addition, we expect learners to have some basic familiarity with Python (Software Carpentries provides such a [workshop](https://swcarpentry.github.io/python-novice-inflammation/)).

In summary the core pre-requisites that we expect learners to have some familiarity with are the following:
- Basic Python programming knowledge
- [DataLad](datalad.org)
- [BIDS](bids.neuroimaging.io) and the pyBIDS for querying BIDS datasets
- Introductory knowledge about NIFTI data: header, affine, array data, voxel resolution

## Lesson Design for Instructors

### Teaching Style

This workshop as originally designed to be a live-coding session where learners are walked through the process of cleaning and analyzing resting state fMRI data. To this end, all lessons in the carpentries have a mirror Jupyter Notebook codebook. Jupyter Notebooks can be found in [the code directory of the git repo](https://github.com/carpentries-incubator/SDC-BIDS-fMRI/tree/gh-pages/code). Each episode in `code/` mirrors the corresponding episode in the workshop's carpentries site. 

In addition, we provide two versions of each notebook i.e:

- `02-exploring_fmriprep.ipynb`
- `02-exploring_fmriprep_solutions.ipynb`

The notebook with a `_solutions` suffix contains pre-filled cells that can be used by the instructor as a reference when live-coding. In addition, any learners falling/running into issues may also reference the solutions noteobok to catch-up to the instructor.

The notebook without the `_solutions` suffix ("workshop notebook") is mostly blank (aside from boilerplate code, and markdown text) and serves as the platform on which live-coding occurs. In addition, any exercise in the workshop notebook may contain template code that learners are expected to complete in a fill-in-the-blanks style problem.

### A note on Episode 01 and Companion slides

[Episode-01]({{relative-root_path}}/{% link _episodes/01-intro-and-preprocessing.md %}) provides an overview of the course material as well a coarse overview of fMRI preprocessing. These originally derive from a set of [Slides](https://docs.google.com/presentation/d/1er6dQcERL-Yeb5-7A29tJnmqgHNaLpTLXM3e-SmpjDg/edit#slide=id.g484812a0c7_6_1) which may be used in lieu of Episode 01 when teaching. 

Talking points for the slides can be found in [Episode-01]({{relative-root_path}}/{% link _episodes/01-intro-and-preprocessing.md %}).

### Tips for hosting a successful workshop

- From experience, the most difficult component of the workshop is the set-up process. It is highly recommended that learners use the [workshop's Binder image](https://mybinder.org/v2/gh/carpentries-incubator/SDC-BIDS-fMRI/gh-pages). It may be useful to set up a separate time-slot to focus on local set-up after the main workshop. 
- It is often helpful (wherever possible) to have multiple screens on display during the workshop:
	- one with the workshop live-coding notebook
	- one with a solutions notebook
	- This is helpful for learners falling behind
- This workshop is _sequentially dependent_, if learners fail to run a preceding code block they will not be able to run subsequent blocks causing frustration. Try to ensure that any issues from learners get resolved as soon as it is brought up
- We recommend additional helpers be available during teaching of the workshop. It is often easier to keep the pace/timing of the workshop when a helper is available to address minor issues learners may run into

### Frequent Issues

- None as of now, this will be updated with additional piloting of the workshop



{% include links.md %}
