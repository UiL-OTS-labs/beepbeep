#!/usr/bin/python3

# Code-wise, this way of working with lists instead of (numpy) arrays is not 
# very wise, or efficient. The same holds for the non-buffered `save_wav()`
# -routine. But if you keep the durations rather low, say below 10 seconds per
# beep, this should not give rise to (m)any problems. 

# Sound stuff based on : www.daniweb.com/code/snippet263775.html

import os 
import math
import wave
import struct

def generate_beep_wavs(dirname='output', 
                        pre='a',
                        somany=9,
                        padspec='{0:02d}',
                        dur_ms=300,
                        sample_rate=44100.0,
                        freq=440,
                        volume=1):
    """
    Generate N instances of a simple sine wave beep.
    
    Parameters
    ----------
    dirname : str
        Output files will be created in `dirname`, if given.
    pre : str
        Some common prefix for all files, like "Experiment_42_".
    somany : int
        This many files will be created (all with the same beep specs!).
    padspec : str
        Padding specification string, default zero-pads 01-99, the spec 
        '{0:03d}' would pad 1-999 as 001, 002 ... 099, 100 ... 999.
    dur_ms : int 
        Duration of the beep, in milliseconds.
    sample_rate : int
        Sane values would be 48000 or 44100 for uncompressed 16 bit wav.
    freq : int
        Freqency of the sine wave ('A'=440 cycles/second)
    volume : float (0-1)
        Full loudness (amplitude) is '1.0'.
    """ 
    cwd = os.getcwd()
    fulldir = cwd + os.path.sep + dirname
    print (fulldir)
    if not os.path.exists(fulldir):
        os.mkdir(cwd + os.path.sep + dirname)
        print ("creating", cwd + os.path.sep + dirname)
    #only the first time, audio has to actually be created
    sound = make_new_sine_wav(fname=None, 
                            sample_rate=sample_rate,
                            dur_ms=dur_ms,
                            freq=freq,
                            volume=volume)
    # now we create file names (just call the first one 01, not 00)
    for i in range(somany):
        fname = fulldir + os.path.sep + pre + padspec.format(i + 1) + ".wav"
        print ("Creating: ", fname)
        save_wav(fname, sound, sample_rate) 
    return 
    
def make_new_sine_wav(fname=None, 
                    sample_rate=44100.0, 
                    dur_ms=300, 
                    freq=440,
                    volume=1.0):
    """
    Create a file with a sine wave of some frequency and some duration. 
    
    If fname is None, it will not save to file, but only return the audio list.
    
    Parameters
    ----------
    fname : None or str
        If None, the file will not be saved as wav.
    sample_rate : int
        Sane values would be 48000 or 44100 for uncompressed 16 bit wav
    dur_ms : int 
        Duration of the beep, in milliseconds.
    freq : int
        Freqency of the sine wave ('A'=440 cycles/second)
    volume : float (0-1)
        Full loudness (amplitude) is '1.0'.
    """ 
    audio = []
    num_sound_samples = dur_ms * (sample_rate / 1000.0)
    
    for x in range(int(num_sound_samples)):
        audio.append(volume * 
                    math.sin(2 * math.pi * freq * ( x / sample_rate )))
    # save it to disk for a single file? It has to have a name then...
    if fname:
        save_wav(fname, audio)
    return audio


def save_wav(fname, audio, sample_rate):
    """
    Save audio (list) to disk as a wav file.
    
    Parameters
    ----------
    fname : str
        A file name.
    audio : list
        A list with audio samples.
    sample_rate : int 
        Sample rate. 44100 or 48000, for instance
    """
    wav_file = wave.open(fname,"w")
    # wav params
    nchannels = 1
    sampwidth = 2
    nframes = len(audio)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, 
                        comptype, compname))
    # (32767 ---> 16 bit largest number)
    for sample in audio:
        wav_file.writeframes(struct.pack('h', int( sample * 32767.0 )))
    wav_file.close()
    return

# This is a dict with Rachida's naming/amount specs. 
# I chose some values for tones. It results in a nice kind of scale ;-) 

big = dict({'a':  {'pre':'a', 'dur':250, 'tone':222, 'amount':60},
			'b':  {'pre':'b', 'dur':250, 'tone':333, 'amount':60},
			'c':  {'pre':'c', 'dur':250, 'tone':444, 'amount':60},
			'd':  {'pre':'d', 'dur':250, 'tone':555, 'amount':60},
			'fa': {'pre':'fa','dur':250, 'tone':666, 'amount':66},
			'fb': {'pre':'fb','dur':250, 'tone':777, 'amount':66},
			'fc': {'pre':'fc','dur':250, 'tone':888, 'amount':66},
			'fd': {'pre':'fd','dur':250, 'tone':999, 'amount':66},
			'pa': {'pre':'pa', 'dur':500, 'tone':222, 'amount':2},
			'pb': {'pre':'pb', 'dur':500, 'tone':333, 'amount':2},
			'pc': {'pre':'pc', 'dur':500, 'tone':444, 'amount':2},
			'pd': {'pre':'pa', 'dur':500, 'tone':555, 'amount':2}
			})

# single version test-dict

# big = dict({'a':  {'pre':'a', 'dur':250, 'tone':222, 'amount':1},
# 			'b':  {'pre':'b', 'dur':250, 'tone':333, 'amount':1},
# 			'c':  {'pre':'c', 'dur':250, 'tone':444, 'amount':1},
# 			'd':  {'pre':'d', 'dur':250, 'tone':555, 'amount':1},
# 			'fa': {'pre':'fa','dur':250, 'tone':666, 'amount':1},
# 			'fb': {'pre':'fb','dur':250, 'tone':777, 'amount':1},
# 			'fc': {'pre':'fc','dur':250, 'tone':888, 'amount':1},
# 			'fd': {'pre':'fd','dur':250, 'tone':999, 'amount':1},
# 			'pa': {'pre':'pa', 'dur':500, 'tone':222, 'amount':1},
# 			'pb': {'pre':'pb', 'dur':500, 'tone':333, 'amount':1},
# 			'pc': {'pre':'pc', 'dur':500, 'tone':444, 'amount':1},
# 			'pd': {'pre':'pa', 'dur':500, 'tone':222, 'amount':1}
# 			})


# print (big.items())
# print (big.keys())

# function to create all stuff at once (custom part defined on 
# dictionary structure)

def make_all_beeps(d=big):
	"""
	Based upon the dictionary 'big', build some beeps.
	"""
	for k, v in d.items():
		generate_beep_wavs(dirname='output', 
							pre=v['pre'],
                        	somany=v['amount'],
                        	padspec='{0:02d}',
                        	dur_ms=v['dur'],
                        	sample_rate=44100.0,
                        	freq=v['tone'],
                        	volume = 1)
 
    
    
	














