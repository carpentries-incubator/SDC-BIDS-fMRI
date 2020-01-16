
---
title: "Introduction to Image Manipulation using Nilearn"
teaching: 30
exercises: 15
questions:
- "How can be perform arithmetic operations on MR images"
objectives:
- "Use Nilearn to perform masking and mathematical operations"
- "Learn how to resample across modalities for image viewing and manipulation"
keypoints:
- "MR images are essentially 3D arrays where each voxel is represented by an (i,j,k) index"
- "Nilearn is Nibabel under the hood, knowing how Nibabel works is key to understanding Nilearn"
---

# Introduction

Nilearn is a functional neuroimaging analysis and visualization library that wraps up a whole bunch of high-level operations (machine learning, statistical analysis, data cleaning, etc...) in easy-to-use commands. The neat thing about Nilearn is that it implements Nibabel under the hood. What this means is that everything you do in Nilearn can be represented by performing a set of operations on Nibabel objects. This has the important consequence of allowing you, yourself to perform high-level operations (like resampling) using Nilearn then dropping into Nibabel for more custom data processing then jumping back up to Nilearn for interactive image viewing. Pretty cool!

# Setting up

The first thing we'll do is to important some Python modules that will allow us to use Nilearn:

~~~
import os
import matplotlib.pyplot as plt
from nilearn import image as img
from nilearn import plotting as plot
from bids import BIDSLayout

#for inline visualization in jupyter notebook
%matplotlib inline 
~~~
{: .language-python}

Notice that we imported two things:
1. `image as img` - allows us to load NIFTI images using nibabel under the hood
2. `plotting as plot`- allows us to using Nilearn's plotting library for easy visualization

First let's grab some data from where we downloaded our **FMRIPREP** outputs:

~~~
#Base directory for fmriprep output
fmriprep_dir = '../data/ds000030/derivatives/fmriprep/'
layout= BIDSLayout(fmriprep_dir, validate=False)
T1w_files = layout.get(subject='10788', datatype='anat', suffix='preproc')
brainmask_files = layout.get(subject='10788', datatype='anat', suffix='brainmask')
~~~
{: .language-python}

Here we used pyBIDS (as introduced in earlier sections) to pull a single participant. Specifically, we pulled all preprocessed (MNI152NLin2009cAsym, and T1w) anatomical files as well as their respective masks. Let's quickly view these files for review:

~~~
#Display preprocessed files inside of anatomy folder
for f in T1w_files:
    print(f.path)
~~~
{: .language-python}

~~~
/mnt/tigrlab/projects/jjeyachandra/scwg2018_python_neuroimaging/data/ds000030/derivatives/fmriprep/sub-10171/anat/sub-10171_T1w_preproc.nii.gz
/mnt/tigrlab/projects/jjeyachandra/scwg2018_python_neuroimaging/data/ds000030/derivatives/fmriprep/sub-10171/anat/sub-10171_T1w_space-MNI152NLin2009cAsym_preproc.nii.gz
~~~
{: .output}

Now that we have our files set up, let's start performing some basic image operations.

## Basic Image Operations

In this section we're going to deal with the following files:

1. <code>sub-10171_T1w_preproc.nii.gz</code> - the T1 image in native space
2. <code>sub-10171_T1w_brainmask.nii.gz</code> - a mask with 1's representing the brain and 0's elsewhere.

~~~
t1 = T1w_files[0].path
bm = brainmask_files[0].path

t1_img = img.load_img(t1)
bm_img = img.load_img(bm)
~~~
{: .language-python}

