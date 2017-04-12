<?php 
function getLast(){ 
	//connect
	$conn = mysql_connect('localhost', 'root', 'ultra', 'drone_data');
	if(!$conn){
	die ('Error');
	mysqli_close($conn);
	echo ('die'); 
	exit; 
	} 	
	$db = mysql_select_db("data", $conn); 
	if(!$db){
	die('fail');
	mysql_close($conn);
	exit; 
	}
	//get
        $find = "SELECT' 'height' FROM 'data' ORDER BY 'time' DESC LIMIT 1"
	$query = mysql_query($find, $conn);
	
	if($query){
	echo($query); 
	mysql_close($conn);
        exit; 
	} 
	else{
	echo ('Error');  
	mysql_close($conn);
	exit;
	}  
	
}
?>
