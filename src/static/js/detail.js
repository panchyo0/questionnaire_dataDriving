// answers validation when submit.
window.onload=function(){
  var btn=document.getElementById('sub_form');
  btn.addEventListener('click',function showMessage(event){
        var check=[];
        $('textarea').each(function(){
          var content=$(this).val();
          if (content) {
            $('h5').remove();
            check.push(1);
          } else {
            $(this).before("<h5>Please answer this question and try submit again.</h5>");
            $('h5').css({"color": "red"});
            check.push(0);
          }
        });
        var counter=0;
        for (var i = 0; i < check.length; i++) {
          if (check[i]) {
            counter+=check[i]
          }
        }
        if (counter==check.length) {
          $('#formsubmit').submit() ;
          alert("Save Succee. Thanks for your time.");
        }
      }
  ,false);
}

// change textarea UI
$(document).ready(function(){
  $('textarea').addClass('form-control');
  $('textarea').css({"height": "70px"});

});
