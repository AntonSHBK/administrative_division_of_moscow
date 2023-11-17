# Административное деление города Москва и Московской области
## Задача:
Получить границы административных округ и районов города Москва и Московской области.
![Округа города Москва](/imgs/moscow.jpg)

![Районы Московской области](/imgs/moscow_area.jpg)

Для получения границ можно использовать ресурсы [OpenStreetMap](https://nominatim.openstreetmap.org/ui/search.html).

![OpenStreetMap](/imgs/open_street_map.jpg)

Запрос к ресурсу:
```http
https://nominatim.openstreetmap.org/search?q=<название объекта>&polygon_geojson=1&format=json
```

