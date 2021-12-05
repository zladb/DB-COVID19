// DB TEAM PROJECT #4 - 5팀(김유진, 이지원)</br>

<?php
            require_once 'dbconfig.php';
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
        $sql="select count(*) from HOSPITAL;";
        $result = mysqli_query($link, $sql);
        $data = mysqli_fetch_assoc($result);
        print "<p><h3>HOSPITAL table (Currently " . $data['count(*)'] . " rows in database)</h3></p>";
    ?>
    <table class = "table table-striped">
        <tr>
            <th>id</th>
            <th>name</th>
            <th>province</th>
            <th>city</th>
            <th>latitude</th>
            <th>longitude</th>
            <th>capacity</th>
            <th>current</th> <!- 현재 병원 ->
        </tr>

        <form action="hosptial_map.php" method="post">
        <?php
            $sql = "select * from HOSPITAL ORDER BY id asc;";
            $result = mysqli_query($link, $sql);
            while($row = mysqli_fetch_assoc($result)){
                foreach ($row as $key => $val){
                  if ($key == "longitude") // x좌표
                    $x = $val;
                  else if($key == "latitude") //y 좌표
                    $y = $val;
                  if($key == "current"){  // 테이블 생성
                    print "<td> <a href= \"http://localhost/hospital_map?x=<%=<?php $x ?>%>&y=<%=<?php $y ?>%>&h=<%=<?php $val ?>%>\">" . $val . "</a> </td>";
                  }else{
                      print "<td>" . $val . "</td>";
                    }
                }
                print "</tr>";
            }
        ?>
      </form>
    </table>
</body>
</html>
