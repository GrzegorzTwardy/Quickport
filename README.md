# Założenia
Aplikacja desktopowa, która automatyzuje import i transformację cenników z plików Excel do struktury Salesforce. Wykorzystuje konfigurowalne pliki JSON do mapowania kolumn, definiowania reguł transformacji i walidacji danych. Aplikacja wspiera profile konfiguracyjne, dzięki czemu można łatwo pracować z różnymi środowiskami Salesforce i zestawami mapowań.

# Co już działa (moduły):
 - pliki widoków,
 - tworzenie i zapis pliku .json mappera za pomocą GUI
 - mapowanie danych z cenników xlsx/xls za pomocą pliku .json mappera do csv (dla obiektu Product2, ProductEntries w trakcie)

 # Co zostało:
 - api z Salesforce,
 - serwis profili,
 - widoki: menu, profile i ich integracja
