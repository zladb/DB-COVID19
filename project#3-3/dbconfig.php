<?php
    $dPconfig['dbhost'] = 'localhost'; 
    $dPconfig['dbuser'] = 'root';
    $dPconfig['dbpass'] = '####';
    $dPconfig['dbname'] = 'COVID19';

    $db_host = $dPconfig['dbhost'];
    $db_user = $dPconfig['dbuser'];
    $db_pass = $dPconfig['dbpass'];
    $db_name = $dPconfig['dbname'];

    $link = mysqli_connect($db_host, $db_user, $db_pass, $db_name);

    if (mysqli_connect_errno()){
        printf("Connect failed : %s\n", mysqli_connect_error());
        exit();
    }

    mysqli_query($link, "set names utf8");
?>
