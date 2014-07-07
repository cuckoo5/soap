function login(){
	if ($("#username").val() == "") {
		//alert("用户名不能为空。");
		$('#login-alert').show().find('span').html("<strong>警告！</strong>用户名不能为空。");
		$("#username").focus();
		return false;
	}
	if ($("#password").val() == "") {
		$('#login-alert').show().find('span').html("<strong>警告！</strong>密码不能为空。");
		$("#password").focus();
		return false;
	}
	$("#loginform").submit();
}
