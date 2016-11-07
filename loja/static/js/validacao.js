// Comandos JavaScript

function validarTamSenha(senha) {
	if (senha.value.length < 4)
		senha.setCustomValidity("A senha deve ter no minimo 4 caracteres!");
	else
		senha.setCustomValidity('');
}

function validarSenha(senha, conf_senha){	
  	if(senha.value != conf_senha.value) 
  		conf_senha.setCustomValidity("As senhas são diferentes!");
  	else
  		conf_senha.setCustomValidity('');
}

//Comandos JQuery
// Ainda nao esta funcionando

jQuery(function($){
   $("cep").mask("xxxxx-xxx");
//   $("#phone").mask("(999) 999-9999");
  //  $("#tin").mask("99-9999999");
   // 	$("#ssn").mask("999-99-9999");
});