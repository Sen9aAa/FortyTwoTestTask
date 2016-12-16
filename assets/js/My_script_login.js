$('#my_login').on('click','#my_login_submit',function(e){
  e.preventDefault();

  $.ajax({
    type:"POST",
    url:"/my_login",
    data:{
      username:$('[type="text"]').val(),
      password:$('[type="password"]').val(),
      csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
    },
    success:function(json){
      if(json.username){
        if(!alert('Welkome '+json.username)){document.location = 'http://127.0.0.1:8000/'};
      };
    },
  });
})

$('#my_logout').on('click','#my_logout_submit',function(e){
  e.preventDefault();

  $.ajax({
    type:'POST',
    url:"/my_logout",
    data:{
      csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
    },
    success:function(json){
        if(!alert(''+json.bay)){document.location = 'http://127.0.0.1:8000/'};
    },
  })
})