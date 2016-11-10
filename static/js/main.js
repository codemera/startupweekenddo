$(function(){

  // Initialize tooltips
  $('[data-toggle="tooltip"]').tooltip();

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
});
