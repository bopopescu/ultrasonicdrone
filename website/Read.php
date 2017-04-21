<?php 
	//connect
	$conn = new mysqli('localhost', 'root', 'ultra', 'drone_data');
	if(!$conn){
	mysqli_close($conn);
	echo (json_encode('die')); 
	//die ('Error');
	mysqli_close($conn);
	exit; 
	} 	
	$db = mysqli_select_db('drone_data', $conn); 
	if(!$db){
	echo('mess in db'); 
	mysqli_close($conn);
	exit; 
	}
	//get
        $find = "SELECT height FROM data ORDER BY time DESC LIMIT 1";
	$query = mysqli_query($find, $conn);

	if($query){
	
	echo(($query->fetch_assoc())["height"]);
	//echo(json_encode($query)); 
	//echo json_encode($query); 
	mysql_close($conn);
        exit; 
	} 
	else{
	echo ('Error with instruction');  
	mysqli_close($conn);
	exit;
	}  
?>
