Projekt przedstawia proces grupowania danych (clustering) z wykorzystaniem metod nienadzorowanego uczenia maszynowego. Analiza wykonywana jest na zbiorze danych o daniach rybnych i obejmuje zarówno grupowanie hierarchiczne, jak i K-Means, a także ocenę jakości klastrów.

Dane

dania.rybne.csv



Technologie Python

Pandas
NumPy
Matplotlib / Seaborn
Scikit-learn
SciPy (hierarchical clustering)

Zakres analizy

Wczytanie i eksploracja danych.
Czyszczenie i przygotowanie zbioru.
Grupowanie hierarchiczne:
macierz połączeń, dendrogram, wybór liczby klastrów.
Klasteryzacja K-Means:
testowanie różnych K, ocena inertia.

Ocena jakości:
silhouette score.
Wizualizacja klastrów i interpretacja wyników.

Wyniki

Wyznaczono optymalną liczbę klastrów.
Porównano klasteryzację hierarchiczną i K-Means.
Zidentyfikowano cechy najlepiej różnicujące grupy.

Wnioski

Część potraw tworzy naturalne, gęste skupiska.
Metody hierarchiczne dały bardziej interpretowalne wyniki.
Klasteryzacja wykryła struktury niewidoczne w zwykłej analizie.