Using the <code>plotting</code> module (which we've aliased as <code>plot</code>), we can view our MR image:

~~~
plot.plot_anat(t1_img)
~~~
{: .language-python}

![image-title-here](../fig/t1_img.png){:class="img-responsive"}

Try viewing the mask as well!

~~~
plot.plot_anat(bm_img)
~~~
{: .language-python}

Let's start performing some image operations. The simplest operations we can perform is **element-wise**, what this means is that we want to perform some sort of mathematical operation on each **voxel** of the MR image. Since *voxels are represented in a 3D array, this is equivalent to performing an operation on each element (i,j,k) of a 3D array*. Let's try inverting the image, that is, flip the colour scale such that all blacks appear white and vice-versa. To do this, we'll use the method

`img.math_img(formula, **imgs)`
Where:
- `formula` is a mathematical expression such as `'a+1'`
- `**imgs` is a set of key-value pairs linking variable names to images. For example `a=T1`

In order to invert the image, we can simply flip the sign which will set the most positive elements (white) to the most negatve elements (black), and the least positives elements (black) to the least negative elements (white). This effectively flips the colour-scale:

~~~
invert_img = img.math_img('-a', a=T1)
plot.plot_anat(invert_img)
~~~
{: .language-python}

![image-title-here](../fig/invert_img.png){:class="img-responsive"}

### Applying a Mask
Let's extend this idea of applying operations to each element of an image to multiple images. Instead of specifying just one image like the following:

`img.math_img('a+1',a=img_a)`

We can specify multiple images by tacking on additional variables:

`img.math_img('a+b', a=img_a, b=img_b)`

The key requirement here is that when dealing with multiple images, that the *size* of the images must be the same. The reason being is that we're deaing with **element-wise** operations. That means that some voxel (i,j,k) in `img_a` is being paired with some voxel (i,j,k) in `img_b` when performing operations. So every voxel in `img_a` must have some pair with a voxel in `img_b`; sizes must be the same.

We can take advantage of this property when masking our data using multiplication. Masking works by multipling a raw image (our `T1`), with some mask image (our `bm`). Whichever voxel (i,j,k) has a value of 0 in the mask multiplies with voxel (i,j,k) in the raw image resulting in a product of 0. Conversely, any voxel (i,j,k) in the mask with a value of 1 multiplies with voxel (i,j,k) in the raw image resulting in the same value. Let's try this out in practice and see what the result is:

~~~
masked_t1 = img.math_img('a*b', a=T1, b=bm)
plot.plot_anat(masked_T1)
~~~
{: .language-python}

![*image-title-here](../fig/masked_t1.png){:class="img-responsive"}

As you can see areas where the mask image had a value of 1 were retained, everything else was set to 0

> ## Exercise #1
> Try applying the mask such that the brain is removed, but the rest of the head is intact!
>
> > ## Solution
> > ~~~
> > inverted_mask_t1 = img.math_img('a*(1-b)', a=T1, b=bm)
> > plot.plot_anat(inverted_mask_t1)
> > ~~~
> > {: .language-python}
> > ![*image-title-here](../fig/inverted_mask_t1.png){:class="img-responsive"}
> {: .solution}
{: .challenge}

## Slicing

Recall that our data matrix is organized in the following manner:

### <INSERT IMAGE HERE>
![image-title-here](../fig/slicing.png){:class="img-responsive"}

Slicing does exactly what it seems to imply. Given our 3D volume, we can pull out 2D subsets (called "slices"). Here's an example of slicing moving from left to right via an animated GIF:

### <INSERT IMAGE HERE>
![image-title-here](../fig/animated_slicing.png){:class="img-responsive"}

What you see here is a series of 2D images that start from the left, and move toward the right. Each frame of this GIF is a slice - a 2D subset of a 3D volume. Slicing can be useful for cases in which you'd want to loop through each MR slice and perform a computation; importantly in functional imaging data slicing is useful for pulling out timepoints as we'll see later!

> Sourced from: https://en.wikipedia.org/wiki/Neuroimaging#/media/File:Parasagittal_MRI_of_human_head_in_patient_with_benign_familial_macrocephaly_prior_to_brain_injury_(ANIMATED).gif
{: .callout}

Slicing is done easily on an image file using the attribute <code>.slicer</code> of a Nilearn <code>image</code> object. For example we can grab the $10^{\text{th}}$ slice along the x axis as follows:

~~~
x_slice = t1_img.slicer[10:11,:,:]
~~~
{: .language-python}

The statement $10:11$ is intentional and is required by <code>.slicer</code>. Alternatively we can slice along the x-axis using the data matrix itself:

~~~
t1_data = t1_img.get_data()
x_slice = t1_data[10,:,:]
~~~
{: .language-python}

This will yield the same result as above. Notice that when using the <code>t1_data</code> array we can just specify which slice to grab instead of using <code>:</code>. We can use slicing in order to modify visualizations. For example, when viewing the T1 image, we may want to specify at which slice we'd like to view the image. This can be done by specifying which coordinates to *cut* the image at:

~~~
plot.plot_anat(t1_img,cut_coords=(50,30,70))
~~~
{: .language-python}

The <code>cut_coords</code> option specifies 3 numbers:
- The first number says cut the X coordinate at slice 50 and display (sagittal view in this case!)
- The second number says cut the Y coordinate at slice 30 and display (coronal view)
- The third number says cut the Z coordinate at slice 70 and display (axial view)

Remember <code>plot.plot_anat</code> yields 3 images, therefore <code>cut_coords</code> allows you to display where to take cross-sections of the brain from different perspectives (axial, sagittal, coronal)


This covers the basics of image manipulation using T1 images. To review in this section we covered:

- Basic image arithmetic
- Visualization
- Slicing

In the next section we will cover how to integrate additional modalities (functional data) to what we've done so far using <code>Nilearn</code>. Then we can start using what we've learned in order to perform analysis and visualization!
