// Variables for radio buttons
var selectedColor = 'white';
var unselectedColor = 'gray';
var hoverColor = '#CCC';
var selectedId = null;
$(".radioButton").click(function() {
	if ($(this).attr('name') == 'unselected'){
		$(this).css('background-color', selectedColor);
		$(".radioButton").each(function() {
			if ($(this).attr('name') == 'selected'){
				$(this).attr('name', 'unselected');
				$(this).css('background-color', unselectedColor)
			}
		});
		selectedId = $(this).attr('id');
		$(this).attr('name', 'selected');
	}
});
$(".radioButton").hover(function(){
	if ($(this).attr('name') != 'selected'){
		$(this).css('background-color', hoverColor);
	}
}, function() {
	if ($(this).attr('name') != 'selected'){
		$(this).css('background-color', unselectedColor);
	}
});

$(".voteButton").click(function(){
	if (selectedId == null){
		$("#errorMessage").html("You didn't select a choice");
	}
	else{
		$.post('vote/', 
		{'choice': selectedId}, 
			function(data, status){
				if (data.length > 40){
					document.clear();
					document.open();
					document.write(data);
					document.close();
				}
				else{
					$("#errorMessage").html(data);
				}
		});
	}
});

$("#newChoiceSubmit").click(function(){
	var val = $("#newChoice").val();
	if (val == ""){
		$("#errorMessage").html("Choices cannot be empty");
	}
	else{
		$.post('addChoice/', {'newChoice':val},
		function(data, status){
			if (data.length > 40){
				document.clear();
				document.open();
				document.write(data);
				document.close()
			}
			else{
				$("#errorMessage").html(data);
			}
		});
	}

});
