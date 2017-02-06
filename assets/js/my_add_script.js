$(document).ready(function(){ 
    var options = {
      url : '/add_data',
      dataType:'json',
      beforeSubmit: showRequest,
      success : showResponse,
    };
    $('#my_add_info').submit(function(){
      $(this).ajaxSubmit(options);
      return false;
    });
});


function showRequest(formData,jqForm,options){
  $('body').addClass("loading"); 
  return true
}
function showResponse(json){
  $('body').removeClass("loading");
  if (json.ok_message){
    if(!alert(json.ok_message)){document.location = 'http://127.0.0.1:8000/'};
  };
}