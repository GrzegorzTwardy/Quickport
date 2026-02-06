# Założenia
Aplikacja desktopowa, która automatyzuje import i transformację cenników z plików Excel do struktury Salesforce. Wykorzystuje konfigurowalne pliki JSON do mapowania kolumn, definiowania reguł transformacji i walidacji danych. Aplikacja wspiera profile konfiguracyjne, dzięki czemu można łatwo pracować z różnymi środowiskami Salesforce i zestawami mapowań.

# Co już działa (moduły):
 - pliki widoków,
 - tworzenie i zapis pliku .json mappera za pomocą GUI
 - mapowanie danych za pomocą mappera
 - ładowanie pliku mappera do GUI (edycja mapppera)
 - API z Salesforce za pomocą Bulk API 2.0 (połączenie z platformą, upsert do Product2 i PricebookEntry)

 # Co zostało:
 - serwis profili,
 - integracja okien