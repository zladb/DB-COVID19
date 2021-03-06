// DB TEAM PROJECT #3 - 5팀(김유진, 이지원)</br>

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

<html>
<style>
    table {
        width: 100%;
        border: 1px solid #444444;
        border-collapse: collapse;
    }
    th, td {
        border: 1px solid #444444;
    }
</style>
<body>
    <?php
        $sql="select count(*) from WEATHER;";
        $result = mysqli_query($link, $sql);
        $data = mysqli_fetch_assoc($result);
        print "<p><h3>WEATHER table (Currently " . $data['count(*)'] . " rows in database)</h3></p>";
    ?>
    <table class = "table table-striped">
        <tr>
            <th>weather_code</th>
            <th>province</th>
            <th>wdate</th>
            <th>avg_temp</th>
            <th>min_temp</th>
            <th>max_temp</th>
        </tr>

        <?php
            $sql = "select * from WEATHER ORDER BY wdate asc;";
            $result = mysqli_query($link, $sql);
            while($row = mysqli_fetch_assoc($result)){
                print "<tr>";
                foreach ($row as $key => $val){
                    print "<td>" . $val . "</td>";
                }
                print "</tr>";
            }
        ?>
    </table>
</body>
</html>
