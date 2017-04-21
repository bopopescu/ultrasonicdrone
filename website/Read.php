<?php 
	//connect
	$conn = mysql_connect('localhost', 'root', 'ultra', 'drone_data');
	if(!$conn){
	mysql_close($conn);
	echo ('die'); 
	//die ('Error');
	mysql_close($conn);
	exit; 
	} 	
	$db = mysql_select_db('drone_data', $conn); 
	if(!$db){
	echo('mess in db'); 
	mysql_close($conn);
	exit; 
	}
	//get
        $find = "SELECT' 'height' FROM 'data' ORDER BY 'time' DESC LIMIT 1";
	$query = mysql_query($find, $conn);

	if($query){
	echo($query); 
	mysql_close($conn);
        exit; 
	} 
	else{
	echo ('Error with instruction');  
	mysql_close($conn);
	exit;
	}  
?>
