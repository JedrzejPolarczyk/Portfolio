Projekt analizuje wpływ regularyzacji L1 (Lasso), L2 (Ridge) oraz Elastic Net na jakość modeli regresji predykcyjnej. Celem jest porównanie wpływu parametrów regularyzacji oraz wybranie najlepszego modelu.

Dane

Pliki Zmienne.txt, dataset.train.txt, dataset.test.txt.
Zawierają dane numeryczne i kategoryczne.

Technologie

Python
Pandas
NumPy
Scikit-learn
Statsmodels
Matplotlib

Zakres prac

Wczytanie danych i analiza braków.
Normalizacja zmiennych i czyszczenie danych.
Model bazowy OLS.
Ridge Regression – tuning alpha.
Lasso Regression – tuning alpha.
Elastic Net – tuning alpha i l1_ratio.
Porównanie R² i współczynników.
Interpretacja istotności cech.

Wyniki

Ridge miał najlepszą stabilność współczynników.
Lasso wyzerowało najmniej istotne cechy (feature selection).
Elastic Net osiągnął najlepsze R² na zbiorze testowym.

Wnioski

Regularyzacja znacząco zwiększa stabilność modelu.
Lasso jest idealne do redukcji liczby cech.
Elastic Net równoważy dokładność i interpretowalność.