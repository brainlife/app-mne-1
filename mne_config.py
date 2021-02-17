"""
Auditory MEG
"""

study_name = 'ds000246'
bids_root = '/Users/guiomar/Projects/ds000246'
deriv_root = '/out_dir'
runs = ['01']
l_freq = .3
h_freq = 100.
decim = 10 #4
subjects = ['0001']
ch_types = ['meg']
reject = dict(mag=4e-12, eog=250e-6)
conditions = ['standard', 'deviant', 'button']
contrasts = [('deviant', 'standard')]
decode = True
#daysback = -365 * 110
on_error = 'debug'