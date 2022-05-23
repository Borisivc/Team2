jQuery.validator.addMethod("customEmail", function(value, element) { 
    return this.optional( element ) || /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test( value ); 
}, "Ingrese un email valido!");
$.validator.addMethod( "alphanumeric", function( value, element ) {
return this.optional( element ) || /^\w+$/i.test( value );
}, "Solo letras, numeros y guiones bajos estan permitidos" );
var $ingreso = $('#ingreso');
if($ingreso.length){
    $ingreso.validate({
        rules:{
            username: {
                required: true,
                alphanumeric:true
            },
            password: {
                required: true
            }
        },
        messages: {
            username: {
                requirid:'Por favor ingrese usuario'
            },
            password: {
                required:'Por favor ingrese contraseña'
            }
        }
    })    
}
var $registrationForm = $('#registro');
if($registrationForm.length){
    $registrationForm.validate({
        rules:{
            username2: {
                required: true,
                alphanumeric:true
            },
            email:{
                required: true,
                customEmail: true
            },
            password2: {
                required: true
            },
            confirm: {
                required: true,
                equalto: '#password2'
            }
        },
        messages:{
            username2: {
                required: 'Por favor ingrese usuario'
            },
            email:{
                required: 'Por favor ingrese un email',
                email: 'Ingrese un email valido'
            },
            password2: {
                required: 'Por favor ingrese una contraseña'
            },
            confirm: {
                required: 'Por favor confirme contraseña',
                equalto: 'Las contraseñas deben ser iguales'
            }
        }    

    })
}
var $registroContra = $('#recuperacontrase');
if($registroContra.length){
    $registroContra.validate({
        rules: {
            username3: {
                required: true,
                alphanumeric: true,                
            },
            email2: {
                required: true,
                customEmail: true,                
            },
            password3: {
                required: true
            }
        },
        messages:{
            username3: {
                required: 'Por favor ingrese usuario'
            },
            email2: {
                required: 'Por favor ingrese un email',
                email2: 'Ingrese un email valido'
            },
            password3: {
                required: 'Por favor ingrese una contraseña'
            }
        }
    })
}

