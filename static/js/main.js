$.getJSON('https://api.sypexgeo.net').done(function (location){
   var city = location['city']['name_ru'];
   var country = location['country']['name_ru'];
   $.notify(
       {
           icon: 'glyphicon glyphicon-globe',
           title: city + ', ' + country,
           message: 'Правильно'
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
           delay: 3000,
           icon_type: 'class',
           template:   '<div data-notify="container" class="col-xs-11 col-sm-3 alert alert-{0}" role="alert">' +
                  '<button type="button" aria-hidden="true" class="close" data-notify="dismiss">×</button>' +
                  '<span data-notify="icon"></span> ' +
                  '<span data-notify="title">Ваш регион: <b>{1}</b></span> ' +
                  '<div class="text-center"><span data-notify="message">{2}</span></div>' +
                  '<div class="text-center">'+
                  '<a class="btn btn-info btn-sm" data-notify="dismiss">Да</a>' +
                  '<span>&nbsp;</span>' +
                  '<a class="btn btn-info btn-sm" data-notify="dismiss" id="button_error_location">Нет</a>' +
                  '</div>'+
                                '</div>'
       }
   )
});

$('.carousel').carousel({interval: 3000});

var regionList = ['Московская область', 'Ленинградская область', 'Новгородская область', 'Псковская область', 'Мурманская область'];
$.each(regionList, function(i){
  var li = '<li><a href=#>' + regionList[i] + '</a></li>';
  $('ul.dropdown-menu.regions').append(li)
})
