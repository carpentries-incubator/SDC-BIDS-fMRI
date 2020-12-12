# Introduction to fMRI Analysis in Python

[![Create a Slack Account with us](https://img.shields.io/badge/Create_Slack_Account-The_Carpentries-071159.svg)](https://swc-slack-invite.herokuapp.com/)
[![Slack Status](https://img.shields.io/badge/Slack_Channel-neuroimaging-E01563.svg)](https://swcarpentry.slack.com/messages/CCJBHKCHZ)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/carpentries-incubator/SDC-BIDS-fMRI/gh-pages)

## Background

This is one sub-module within the [Neuroimaging cirriculum][neuro_cirriculum]. Visit the link to view all the modules associated with the Neuroimaging Carpentries program.

**fMRI Analysis in Python** is a programme developed to facilitate reproducibility in functional neuroimaging analyses. Python is emerging as a standard language of data analysis, visualization, and workflow building. More recently, it has rapidly been adopted by the neuroimaging community as a means of developing powerful open-source tools in favour of historically used opaque software such as AFNI, FSL and SPM. In addition, the barrier to entry to Python is low - meaning that you as the user can easily develop your own packages and contribute to the open-source codebase of neuroimaging!


***

The **fMRI Analysis in Python** is a workshop series started up via a collaboration between researchers and staff at the Centre for Addiction and Mental Health (Toronto, ON), the University of Western Ontario (London, Ontario), and McGill University (Montreal, Quebec).

***

## About the lesson

This lesson covers fMRI imaging analysis from the basic steps of preprocessing and data cleaning, to running an analysis, to exploring connectivity patterns in the brain.

### Episodes

| Time | Episode | Question(s) Answered |
| ---  | ---     | ---                  |
||Setup|Download files required for the lesson|
| 00:00 | 1. Preprocessing fMRI data  | Raw fMRI data is unsuable, what steps should one take before using their fMRI data? |
| 00:25 | 2. Exploring Preprocessed fMRI Data from fMRIPREP | How does fMRIPrep store preprocessed neuroimaging data. How do I access preprocessed neuroimaging data  |
| 00:50 | 3. Introduction to Image Manipulation using Nilearn | How can we perform arithmetic operations on MR images |
| 01:25 | 4. Integrating Functional Data  | How is fMRI data represented. How can we access fMRI data along spatial and temporal dimensions. How can we integrate fMRI and structural MRI together |
| 01:50 | 5. Cleaning out potential confounds | How I ensure that my signal better represents brain signal rather than motion artifacts?  |
| 02:10 | 6. Cleaning Confounders in your Data with Nilearn | How can we clean the data so that it more closely reflects BOLD instead of artifacts  |
| 02:45 | 7. Applying Parcellations to Resting State Data | How can we reduce amount of noise-related variance in our data? How can we frame our data as a set of meaningful features?  |
| 03:15 | 8. Functional Connectivity Analysis | How can we estimate brain functional connectivity patterns from resting state data? |
| 04:00 | Finish | |
 

## Contributing

We welcome all contributions to improve the lesson! Maintainers will do their best to help you if you have any
questions, concerns, or experience any difficulties along the way.

We'd like to ask you to familiarize yourself with our [Contribution Guide](CONTRIBUTING.md) and have a look at
the [more detailed guidelines][lesson-example] on proper formatting, ways to render the lesson locally, and even
how to write new episodes.

Please see the current list of [issues](https://github.com/carpentries-incubator/SDC-BIDS-fMRI/issues) for ideas for contributing to this
repository. For making your contribution, we use the GitHub flow, which is
nicely explained in the chapter [Contributing to a Project](http://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project) in Pro Git
by Scott Chacon.
Look for the tag ![good_first_issue](https://img.shields.io/badge/-good%20first%20issue-gold.svg). This indicates that the mantainers will welcome a pull request fixing this issue.


## Maintainer(s)

* [Jerrold Jeyachandra][jerrold_jeyachandra]
* [Michael Joseph][michael_joseph]
* [Olivia Stanley][olivia_stanley]
* [Jason Kai][jason_kai]
* [Erin Dickie][erin_dickie]

## Authors

A list of contributors to the lesson can be found in [AUTHORS](AUTHORS)

## Citation

To cite this lesson, please consult with [CITATION](CITATION)

[lesson-example]: https://carpentries.github.io/lesson-example
[jerrold_jeyachandra]: https://github.com/jerdra
[olivia_stanley]: https://github.com/ostanley
[michael_joseph]: https://github.com/josephmje
[jason_kai]: https://github.com/kaitj
[erin_dickie]: https://github.com/edickie
[neuro_cirriculum]: https://carpentries.org/community-lessons/#neuroimaging
