$(document).on('submit','#my_add_info',function(e){
  e.preventDefault();

  $.ajax({
    type:"POST",
    url:"/add_data",
    data:{
      name:$('#id_name').val(),
      surname:$('#id_surname').val(),
      contacts:$('#id_contacts').val(),
      bio:$('#id_bio').val(),
      birthday:$('#id_birthday').val(),
      photo:$('input.form-control').val(),
      csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
    },
    success:function(json){
      my_error_add(json);
      if(json.ok_message){
        if(!alert(json.ok_message)){document.location = 'http://127.0.0.1:8000/'};
      };           
    },
  });
});
      /*if(json.username){
        console.log(Object.keys(json));
        $('#id_username').parent().attr('id','username_error');
        for(var i = 0;i<json.username.length;i++){
          if ($('ul#username_error_'+[i]).text()){  
            $('ul#username_error_'+[i]).replaceWith("<ul class = 'error'" +"id=username_error_"+[i]+"><li>"+json.username[i]+"</li></ul>")
          }else{
            $('#id_username').parent().prepend("<ul class = 'error'" +"id=username_error_"+[i]+"><li>"+json.username[i]+"</li></ul>");
          };
        };
      }else{
        $('p#username_error ul').replaceWith('');
      };        
      if(json.password1) {
        $('#id_password1').parent().attr('id','password1_error');
        for(var i = 0;i<json.password1.length;i++){
          if ($('ul#password1_error_'+[i]).text()){  
            $('ul#password1_error_'+[i]).replaceWith("<ul class = 'error'" +"id=password1_error_"+[i]+"><li>"+json.password1[i]+"</li></ul>")
          }else{
            $('#id_password1').parent().prepend("<ul class = 'error'" +"id=password1_error_"+[i]+"><li>"+json.password1[i]+"</li></ul>");
          };
        };
      }else{
        $('p#password1_error ul').replaceWith('');
      }; 
      if(json.password2){
        $('#id_password2').parent().attr('id','password2_error');
        for(var i = 0;i<json.password2.length;i++){
          if ($('ul#password2_error_'+[i]).text()){  
            $('ul#password2_error_'+[i]).replaceWith("<ul class = 'error'" +"id=password2_error_"+[i]+"><li>"+json.password2[i]+"</li></ul>")
          }else{
            $('#id_password2').parent().prepend("<ul class = 'error'" +"id=password2_error_"+[i]+"><li>"+json.password2[i]+"</li></ul>");
          };
        };
      }else{
        $('p#password2_error ul').replaceWith('');
      }; 
      if(json.new_user){
        if(!alert(json.new_user)){document.location = 'http://127.0.0.1:8000/'};
      };
    },
  });
});*/  

/*$(document).ready(function() { 
    var options = {
      beforesubmit: showRequest,
      success : showResponse,
      url : '/add_data',
      type : 'POST'
    };
    $(#'my_add_info').submit(function(){
      $(this).ajaxSubmit(options);
      return false;
    });
});
var formData = {name:$('id_name').val()}

function showRequest(formData,options){
  alert('About to submit')
  return true
}>*/