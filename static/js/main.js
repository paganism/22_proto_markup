$.getJSON('https://api.sypexgeo.net').done(function (location){
   var city = location['city']['name_ru'];
   var country = location['country']['name_ru'];
   $.notify(
       {
           icon: 'glyphicon glyphicon-globe',
           title: city + ', ' + country,
           message: 'Правильно?'
       },
       {
           type: 'info',
           allow_dismis: true,
           placement: {
               from: 'top',
               align: 'left'
           },
           offset: {x: 40, y: 60},
           position: 'absolute',
           mouse_over: 'pause',
           delay: 10000,
           icon_type: 'class',
           template: $("#popup-template").html()
       }
   )
});


