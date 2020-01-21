<?php
	function display($filename){
		$myfile = fopen("resource/txt/".$filename, "r+") or die("Unable to open file!");
		while(!feof($myfile)) {
			echo fgets($myfile) . "<br>";
		}
		fclose($myfile);
	}

	function setup_html($filename){
		include_once "resource/html/".$filename.".php";
	}
?>

<!DOCTYPE html>
<html>
	<head>
		<?php
			setup_html("head");
			setup_html("script");
		?>
	</head>

	<body>
		<?php
			setup_html("title");
			setup_html("navigation");
			setup_html("module");
		?>
		
	</body>
</html>
