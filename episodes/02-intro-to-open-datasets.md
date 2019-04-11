---
title: "Exploration of Open Neuroimaging Datasets in BIDS format" 
teaching: 30
exercises: 15
questions:
- "How does standardization of neuroimaging data ease the data exploration process"
objectives:
- "Gain a grasp of the BIDS format"
- "Use PyBIDS in to easily explore a BIDS dataset"
keypoints:
- "BIDS is an organizational principle for neuroimaging data for transparent data sharing"
- "PyBIDS is a python based tool that allows for easy exploration of BIDS-formatted neuroimaging data"
---


## Tutorial Dataset
For this tutorial, we will be using a subset of a pubicly available dataset, ds000030, from openneuro.org. The dataset is structured according to the Brain Imaging Data Structure (BIDS). BIDS is a simple and intuitive way to organize and describe your neuroimaging and behavioural data. Neuroimaging experiments result in complicated data that can be arranged in several different ways. BIDS tackles this problem by suggesting a new standard (based on consensus from multiple researchers across the world) for the arrangement of neuroimaging datasets.

Using the same structure for all of your studies will allow you to easily reuse all of your scripts between studies. Additionally, sharing code with other researchers will be much easier.

Let's take a look at the participants.tsv file to see what the demographics for this dataset look like.

~~~
import pandas as pd

participant_metadata = pd.read_csv('../data/ds000030/participants.tsv', sep='\t')
participant_metadata
~~~
{: .language-python}

**OUTPUT:**
<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>participant_id</th>      <th>diagnosis</th>      <th>age</th>      <th>gender</th>      <th>bart</th>      <th>bht</th>     <th>dwi</th>      <th>pamenc</th>      <th>pamret</th>      <th>rest</th>      <th>scap</th>      <th>stopsignal</th>      <th>T1w</th>      <th>taskswitch</th>      <th>ScannerSerialNumber</th>      <th>ghost_NoGhost</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>sub-10159</td>     <td>CONTROL</td>      <td>30</td>      <td>F</td>      <td>1.0</td>      <td>NaN</td>      <td>1.0</td>      <td>NaN</td>      <td>NaN</td>      <td>1.0</td>      <td>1.0</td>      <td>1.0</td>      <td>1.0</td>      <td>1.0</td>      <td>35343.0</td>      <td>No_ghost</td>    </tr>    <tr>      <th>1</th>      <td>sub-10171</td>      <td>CONTROL</td>      <td>24</td>      <td>M</td>      <td>1.0</td>      <td>1.0</td>      <td>1.0</td>      <td>NaN</td>      <td>NaN</td>      <td>1.0</td>      <td>1.0</td>      <td>1.0</td>      <td>1.0</td>      <td>1.0</td>      <td>35343.0</td>      <td>No_ghost</td>    </tr>    <tr>      <th>2</th>      <td>sub-10189</td>      <td>CONTROL</td>      <td>49</td>      <td>M</td>      <td>1.0</td>      <td>NaN</td>      <td>1.0</td>      <td>NaN</td>      <td>NaN</td>      <td>1.0</td>      <td>1.0</td>      <td>1.0</td>      <td>1.0</td>      <td>1.0</td>      <td>35343.0</td>      <td>No_ghost</td>    </tr>    <tr>      <th>3</th>      <td>sub-10193</td>      <td>CONTROL</td>      <td>40</td>      <td>M</td>      <td>1.0</td>      <td>NaN</td>      <td>1.0</td>      <td>NaN</td>      <td>NaN</td>      <td>NaN</td>      <td>NaN</td>      <td>NaN</td>      <td>1.0</td>      <td>NaN</td>      <td>35343.0</td>      <td>No_ghost</td>    </tr>    <tr>      <th>4</th>      <td>sub-10206</td>      <td>CONTROL</td>      <td>21</td>      <td>M</td>      <td>1.0</td>      <td>NaN</td>      <td>1.0</td>      <td>NaN</td>      <td>NaN</td>      <td>1.0</td>      <td>1.0</td>      <td>1.0</td>      <td>1.0</td>      <td>1.0</td>      <td>35343.0</td>      <td>No_ghost</td>    </tr>  </tbody></table>

From this table we can easily view unique diagnostic groups:

~~~
participant_metadata['diagnosis'].unique()
~~~
{: .language-python}

