$(document).ready(function () {
	init_validation();
});

function search() {
	use = $("#use").val();
	skin_type = $("#skin_types").val();
	difficult_degree = $("#difficult_degree").val();
	
	datas = {
		use : use,
		skin_type : skin_type,
		difficult_degree : difficult_degree
	}
	$.get(http_path + "formula/index", datas)
}


function add_formula(){
	window.location.href = http_path + "formula/new";
}

function init_validation() {
	$("input,select,textarea").jqBootstrapValidation({
		preventSubmit : true,
		submitError : function($form, event, errors) {
		},
		submitSuccess : function($form, event) {
			//TODO
			event.preventDefault();
		},
		filter : function() {
			return $(this).is(":visible");
		}
	});
}
