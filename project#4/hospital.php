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

    <form method="post">
        <br><h2>병원의 id(1~41)를 입력하세요</h2>
        <input type="text" name="h_id">
        <input type="submit" value="전송">
    </form> 

    <?php
        $sql="select count(*) from PATIENTINFO;";
        $result = mysqli_query($link, $sql);
        $data = mysqli_fetch_assoc($result);
        print "<p><h3>PATIENTINFO + HOSPITAL_ID table (Currently " . $data['count(*)'] . " rows in database)</h3></p>";
    ?>

    <table class = "table table-striped">
        <tr>
            <th>patient_id</th>
            <th>sex</th>
            <th>age</th>
            <th>country</th>
            <th>province</th>
            <th>city</th>
            <th>infection_case</th>
            <th>infected_by</th>
            <th>contact_number</th>
            <th>symptom_onset_date</th>
            <th>confirmed_date</th>
            <th>released_date</th>
            <th>deceased_date</th>
            <th>state</th>
            <th>hospital_id</th>
        </tr>

    <?php
        if(isset($_POST['h_id']))
        {
            $sql = "select * from PATIENTINFO where hospital_id={$_POST['h_id']} ORDER BY patient_id asc;";
            $result = mysqli_query($link, $sql);
        }
        else
        {
            $sql = "select * from PATIENTINFO ORDER BY patient_id asc;";
            $result = mysqli_query($link, $sql);
        }
    ?>

      <form action="hospital_map.php" method="post">
        <?php
            while($row = mysqli_fetch_assoc($result)){
                foreach ($row as $key => $val)
                {
                    if($key == "hospital_id")
                    {  // 테이블 생성
                        $sql = "select name, latitude, longitude from HOSPITAL WHERE id = {$val}";
                        $result2 = mysqli_query($link, $sql);
                        $point = mysqli_fetch_assoc($result2);
                        $x = $point["longitude"];   // 경도
                        $y = $point["latitude"];    // 위도
                        $name = $point["name"];
                        print "<td> <a href= \"http://localhost/hospital_map?x=$x&y=$y&name=$name\">" . $val . "</a> </td>";
                    }
                    else
                    print "<td>" . $val . "</td>";
                }
                print "</tr>";
            }
        ?>

      </form>
    </table>
</body>
</html>
