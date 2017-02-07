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