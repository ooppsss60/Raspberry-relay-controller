$.getJSON( "/states.json", function(states) {
	$('.r').click(function(){
		$.get( '/api',{relay:this.name[0],mode:this.name[1]})
		if (this.classList.contains("auto")){
			if (states[this.name[0]-1]){
				$(".font"+this.name[0]).css('color', 'green');
			}else{
				$(".font"+this.name[0]).css('color', 'red');
			}}
		if (this.classList.contains("on")){
			$(".font"+this.name[0]).css('color', 'green')}
		if (this.classList.contains("off")){
			$(".font"+this.name[0]).css('color', 'red')}
	});    
});