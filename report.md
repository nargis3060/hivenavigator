# HiveNavigator — Acoustic & Sensor Analysis Report
**Candidate:** Nargisa  
**Programme:** DigiLink 26/27  
**Submission Date:** 24 March 2026  

---

## 1. Which features best separate queenless from queenright?

The two strongest features are:
- **RMS Energy**: Queenless hives show 46.7% lower energy than queenright hives
  (Queenless: 0.000267 ± 0.000171 vs Queenright: 0.000500 ± 0.000274)
- **Spectral Flatness**: Queenless hives show 55% higher flatness
  (Queenless: 0.005347 vs Queenright: 0.003450)
  This means queenless hives produce more noise-like, less structured sound.

Spectral centroid and ZCR showed minimal difference (<1%).

---

## 2. Do the two queenless hives show consistent signatures?

Hive 03 and Hive 04 showed different patterns:
- Hive 04 showed much stronger signals: RMS dropped 65.6% and flatness 
  dropped 86.1% after queen introduction on 12 March
- Hive 03 showed weaker changes: RMS only changed +6.1% after queen removal

This divergence may be explained by:
- Different queen removal timing (Hive 04 was queenless for 3 days before 12 Mar)
- Individual colony differences in bee population size
- Different adaptation rates to queen loss

---

## 3. How quickly does the queenless signature appear?

Based on Hive 04 analysis, the acoustic signature changes are visible 
within the first recording after the queen status change. The flatness 
and RMS energy show immediate shifts, suggesting bees respond acoustically 
within hours of queen removal or introduction.

---

## 4. Does the modulation spectrogram reveal additional patterns?

Yes — the modulation spectrogram revealed differences in the low frequency 
range (0-1000 Hz) that are not visible in plain MFCCs. The before-removal 
spectrogram shows stronger energy concentration in the lowest frequency bins,
while the after-removal spectrogram shows a more distributed pattern with 
a distinct shift around modulation index 16-17. This suggests changes in 
the temporal modulation of bee activity.

---

## 5. Correlating signals in accelerometer/sensor data?

The temperature data from Hive 03 shows a gradual increase during the 
recording period (March 7-22), consistent with seasonal warming. No strong 
correlation was found between temperature spikes and the acoustic changes,
suggesting the acoustic differences are driven by colony behaviour rather 
than environmental factors.
