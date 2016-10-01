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
});
