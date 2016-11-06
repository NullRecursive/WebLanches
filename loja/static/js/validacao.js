	
function validarTamSenha(senha) {
	if (senha.value.length < 4)
		senha.setCustomValidity("A senha deve ter no minimo 4 caracteres!");
	else
		senha.setCustomValidity('');
}

function validarSenha(senha, conf_senha){	
  	if(senha.value != conf_senha.value) {
  		conf_senha.setCustomValidity("As senhas são diferentes!");
  	}
  	else
  		conf_senha.setCustomValidity('');
}
//rejeita caracteres que nao sejam digitos
function rejeitaLetras(telefone){
	telefone.value = telefone.value.replace(/\D/g,"")
}

