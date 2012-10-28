<?php 
include 'pages/special/header.php';
include 'pages/special/menu.php';
if(isset($_GET['page']))
{
	$file='pages/' . $_GET['page'] . '.php';
	if(file_exists($file))
	{
		include $file;
	}
	else
	{
		include 'pages/special/not_exists.php';
	}
}
else
{
	include 'pages/home.php';
}
include 'pages/special/footer.php'; 
?> 
