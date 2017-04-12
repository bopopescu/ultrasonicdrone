<?php 
function getLast(){ 
	//connect
	$conn = mysqli_connect('localhost', 'root', 'ultra', 'drone_data') or die ("Error");
	
	//get
        $find = "SELECT' 'height' FROM 'data' ORDER BY 'time' DESC LIMIT 1"
	$query = mysqli_query($conn, $find) or die ("Error");
	
	if($query){
	echo($query); 
	mysqli_close($conn);
        exit; 
	} 
	else{
	echo "Error";  
	exit;
	}  
	
}
?>
