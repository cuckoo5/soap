var http_path = "/"
$(document).ready(function () {
	//模态窗口居中
    $("div[role='dialog']").on("show.bs.modal", function() {  
        // 具体css样式调整  
        $(this).css({  
            "display": "block",  
            "margin-top": function() {  
                return ($(this).height() / 3);  
            }  
        });  
    });
});

function click_a(relative_path){
	window.location.href = http_path + relative_path;
}

function open_login_modal(){
	$('#login_modal').modal('show');
	init_login_form_validation();
}


/**
 *设置Cookies 
 */
function set_cookie(name,value,day){
	var Days = day; 
	var exp  = new Date();    //new Date("December 31, 9998");
	exp.setTime(exp.getTime() + Days*24*60*60*1000);
	document.cookie = name + "="+ escape (value) + ";path=/;expires=" + exp.toGMTString();
}

/**
 *读取Cookies 
 */
function get_cookie(name){
	var arr = document.cookie.match(new RegExp("(^| )"+name+"=([^;]*)(;|$)"));
	if(arr != null) return unescape(arr[2]); return "";
}

/**
 *清除Cookies 
 */
function del_cookie(name){
	var exp = new Date();
	exp.setTime(exp.getTime() - 1270719748000);
	var cval=getCookie(name);
	if(cval!=null) document.cookie= name + "="+cval+";expires="+exp.toGMTString();
	//document.cookie = name + "=; expires=Fri, 31 Dec 1999 23:59:59 GMT;";
}