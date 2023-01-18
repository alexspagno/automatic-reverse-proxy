<html>
<body>
<?php
$myfile = fopen("user1.cfg", "r") or die("Unable to open file!");
$new_url = fread($myfile,filesize("user1.cfg"));
fclose($myfile);
header("location:" . $new_url);
?>
</body>
</html>