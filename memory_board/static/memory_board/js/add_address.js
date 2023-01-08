ymaps.ready(init);
function init() {

    // Строка с адресом, который необходимо геокодировать
    var address = document.getElementById('address').innerHTML;

    // Поиск объекта:
    var myGeocoder = ymaps.geocode(address);

    myGeocoder.then(
    function (res) {

        // Создание карты и доп. параметры
        var myMap = new ymaps.Map("map_add", {
            center: res.geoObjects.get(0).geometry.getCoordinates(),
            zoom: 12,
        });

        myMap.controls.remove('geolocationControl'); // удаляем геолокацию
        myMap.controls.remove('searchControl'); // удаляем поиск
        myMap.controls.remove('trafficControl'); // удаляем контроль трафика
        myMap.controls.remove('rulerControl'); // удаляем контрол правил
        myMap.behaviors.disable(['scrollZoom']); // отключаем скролл карты (опционально)

        myMap.behaviors.disable('drag');

        myMap.geoObjects.add(res.geoObjects);

    }
    );

}



