# Importowanie niezbędnych bibliotek
import numpy as np  # Biblioteka NumPy do obliczeń numerycznych
import pandas as pd  # Biblioteka Pandas do manipulacji i analizy danych
import matplotlib.pyplot as plt  # Biblioteka Matplotlib do tworzenia wykresów
import seaborn as sns  # Biblioteka Seaborn do tworzenia bardziej zaawansowanych wykresów

# Wczytanie danych treningowych
train_data = pd.read_csv('train.csv')  # Wczytanie danych z pliku CSV

# Wyświetlenie pierwszych 5 wierszy danych
train_data.head(5)

# Wyświetlenie podstawowych statystyk danych
train_data.describe()

# Utworzenie mapy cieplnej korelacji między cechami
sns.heatmap(train_data.corr(), cmap="YlGnBu")  # Użycie Seaborn do stworzenia mapy cieplnej
plt.show()  # Wyświetlenie wykresu

# Wyświetlenie danych treningowych
train_data

# Importowanie narzędzi do podziału danych
from sklearn.model_selection import StratifiedShuffleSplit

# Utworzenie podziału danych na zestawy treningowe i testowe
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2)  # Ustawienie parametrów podziału
# Podział danych z uwzględnieniem równomiernego rozłożenia klas
for train_indices, test_indices in split.split(train_data, train_data[["Survived", "Pclass", "Sex"]]):
  strat_train_set = train_data.loc[train_indices]  # Zestaw treningowy
  strat_test_set = train_data.loc[test_indices]  # Zestaw testowy

# Tworzenie histogramów dla zestawów treningowych i testowych
plt.subplot(1,2,1)  # Ustawienie pierwszego panelu
strat_train_set['Survived'].hist()  # Histogram przeżywalności dla zestawu treningowego
strat_train_set['Pclass'].hist()  # Histogram klasy pasażerskiej dla zestawu treningowego

plt.subplot(1,2,2)  # Ustawienie drugiego panelu
strat_test_set['Survived'].hist()  # Histogram przeżywalności dla zestawu testowego
strat_test_set['Pclass'].hist()  # Histogram klasy pasażerskiej dla zestawu testowego

plt.show()  # Wyświetlenie histogramów

# Wyświetlenie informacji o zestawie treningowym
strat_train_set.info()

# Importowanie narzędzi do przetwarzania danych
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer

# Definicja klasy do imputacji wieku
class AgeImputer(BaseEstimator, TransformerMixin):
  def fit(self, X, y=None):
    return self

  def transform(self, X):
    imputer = SimpleImputer(strategy="mean")  # Użycie imputacji średnią
    X[['Age']] = imputer.fit_transform(X[['Age']])  # Imputacja wieku
    return X

# Definicja klasy do kodowania cech
from sklearn.preprocessing import OneHotEncoder
class FeatureEncoder(BaseEstimator, TransformerMixin):
  def fit(self, X, y=None):
    return self

  def transform(self, X):
    encoder = OneHotEncoder()  # Użycie kodowania One-Hot
    # Kodowanie cechy 'Embarked'
    matrix = encoder.fit_transform(X[['Embarked']]).toarray()
    column_names = ["C", "S", "Q", "N"]  # Nazwy kolumn
    for i in range(len(matrix.T)):
      X[column_names[i]] = matrix.T[i]  # Dodanie zakodowanych kolumn do danych

    # Kodowanie cechy 'Sex'
    matrix = encoder.fit_transform(X[['Sex']]).toarray()
    column_names = ["Female", "Male"]  # Nazwy kolumn
    for i in range(len(matrix.T)):
      X[column_names[i]] = matrix.T[i]  # Dodanie zakodowanych kolumn do danych

    return X

# Definicja klasy do usunięcia zbędnych cech
class FeatureDropper(BaseEstimator, TransformerMixin):
  def fit(self, X, y=None):
    return self

  def transform(self, X):
    return X.drop(["Embarked","Name","Ticket","Cabin","Sex","N"], axis = 1, errors="ignore")  # Usunięcie wybranych kolumn

# Utworzenie potoku przetwarzania danych
from sklearn.pipeline import Pipeline
pipeline = Pipeline([("ageimputer", AgeImputer()),  # Krok imputacji wieku
                    ("featureencoder", FeatureEncoder()),  # Krok kodowania cech
                    ("featuredropper", FeatureDropper())])  # Krok usunięcia cech

# Przetworzenie zestawu treningowego
strat_train_set = pipeline.fit_transform(strat_train_set)

