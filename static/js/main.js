$(function(){

  // Show exra fields when user selects 'Yes'
  $(document).ready(function() {
    $('input[type=radio]').click(function () {
       if (this.id == "mce-MMERGE3-0") {
           $(".extra-fields").show();
       } else {
           $(".extra-fields").hide();
       }
   });
  });

  // Adds smooth scrolling functionality for anchor tags
  // (excludes anchor tags with data-toggle="collapse")
  $(function() {
    $('a[href*="#"]:not([data-toggle="collapse"])').click(function() {
      if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
        if (target.length) {
          $('html, body').animate({
            scrollTop: target.offset().top
          }, 1000);
          return false;
        }
      }
    });
  });

  // Instafeed initializer
  var feed = new Instafeed({
		get: 'user',
		clientId: '694f51e4c5964fdca7df9a493fcea120',
		accessToken: '3203931.694f51e.05905d3d8be4472b99a9c92b20988c0e',
		userId: 1542077877,
		limit: 12
	});
	feed.run();
});
