function my_error_add(obj){
  var my_error_list = Object.keys(obj);
  for (var i = 0;i<my_error_list.length;i++){
            $('#id_'+ my_error_list[i]).parent().attr('id',my_error_list[i]);            
            var error_keys = my_error_list[i];
            var my_p = $('p');
            for (var e =0;e<my_p.length;e++){
              if(my_error_list.indexOf(my_p[e].id) == -1){
                my_p[e].id = e;
                $('p#'+e+' ul').replaceWith('');
              }else{
                  for (var y = 0;y<obj[error_keys].length;y++){
                      if ($('ul#'+error_keys+'_error_'+[y]).text()){
                        $('ul#'+error_keys+'_error_'+[y]).replaceWith("<ul class = 'error'" +"id="+error_keys+'_error_'+[y]+"><li>"+obj[error_keys][y]+"</li></ul>")
                      }else{
                         $('#id_'+ my_error_list[i]).parent().prepend("<ul class = 'error'" +"id="+error_keys+'_error_'+[y]+"><li>"+obj[error_keys][y]+"</li></ul>")
                      }; 
                  };
              };    
          };
  };
};

function me_error_delete(obj){
  var my_error_list = Object.keys(obj);
  var my_p = $('p');
  for (var i = 0;i<my_error_list.length;i++){
    my_error_list_name = my_error_list[i]+'_error'
    for (var e = 0;e<my_p.length;e++){
      if (my_p[e].id != my_error_list_name){
        my_p[e].id = e;
        $('p#'+e+' ul').replaceWith('');    
      }else{
        $('#id_'+ my_error_list[i]).parent().attr('id',my_error_list[i] + '_error');
        var error_keys = my_error_list[i]
        for (var y = 0;y<obj[error_keys].length;y++){
          if ($('ul#'+error_keys+'_error_'+[y]).text()){
            $('ul#'+error_keys+'_error_'+[y]).replaceWith("<ul class = 'error'" +"id="+error_keys+'_error_'+[y]+"><li>"+obj[error_keys][y]+"</li></ul>")
          }else{
            $('#id_'+ my_error_list[i]).parent().prepend("<ul class = 'error'" +"id="+error_keys+'_error_'+[y]+"><li>"+obj[error_keys][y]+"</li></ul>")
          }; 
        };
      }
    };
  };
};

$(document).on('submit','#my_registration_form',function(e){
  e.preventDefault();

  $.ajax({
    type:"POST",
    url:"/my_registration",
    data:{
      username:$('#id_username').val(),
      password1:$('#id_password1').val(),
      password2:$('#id_password2').val(),
      csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
    },
    success:function(json){
        my_error_add(json);   
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
