
function validarSenha(senha, conf_senha){	
  	if(senha.value != conf_senha.value) 
  		conf_senha.setCustomValidity("As senhas são diferentes!");
  	else
  		conf_senha.setCustomValidity('');
}