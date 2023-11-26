import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

covariance_manual = np.mean((zp - np.mean(zp)) * (ks - np.mean(ks)))  # Ручной подсчет
covariance_numpy = np.cov(zp, ks, ddof=1)[0, 1]  # Использование функции cov из NumPy

print("Covariance (manual):", covariance_manual)
print("Covariance (NumPy):", covariance_numpy)



import numpy as np
import pandas as pd

correlation_manual = covariance_manual / (np.std(zp, ddof=1) * np.std(ks, ddof=1))  # Ручной подсчет
correlation_numpy = np.corrcoef(zp, ks)[0, 1]  # Использование функции corrcoef из NumPy
correlation_pandas = pd.Series(zp).corr(pd.Series(ks))  # Использование функции corr из Pandas

print("Correlation (manual):", correlation_manual)
print("Correlation (NumPy):", correlation_numpy)
print("Correlation (Pandas):", correlation_pandas)
