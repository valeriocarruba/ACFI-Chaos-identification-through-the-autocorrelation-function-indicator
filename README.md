# ACFI-Chaos-identification-through-the-autocorrelation-function-indicator
Python codes to compute the ACFI chaos indicator, for small bodies in the Solar System. The ACFI chaos indicator is an approach based on the autocorrelation function of time series, the ACF index (ACFI). Autocorrelation coefficients measure the correlation of a time-series with a lagged copy of itself. By measuring the fraction of autocorrelation coefficients obtained after a given time-lag that are higher than the 5% null hypothesis threshold, we can determine how the time-series auto-correlates with itself. This allows identifying unpredictable time-series, characterized by low values of ACFI. ACFI is not affected by stochastic events, like close encounters with massive bodies, and this makes it an useful tool for studying chaos in orbital regions affected by chaos caused by resonance overlapping and close encounters, like like the 3:1 mean-motion resonance with Jupiter in the asteroid main belt, or the mean-motion resonances with Neptune in the TNOs orbital  region.
Here we provide an example of an integration of 20 test particles, integrated over 20 Myr over the gravitational influence of all planets, with a Burlisch-Stoer integrator, and a python code to automatically compute values of ACFI.  The code runs on a Linux Ubuntu machine, with a Python3.8.3 version. There might be portability issues on other operating systems.  To run the code, simply type:

```
python3 compute_acfi.py
```

This command will output the particle number, the number of autocorrelation coefficients with amplitudes larger than +/-0.05, the lenght of lags intervals used to compute ACFI, and ACFI itself.  
