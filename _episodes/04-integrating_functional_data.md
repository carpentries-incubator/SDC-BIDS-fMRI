---
title: "Integrating Functional Data"
teaching: 30
exercises: 15
questions:
- "How is fMRI data represented"
- "How can we access fMRI data along spatial and temporal dimensions"
- "How can we integrate fMRI and structural MRI together"
objectives:
- "Extend the idea of slicing to 4 dimensions"
- "Apply resampling to T1 images to combine them with fMRI data"
keypoints:
- "fMRI data is represented by spatial (x,y,z) and temporal (t) dimensions, totalling 4 dimensions"
- "fMRI data is at a lower resolution than structural data. To be able to combine data requires resampling your data"
---

# Integrating Functional Data

So far most of our work has been examining anatomical images - the reason being is that it provides a nice visual way of exploring the effects of data manipulation and visualization is easy. In practice, you will most likely not analyze anatomical data using <code>nilearn</code> since there are other tools that are better suited for that kind of analysis (freesurfer, connectome-workbench, mindboggle, etc...). 

In this notebook we'll finally start working with functional MR data - the modality of interest in this workshop. First we'll cover some basics about how the data is organized (similar to T1s but slightly more complex), and then how we can integrate our anatomical and functional data together using tools provided by <code>nilearn</code>

Functional data consists of full 3D brain volumes that are *sampled* at multiple time points. Therefore you have a sequence of 3D brain volumes, stepping through sequences is stepping through time and therefore time is our 4th dimension! Here's a visualization to make this concept more clear:

![4D Array Representation](../fig/4D_array.png){:class="img-responsive"}

Each index along the 4th dimensions (called TR for "Repetition Time", or Sample) is a full 3D scan of the brain. Pulling out volumes from 4-dimensional images is similar to that of 3-dimensional images except you're now dealing with:


<code> nimg.slicer[x,y,z,time] </code>!

Let's try a couple of examples to familiarize ourselves with dealing with 4D images. But first, let's pull some functional data using PyBIDS!

~~~
import os
import matplotlib.pyplot as plt #to enable plotting within notebook
from nilearn import image as nimg
from nilearn import plotting as nplot
from bids.layout import BIDSLayout
import numpy as np
%matplotlib inline
~~~
{: .language-python}

These are the usual imports. Let's now pull some structural *and* functional data using pyBIDS:

~~~
fmriprep_dir = '../data/ds000030/derivatives/fmriprep/'
layout=BIDSLayout(fmriprep_dir, validate=False)
T1w_files = layout.get(subject='10788', datatype='anat', suffix='preproc')
brainmask_files = layout.get(subject='10788', datatype='anat', suffix='brainmask')
func_files = layout.get(subject='10788', datatype='func', suffix='preproc')
func_mask_files = layout.get(subject='10788', datatype='func', suffix='brainmask')
~~~
{: .language-python}

We'll be using functional files in MNI space rather than T1w space. Recall, that MNI space data is data that was been warped into standard space. These are the files you would typically use for a group-level functional imaging analysis!

~~~
func_mni = func_files[1].path
func_mni_img = nimg.load_img(func_mni)
~~~
{: .language-python}

## fMRI as a time-series signal

First note that fMRI data contains both spatial dimensions (x,y,z) and a temporal dimension (t). This would mean that we require 4 dimensions in order to represent our data. Let's take a look at the shape of our data matrix to confirm this intuition:

~~~
func_mni_img.shape
~~~
{: .language-python}

~~~
(60, 86, 65, 152)
~~~
{: .output}

Notice that the Functional MR scan contains *4 dimensions*. This is in the form of $(x,y,z,t)$, where $t$ is time. 
We can use slicer as usual where instead of using 3 dimensions we use 4. 

For example:

<code> func.slicer[x,y,z] </code> 

vs.

<code> func.slicer[x,y,z,t] </code>


> ## Exercise
> 
> Try pulling out the 5th TR and visualizing it using <code>nplot.plot_epi</code>. <code>plot_epi</code> is exactly the same as <code>plot_anat</code> except it displays using colors that make more sense for functional images...
> 
> > ~~~
> > #Pull the 5th TR
> > func_vol5 = func_mni_img.slicer[:,:,:,4]
> > nplot.plot_epi(func_vol5)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}


![Visual of fMRI EPI Data](../fig/fmri_data.png){:class="img-responsive"}

## What fMRI actually represents

We've represented fMRI as a snapshot of MR signal over multiple timepoints. This is a useful way of understanding the organization of fMRI, however it isn't typically how we think about the data when we analyze fMRI data. fMRI is typically thought of as **time-series** data. We can think of each voxel (x,y,z coordinate) as having a time-series of length T. The length T represents the number of volumes/timepoints in the data. Let's pick an example voxel and examine its time-series using <code>func_mni_img.slicer</code>:

~~~
#Pick one voxel at coordinate (60,45,88)
single_vox = func_mni_img.slicer[59:60,45:46,30:31,:].get_data()
single_vox.shape
~~~
{: .language-python}

~~~
(1, 1, 1, 152)
~~~
{: .output}

