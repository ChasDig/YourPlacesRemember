function init() {

  let RememberMap,
      // Create map:
      map = new ymaps.Map('map', {

        center: [56.022798299805636, 92.89742899999986],
        zoom: 11

      });

  // Lisen events:
  map.events.add('click', function (e) {

    // Get coordinate:
    let coord_memory = e.get('coords');

    // Make marker:
    if (RememberMap) {

      RememberMap.geometry.setCoordinates(coord_memory)

    }
    else {

      RememberMap = createRememberPlaces(coord_memory)
      map.geoObjects.add(RememberMap)

    }

    getAddress(coord_memory);

  });

  // Create marker:
  function createRememberPlaces(coord_memory) {

    return new ymaps.Placemark(coord_memory, {}, {

      iconLayout: "default#image",
      iconImageHref: "https://cdn-icons-png.flaticon.com/512/9131/9131546.png"

    });
  }


  // Обратное геокодирование (адрес по координатам):
    function getAddress(coords) {
        ymaps.geocode(coords).then(function (res) {
            var GeoObject_1 = res.geoObjects.get(0);

            RememberMap.properties
                .set({
                    // Данные о выбранном объекте:
                    iconCaption: [
                        // Название выбранного объекта (его официальное название):
                        GeoObject_1.getLocalities().length ? GeoObject_1.getLocalities() : GeoObject_1.getAdministrativeAreas(),
                        // Получаем наименование здания:
                        GeoObject_1.getThoroughfare() || GeoObject_1.getPremise()
                    ].filter(Boolean).join(', '),
                    // Балун - строкф с адресом объекта:
                    balloonContent: GeoObject_1.getAddressLine()
                });

            // Записываем значение в скрытое поле формы для отправки на сервер:
            document.getElementById('id_address').value = GeoObject_1.getAddressLine();
        });
    }
}

ymaps.ready(init);
