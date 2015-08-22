$("#newQuestionSubmit").click(function(){
	var val = $("#newQuestion").val(); 
	if (val == ""){
		$("#questionError").html("A Quetion cannot be an empty string");
	}
	else{
		$.post('addQuestion/', {'newQuestion':val}, 
		function(data, status){
			if (data.length > 40){
				document.clear();
				document.open();
				document.write(data);
				document.close();
			}
			else{
				$("#questionError").html(data);
			}
		});
	}
});

