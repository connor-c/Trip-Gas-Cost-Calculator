$(document).ready(function() {
  $('#option2').change(function() {
    var pathName = window.location.pathname;
    if((pathName == '/') || (pathName == '/calculated_addresses/')) {
      window.location = '../use_distance';
    }
  });
});

$(document).ready(function() {
  $('#option1').change(function() {
    var pathName = window.location.pathname;
    if((pathName == '/use_distance/') || (pathName == '/calculated_distance/')) {
      window.location = '../';
    }
  });
});
