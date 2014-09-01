// $('#myModal').on('show', function () {
// });

$(document).ready(function () {

});

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

	// $("#loginform").submit();
	user_name = $("#username").val();
	password = $("#password").val();
	alert(user_name);
	alert(password);
	datas = {
		user_name : user_name,
		password : password
	}
	// $.post(http_path + "login", datas, function(result){
		// alert("ccc");
		// $('#login_modal').modal('hide');
	// }, "json");
	
	url = httpPath + "login";
	$.ajax({
	    type: "POST",
	    async: false,
	    url: url,
	    data: datas ,
	    success: function (data) {
	        if (data.errorCode == 0) {
	            process_cookie();
	            set_cookie("token", data.result.token, 1);
	            //关闭登录窗口
	            $('#login_modal').modal('hide');
	            //刷新当前页面
	            window.opener.document.location.reload();
	        } else if (data.errorCode == 2) {
	        	alert("未注册");
	        }else {
	            alert("登录失败");
	        }
	    },
	    error: function (xmlReqObj, textStatus, errorThrown) {
	        alert("Server Error");
	    }
	});
	$("#password").val("");
}

function logout() {
	url = httpPath + "logout";
	$.ajax({
		type: "POST",
		async: false,
		url: url,
		data: '{}',
		success: function(data, textStatus) {
			if (data.errorCode == 0) {
				window.location.href = "/";
			} else {
				alert(data.errorMessage);
			}
		}, error: function() {
	    	alert("Server Error");
		}
	});
}

function login_from_register(){
	//关闭注册窗口
	$('#register_modal').modal('hide');
	//打开登录窗口
	$('#login_modal').modal('show');
}

function register(){
	$("#registerform").submit();
}