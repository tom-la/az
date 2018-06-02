## Sposób użycia

Program wynikowy `az-tree.exe` znajduje się w folderze *dist*.
Argumentem programu jest dwuwymiarowa tablica wartości typu `int`.
Program wypisuje na wyjściu odpowiadający ciąg Prüfera oraz słownik zawierający zapis drzewa (kluczami są numery wierzchołków, a wartościami listy sąsiadów).
Możliwe są dwa sposoby podania argumentu:

### Plik csv

`./az-tree.exe --file ./tree.csv`

Przykładowy, odpowiednio sformatowany plik csv znajduje się w folderze *src*.

### Konsola

`./az-tree.exe --distances "[[0, 2, 3], [2, 0, 3], [3, 3, 0]]"`

Zapis argumentu musi być poprawnym zapisem dwuwymiarowej listy w języku Python.

### Rysowanie drzewa

Program pozwala na wygenerowanie pliku PNG z rysunkiem wyjściowego grafu, za pomocą opcjonalnej flagi `--output-file`:

`./az-tree.exe --file ./tree.csv --ouput-file ./tree.png`

**Uwaga:** Ta opcja wymaga zainstalowania pakietu [graphviz](http://www.graphviz.org/ "Graphviz").


## Tworzenie pliku wykonywalnego

Aby stworzyć nowy plik .exe należy użyć biblioteki [pyinstaller](http://www.pyinstaller.org/ "PyInstaller").

W folderze *src* należy wykonać:
`pyinstaller --onefile ./az-tree.py`