# Wyświetlenie przetworzonego zestawu treningowego
strat_train_set

# Wyświetlenie informacji o przetworzonym zestawie treningowym
strat_train_set.info()

# Importowanie narzędzia do skalowania danych
from sklearn.preprocessing import StandardScaler

# Przygotowanie danych do modelowania
X = strat_train_set.drop(['Survived'], axis=1)  # Cechy
y = strat_train_set['Survived']  # Etykieta

# Skalowanie danych
scaler = StandardScaler()
X_data = scaler.fit_transform(X)
y_data = y.to_numpy()

# Importowanie klasyfikatora i narzędzia do strojenia hiperparametrów
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

# Utworzenie klasyfikatora
clf = RandomForestClassifier()

# Definicja siatki hiperparametrów
param_grid = [
    {"n_estimators": [10, 100, 200, 500], "max_depth": [None, 5, 10], "min_samples_split": [2,3,4]}
]

# Utworzenie i uruchomienie wyszukiwania siatki
grid_search = GridSearchCV(clf, param_grid, cv=3, scoring="accuracy", return_train_score=True)
grid_search.fit(X_data, y_data)

# Wybranie najlepszego estymatora
final_clf = grid_search.best_estimator_

# Wyświetlenie najlepszego klasyfikatora
final_clf

# Przetworzenie zestawu testowego
strat_test_set = pipeline.fit_transform(strat_test_set)

# Wyświetlenie przetworzonego zestawu testowego
strat_test_set

# Przygotowanie danych testowych
X_test = strat_test_set.drop(['Survived'], axis = 1)
y_test = strat_test_set['Survived']

# Skalowanie danych testowych
scaler = StandardScaler()
X_data_test = scaler.fit_transform(X_test)
y_data_test = y_test.to_numpy()

# Ocena modelu na danych testowych
final_clf.score(X_data_test, y_data_test)

# Przetworzenie pełnego zestawu danych
final_data = pipeline.fit_transform(train_data)

# Wyświetlenie przetworzonych danych
final_data

# Przygotowanie pełnego zestawu danych do modelowania
X_final = final_data.drop(['Survived'], axis=1)
y_final = final_data['Survived']

# Skalowanie pełnego zestawu danych
scaler = StandardScaler()
X_data_final = scaler.fit_transform(X_final)
y_data_final = y_final.to_numpy()

# Utworzenie nowego klasyfikatora
prod_clf = RandomForestClassifier()

# Definicja siatki hiperparametrów dla pełnego zestawu danych
param_grid = [
    {"n_estimators": [10, 100, 200, 500], "max_depth": [None, 5, 10], "min_samples_split": [2,3,4]}
]

# Utworzenie i uruchomienie wyszukiwania siatki dla pełnego zestawu danych
grid_search = GridSearchCV(prod_clf, param_grid, cv=3, scoring="accuracy", return_train_score=True)
grid_search.fit(X_data_final, y_data_final)

# Wybranie najlepszego estymatora dla pełnego zestawu danych
prod_final_clf = grid_search.best_estimator_

# Wyświetlenie najlepszego klasyfikatora dla pełnego zestawu danych
prod_final_clf

# Wczytuje dane testowe z pliku CSV, które będą używane do oceny finalnego modelu.
test_data = pd.read_csv("test.csv")

# rzetwarzanie danych testowych
final_test_data = pipeline.fit_transform(test_data)

# Przygotowanie cech do modelu
# Przypisuje przetworzone dane do zmiennej X_final_test i wypełnia brakujące wartości w danych (jeśli takie występują) metodą forward fill (ffill). 
# Metoda ffill wypełnia brakujące wartości używając ostatniej dostępnej wartości w danych.
X_final_test = final_test_data
X_final_test = X_final_test.fillna("ffill")

# Normalizacja cech
scaler = StandardScaler()
X_data_final_test_= scaler.fit_transform(X_final_test)

# Generowanie predykcji:
predictions = prod_final_clf.predict(X_data_final_test)

# Tworzy DataFrame final_df z kolumną PassengerId, dodaje do niego wyniki przewidywań (Survived), zapisuje to jako plik CSV "wyniki.csv"
final_df = pd.DataFrame(test_data['PassengerId'])
final_df['Survived'] = predictions
final_df.to_csv("wyniki.csv", index=False)

# Jeśli wszystko zostało wykonane poprawnie, final_df powinien zawierać dwie kolumny: PassengerId i Survived, gdzie Survived zawiera przewidywane etykiety przeżycia pasażerów.
final_df