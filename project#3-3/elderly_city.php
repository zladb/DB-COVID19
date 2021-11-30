// DB TEAM PROJECT #3 - 5팀(김유진, 이지원)</br>

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
        $sql="create or replace view elderly_city as 
        select p.province, p.city, p.infection_case, r.elderly_population_ratio 
        from REGION as r join PATIENTINFO as p on r.city=p.city 
        where r.elderly_population_ratio>'20'
        group by city, infection_case;";
        mysqli_query($link, $sql);

        $sql="select count(*) from elderly_city;";
        $result = mysqli_query($link, $sql);
        $data = mysqli_fetch_assoc($result);
        print "<p><h3>elderly_city view (Currently " . $data['count(*)'] . " rows in database)</h3></p>";
    ?>
    <table class = "table table-striped">
        <tr>
            <th>province</th>
            <th>city</th>
            <th>infection_case</th>
            <th>elderly_population_ratio</th>
        </tr>

        <?php
            $sql = "select * from elderly_city;";
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