As you can see we have 1 element in (x,y,z) dimension representing a single voxel. In addition, we have 152 elements in the fourth dimension. In totality, this means we have a single voxel with 152 timepoints. Dealing with 4 dimensional arrays are difficult to work with - since we have a single element across the first 3 dimensions we can squish this down to a 1 dimensional array with 152 time-points. We no longer need the first 3 spatial dimensions since we're only looking at one voxel and don't need (x,y,z) anymore:

~~~
single_vox = single_vox.flatten()
single_vox.shape
~~~
{: .language-python}

~~~
(152,)
~~~
{: .output}

Now we have a single 1-D array with 152 elements. This 1D array represents the single voxel we pulled out earlier and its 152 timepoints. Now we can visualize the signal coming from this signal voxel using a time-series plot!

First let's import the standard python plotting library <code>matplotlib</code>:

~~~
import matplotlib.pyplot as plt
~~~
{: .language-python}

Let's now plot this:

~~~
# Make an array counting from 0 --> 152, this will be our x-axis
x_axis = np.arange(0, single_vox.shape[0])

# Plot our x and y data, the 'k' just specifies the line color to be black
plt.plot( x_axis, single_vox, 'k')

# Label our axes
plt.xlabel('Timepoint')
plt.ylabel('Signal Value')
~~~
{: .language-python}

![Example fMRI Timeseries](../fig/timeseries.png){:class="img-responsive"}

As you can see from the image above, fMRI data really is just a signal per voxel over time!

## Resampling
Recall from our introductory exploration of neuroimaging data:

- T1 images are typically composed of voxels that are 1x1x1 in dimension
- Functional images are typically composed of voxels that are 4x4x4 in dimension

If we'd like to overlay our functional on top of our T1 (for visualization purposes, or analyses), then we need to match the size of the voxels! 

Think of this like trying to overlay a 10x10 JPEG and a 20x20 JPEG on top of each other. To get perfect overlay we need to resize (or more accurately *resample*) our JPEGs to match!

>Resampling is a method of interpolating in between data-points. When we stretch an image we need to figure out what goes in the spaces that are created via stretching - resampling does just that. In fact, resizing any type of image is actually just resampling to new dimensions.
{: .callout}

Let's resampling some MRI data using nilearn:

~~~
#Files we'll be using (Notice that we're using _space-MNI..._ which means they are normalized brains)
T1_mni = T1w_files[1].path
T1_mni_img = nimg.load_img(T1_mni)
~~~
{: .language-python}

Let's take a quick look at the sizes of both our functional and structural files:

~~~
print(T1_mni_img.shape)
print(func_mni_img.shape)
~~~
{: .language-python}

~~~
(193, 229, 193)
(60, 86, 65, 152)
~~~
{: .output}

Taking a look at the spatial dimensions (first three dimensions), we can see that the number of voxels in the T1 image does not match that of the fMRI image. This is because the fMRI data (which has less voxels) is a *lower resolution image*. We either need to *upsample* our fMRI image to match that of the T1 image, or we need to *downsample* our T1 image to match that of the fMRI image. Typically, since the fMRI data is the one we'd like to ultimately use for analysis, we would leave it alone and downsample our T1 image. The reason being is that *resampling* requires interpolating values which may contaminate our data with artifacts. We don't mind having artifacts in our T1 data (for visualization purposes) since the fMRI data is the one actually being analyzed.

Resampling in nilearn is as easy as telling it which image you want to sample and what the target image is.
Structure of function:

nimg.resample_to_img(source_img,target_img,interpolation) 
- source_img = the image you want to sample
- target_img = the image you wish to *resample to* 
- interpolation = the method of interpolation

> A note on **interpolation**
> nilearn supports 3 types of interpolation, the one you'll use depends on the type of data you're resampling!
> 1. **continuous** - Interpolate but maintain some edge features.  Ideal for structural images where edges are well-defined. Uses $3^\text{rd}$-order spline interpolation.
> 2. **linear (default)** - Interpolate uses a combination of neighbouring voxels - will blur. Uses trilinear interpolation.
> 3. **nearest** - matches value of closest voxel (majority vote from neighbours). This is ideal for masks which are binary since it will preserve the 0's and 1's and will not produce in-between values (ex: 0.342). Also ideal for numeric labels where values are 0,1,2,3... (parcellations). Uses nearest-neighbours interpolation with majority vote.
{: .callout}

~~~
#Try playing around with methods of interpolation
#options: 'linear','continuous','nearest'
resamp_t1 = nimg.resample_to_img(source_img=T1_mni_img,target_img=func_mni_img,interpolation='continuous')
print(resamp_t1.shape)
print(func_mni_img.shape)
nplot.plot_anat(resamp_t1)
~~~
{: .language-python}

![Downsampled T1](../fig/downsample_t1.png){:class="img-responsive"}

Now that we've explored the idea of resampling let's do a cumulative exercise bringing together ideas from resampling and basic image operations.

