$(function(){
   var $registerForm = $("#registro");
   if($registerForm.length){
    $registerForm.validate({
        rules:{
            username:{
                required: true
            }
        },
        password: {
            required: true
        },
        messages:{
            Usuario:{
                required: 'Usuario es requerido'
            }
        }
    })
   }

})