# -*- coding: utf-8 -*-
"""
# ===========================================================================
# ===========================================================================
# !==   Valerio Carruba                                                    ==
# !==   Safwan Aljbaae                                                     ==
# !==   Rita de Cássia Domingos                                            ==
# !==   February 2021                                                      ==
# ===========================================================================
"""
import numpy as np
import pandas as pd

for j in range(1,21):
    particle = j
    srt_particle = str(particle).zfill(2)

    filename = 'el_osc_' + srt_particle
    df = pd.read_csv(str(filename),
                     skiprows=0,
                     header=None,
                     delim_whitespace=True,
                     index_col=None,
                     names=['Time', 'a', 'e', 'i', 'Comega', 'omega', 'M'],
                     low_memory=False,
                     dtype={'Time': np.float64,
                            'a': np.float64,
                            'e': np.float64,
                            'i': np.float64,
                            'Comega': np.float64,
                            'omega': np.float64,
                            'M': np.float64}
    )
    aa=pd.Series(df.a)
    nind=0
    nmin=200
    nmax=500
    for i in range(nmax):
        ind=aa.autocorr(lag=i)
        if i > nmin:
            if abs(ind) > 0.05:
                nind=nind+1
    freq=nind/(nmax-nmin)
    print("%2d" % j, "%3d" % nind, "%3d" % (nmax-nmin), "%6.3f" % freq)
            
