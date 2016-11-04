var senha = document.getElementById("senha"),
	conf_senha = document.getElementById("csenha");

function validatePassword(){
  if(senha.value != conf_senha.value) {
    conf_senha.setCustomValidity("As senhas são diferentes!");
  } else {
    conf_senha.setCustomValidity('');
  }
}

senha.onchange = validatePassword;
conf_senha.onkeyup = validatePassword;