> ## Exercise
> 
> Using **Native** T1 and **T1w** resting state functional do the following:
> 1. Resample the native T1 image to resting state size
> 2. Replace the brain in the T1 image with the first frame of the resting state brain
> 
> ### Files we'll need
> 
> 
> #### Structural Files
> 
> ~~~
> #T1 image
> ex_t1 = nimg.load_img(T1w_files[0].path)
> 
> #mask file
> ex_t1_bm = nimg.load_img(brainmask_files[0].path)
> ~~~
> {: .language-python}
> 
> #### Functional Files
> 
> ~~~
> #This is the pre-processed resting state data that hasn't been standardized
> ex_func = nimg.load_img(func_files[1].path)
> 
> #This is the associated mask for the resting state image.
> ex_func_bm = nimg.load_img(func_mask_files[1].path)
> ~~~
> {: .language-python}
> 
> The first step we need to do is to make sure the dimensions for our T1 image and resting state image match each other:
> 
> ~~~
> #Resample the T1 to the size of the functional image!
> resamp_t1 = nimg.resample_to_img(source_img=??, target_img=??, interpolation='continuous')
> nplot.plot_anat(??)
> print(resamp_t1.shape)
> ~~~
> {: .language-python}
> 
> ![Episode 04 Exercise Downsampled Image](../fig/exercise_t1.png){:class="img-responsive"}
> 
> Next we want to make sure that the brain mask for the T1 is also the same dimensions as the functional image. This is exactly the same as above, except we use the brain mask as the source.
> 
> What kind of interpolation should we use for masks?
> 
> ~~~
> resamp_bm = nimg.??(??)
> 
> #Plot the image
> ??
> 
> print(resamp_bm.shape)
> ~~~
> {: .language-python}
> 
> Once we've resampled both our T1 and our brain mask. We now want to remove the brain from the T1 image so that we can replace it with the funtional image instead. Remember to do this we need to:
> 
> 1. Invert the T1 mask
> 2. Apply the inverted mask to the brain
> 
> ~~~
> inverted_bm_t1 = nimg.math_img(??,a=resamp_bm)
> nplot.plot_anat(inverted_bm_t1)
> ~~~
> {: .language-python}
> 
> Now apply the mask using basic image arithmetic:
> 
> ~~~
> resamp_t1_nobrain = nimg.??(??)
> nplot.plot_anat(resamp_t1_nobrain)
> ~~~
> {: .language-python}
> 
> We now have a skull missing the structural T1 brain. The final steps is to stick in the brain from the functional image into the now brainless head. First we need to remove the surrounding signal from the functional image.
> 
> Since a functional image is 4-Dimensional, we'll need to pull the first volume to work with. This is because the structural image is 3-dimensional and operations will fail if we try to mix 3D and 4D data.
> 
> ~~~
> #Let's visualize the first volume of the functional image:
> first_vol = ex_func.slicer[??,??,??,??]
> nplot.plot_epi(first_vol)
> ~~~
> {: .language-python}
> 
> As shown in the figure above, the image has some "signal" outside of the brain. In order to place this within the now brainless head we made earlier, we need to mask out the functional MR data as well!
> 
> ~~~
> #Mask first_vol using ex_func_bm
> masked_func = nimg.math_img('??', a=??, b=??)
> nplot.plot_epi(masked_func)
> ~~~
> {: .language-python}
> 
> The final step is to stick this data into the head of the T1 data. Since the hole in the T1 data is represented as $0$'s. We can add the two images together to place the functional data into the void:
> 
> ~~~
> #Now overlay the functional image on top of the anatomical
> combined_img = nimg.math_img(??)
> nplot.plot_anat(combined_img)
> ~~~
> {: .language-python}
> 
> > ## Solution
> > 
> > ~~~
> > #Resample the T1 to the size of the functional image!
> > resamp_t1 = nimg.resample_to_img(source_img=ex_t1, target_img=ex_func, interpolation='continuous')
> > nplot.plot_anat(resamp_t1)
> > print(resamp_t1.shape)
> > 
> > resamp_bm = nimg.resample_to_img(source_img=ex_t1_bm, target_img=ex_func,interpolation='nearest')
> > nplot.plot_anat(resamp_bm)
> > print(resamp_bm.shape)
> > 
> > inverted_bm_t1 = nimg.math_img('1-a',a=resamp_bm)
> > nplot.plot_anat(inverted_bm_t1)
> > 
> > resamp_t1_nobrain = nimg.math_img('a*b',a=resamp_t1,b=inverted_bm_t1)
> > nplot.plot_anat(resamp_t1_nobrain)
> > 
> > #Let's visualize the first volume of the functional image:
> > first_vol = ex_func.slicer[:,:,:,0]
> > nplot.plot_epi(first_vol)
> > 
> > masked_func = nimg.math_img('a*b', a=first_vol, b=ex_func_bm)
> > nplot.plot_epi(masked_func)
> > 
> > #Now overlay the functional image on top of the anatomical
> > combined_img = nimg.math_img('a+b',a=resamp_t1_nobrain,b=masked_func)
> > nplot.plot_anat(combined_img)
> > 
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

{% include links.md %}
