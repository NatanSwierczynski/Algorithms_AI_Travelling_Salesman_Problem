# Optymalizacja trasy podczas zakupów w hipermarkecie

Jest to wariancja problemu komiwojażera, gdzie:
- Na płaszczyźnie umieszczone są „przeszkody” (półki sklepowe), przez które przejście jest niemożliwe,
- Ograniczenie możliwości poruszania się poprzez zmianę kierunku tylko o 90° lub -90°,
- Trasa rozpoczyna i kończy się w określonych miejscach
- Każdy ruch ma taką samą wagę.

Główne cele aplikacji:
- Wyznaczenie trasy zakupów - przejście od punktu wejściowego do punktu wyjściowego, po jak najkrótszej trasie, która pozwoli na przejście przez wszystkie punkty kontrolne,
- Optymalizacja trasy pomiędzy poszczególnymi punktami kontrolnymi,
- Optymalizacja kolejności przechodzenia przez punkty kontrolne.

Wykorzystane algorytmy:
- BFS, DFS, A* - wykorzystane do wyznaczenia tras pomiędzy poszczególnymi produktami.
- Symulowane wyżarzanie – wykorzystany do wyznaczenia kolejności przechodzenia przez punkty kontrolne.

Interfejs użytkownika został zrobiony w konsoli.

Przykladowe dzialanie aplikacji:

Labirynt poczatkowy z wylosowanymi produktami oznaczonymi kolejnymi literami alfabetu:

![image](https://github.com/NatanSwierczynski/Algorytmy_AI/assets/106707211/2a3883c4-49bd-4225-9fe9-a3f4fe9ba7db)

Wyznaczona trasa:

![image](https://github.com/NatanSwierczynski/Algorytmy_AI/assets/106707211/45465956-1a63-49dd-be19-d29f0461a765)




