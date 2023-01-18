</head>
<body>
 <?php
$newUrl = $_GET['url'];
$myfile = fopen("user1.cfg", "w") or die("Unable to open file!");
fwrite($myfile, $newUrl);
fclose($myfile);
printf("new URL: " . $newUrl);
?> 
</body>
</html>
