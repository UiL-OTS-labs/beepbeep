# Beep helpers

A script to generate a lot of short wav files with beeps according to some 
naming convention, so one can easily create a 'dummy experiment' for testing/
debugging.

## Background and rationale

Consider the case of Wil de Bras (fake person). Wil is a linguistics master 
student, who wants to run an experiment in which EEG/ERP signals may or may not
be found to be different based upon some deep language logic. Let's say
sense making language vs non sense making context sentences.

In order to create context, some rather long wav files have been prepared, and
all kinds of conditions have been matched. A trial consists of some 
concatenation of different wav files. One trial can easily take 30 
seconds to play, and in order to have enough power, a total of 504 different, 
wav files have to be in the experiment, all nicely counterbalanced, 
block designed, matched and pseudorandomised, the whole enchilada. 

The exeriment runs in, say, neurobs Presentation.

Let's say we've come up with an experiment with the following type of 
file names:

- 60 wavs of type a
- 60 wavs of type b
- 60 wavs of type c
- 60 wavs of type d

- 66 wavs of type fa
- 66 wavs of type fb
- 66 wavs of type fc
- 66 wavs of type fd

- 2 wavs of type pa
- 2 wavs of type pb
- 2 wavs of type pc
- 2 wavs of type pd

All have nicely been recorded and by hand named to be used programatically in 
Presentation, so all types are in the wav filename, e.g.

Type A yields:

	a01.wav
	a02.wav
	a03.wav
	...
	a58.wav
	a59.wav
	a60.wav

Type B yields:

	a01.wav
	a02.wav
	a03.wav
	...
	a58.wav
	a59.wav
	a60.wav

And so on...

### Questions

- How long would it take to (tech) pilot the entire experiment and check if all
  items are randomised correctly?
- How long would it take to find a bug in the code that only happens every now 
  and then, due to some specifics in randomisation? 
- What if you just want to check if the different wav *types* are nicely 
  generated to form trials, instead of having to judge this by linguistic 
  content?

The anwser is, you (and your technician) have arrived in ~~hell~~. You have to 
run the entire experiment of more than one hour at least 10 times to test under 
what condition some bug might appear and spend an entire day listening to your
lengthy sentences.

## Solution: beeps
   
For this reason, beep.py has been created. If you know how to make a custom 
dictionary, you can easily adapt this to your type/token condition needs and
build you own dummy version of the experiment with simple, short beeps instead 
of long, complex sentences with one command in a python shell.

# How to use

This is not aimed at single purpose production use, you will have to create your
own dictionary. Or you techie might be able to help you out.

If you would like the amount of files and types exactly like Wil de Bras, you
can clone or download this repository, make sure you have the right permission,
fire up Konsole, Terminal, or windows python and for instance, type:

ipython3
Python 3.7.2 (default, Jan 13 2019, 12:50:15)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import beep as b
In [2]: b.make_all_beeps()

(TODO for specific UiL OTS labs situation)




