Gauge = function(id) {
	//canvas initialization
	var canvas=document.getElementById(id);
	var ctx = canvas.getContext("2d");
	
	//dimensions
	var W = canvas.width;
	var H = canvas.height;
	
	//Variables
	var data =30;
	var degrees = 45;
	var new_degrees = 0;
	var difference = 0;
	var color = "lightgreen"; //green looks better to me
	var bgcolor = "lightgrey";
	var text;

	this.draw=function(data) {
		var d=parseInt(data)
	//Clear the canvas everytime a chart is drawn
	ctx.clearRect(0, 0, W, H);
		
	//Background 360 degree arc
	ctx.beginPath();
	ctx.strokeStyle = bgcolor;
	ctx.lineWidth = 20;
	ctx.arc(W/2, H/2, 70, -225/180*Math.PI, 45/180*Math.PI, false); //you can see the arc now
	ctx.stroke();
		
	//gauge will be a simple arc
	//Angle in radians = angle in degrees * PI / 180
	ctx.beginPath();
	ctx.strokeStyle = color;
	ctx.lineWidth = 20;
	//The arc starts from the rightmost end. If we deduct 90 degrees from the angles
	//the arc will start from the topmost end
        val_max = 1500;
	ctx.arc(W/2, H/2, 70, - 225*Math.PI/180, (-225+270/val_max*d)/180*Math.PI, false); 
	//you can see the arc now
	ctx.stroke();
	
		ctx.fillStyle = color;
		ctx.font = "15px Arial";
		text = data + " hPa";
		//Lets center the text
		//deducting half of text width from position x
		text_width = ctx.measureText(text).width;
		//adding manual value to position y since the height of the text cannot
		//be measured easily. There are hacks but we will keep it manual for now.
		ctx.fillText(text, W/2 - text_width/2, H/2);
	};
};
