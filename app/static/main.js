$('.r').click(function(){
	console.log(this.classList[1] + ": " + this.classList[2])
	$.get( '/api',{relay:this.name[0],mode:this.name[1]})
	$(".font"+this.name[0]).css('color', 'blue');
});    