~~~
array(['CONTROL', 'SCHZ', 'BIPOLAR', 'ADHD'], dtype=object)
~~~
{: .output}

For this tutorial, we're just going to work with participants that are either CONTROL or SCHZ (`diagnosis`) and have both a T1w (`T1w == 1`) and rest (`rest == 1`) scan. Also, you'll notice some of the T1w scans included in this dataset have a ghosting artifact. We'll need to filter these out as well (`ghost_NoGhost == 'No_ghost'`).

We'll filter this data out like so:
~~~
participant_metadata = participant_metadata[(participant_metadata.diagnosis.isin(['CONTROL', 'SCHZ'])) & 
                                            (participant_metadata.T1w == 1) & 
                                            (participant_metadata.rest == 1) & 
                                            (participant_metadata.ghost_NoGhost == 'No_ghost')]
participant_metadata['diagnosis'].unique()
~~~

~~~
array(['CONTROL', 'SCHZ'], dtype=object)
~~~
{: .output}

From this we have a list of participants corresponding to a list of participants who are of interest in our analysis. We can then use this list in order to download participant from software such as `aws` or `datalad`. In fact, this is exactly how we set up a list of participants to download for this workshop! Since we've already downloaded the dataset, we can now explore the structure using PyBIDS:

~~~
import bids.layout
layout = bids.layout.BIDSLayout('../data/ds000030')
~~~
{: .language-python}

The pybids layout object lets you query your BIDS dataset according to a number of parameters by using a get_*() method.
We can get a list of the subjects we've downloaded from the dataset.

~~~
layout.get_subjects()
~~~
{: .language-python}

~~~
['10171',
 '10292',
 '10365',
 '10438',
 '10565',
 '10788',
 '11106',
 '11108',
 '11122',
   ...
 '50083']
~~~
{: .output}

We can also pull a list of imaging modalities in the dataset:

~~~
layout.get_modalities()
~~~
{: .language-python}

~~~
['anat', 'func']
~~~
{: .output}

As well as tasks and more!:

~~~
#Task fMRI
print(layout.get_tasks())

#Data types (bold, brainmask, confounds, smoothwm, probtissue, warp...)
print(layout.get_types())
~~~
{: .language-python}

~~~
['rest']

['bold',
 'brainmask',
 'confounds',
 'description',
 'dtissue',
 'fsaverage5',
 'inflated',
 'midthickness',
 'participants',
 'pial',
 'preproc',
 'probtissue',
 'smoothwm',
 'warp']
~~~
{: .output}


In addition we can specify sub-types of each BIDS category:

~~~
layout.get_types(modality='func')
~~~
{: .language-python}

~~~
['brainmask', 'confounds', 'fsaverage5', 'preproc']
~~~
{: .output}
We can use this functionality to pull all our fMRI NIFTI files:

~~~
layout.get(task='rest', type='bold', extensions='nii.gz', return_type='file')
~~~
{: .language-python}
~~~
TO FILL
~~~
{: .output}

Finally, we can convert the data stored in `bids.layout` into a `pandas.DataFrame` :

~~~
df = layout.as_data_frame()
df.head()
{: .language-python}

**OUTPUT:**
<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>path</th>      <th>modality</th>      <th>subject</th>      <th>task</th>      <th>type</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>/home/jerry/projects/scwg2018_python_neuroimag...</td>      <td>NaN</td>      <td>NaN</td>      <td>rest</td>      <td>bold</td>    </tr>    <tr>      <th>1</th>      <td>/home/jerry/projects/scwg2018_python_neuroimag...</td>      <td>NaN</td>      <td>NaN</td>      <td>NaN</td>      <td>participants</td>    </tr>    <tr>      <th>2</th>      <td>/home/jerry/projects/scwg2018_python_neuroimag...</td>      <td>NaN</td>      <td>NaN</td>      <td>NaN</td>      <td>NaN</td>    </tr>    <tr>      <th>3</th>      <td>/home/jerry/projects/scwg2018_python_neuroimag...</td>      <td>anat</td>      <td>10565</td>      <td>NaN</td>      <td>brainmask</td>    </tr>    <tr>      <th>4</th>      <td>/home/jerry/projects/scwg2018_python_neuroimag...</td>      <td>anat</td>      <td>10565</td>      <td>NaN</td>      <td>probtissue</td>    </tr>  </tbody></table>
