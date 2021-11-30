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
        <h1> Province 선택하세요 <br> </h1>
        <!-- 여기 드롭다운 박스-->

          <?php
            $i = 0;
            //group by state
            $sql = "select * from weather group by province;";
            $result = mysqli_query($link, $sql);
            ?>
            <form method="post">
              <select name="selectProv">
                <?php while( $row = mysqli_fetch_array($result) ){
                        $provName[$i] = $row['province']; $i = $i + 1;?>
                        <option value="<?php echo $row['province'];?>" <?php if(isset($_POST['selectProv'])) echo ($_POST['selectProv']==$row['province'])? ' selected':'';?>> <?php echo $row['province']; ?></option>
                      <?php } ?>
                    </select>
                    <input type="submit" value="Submit"/>
                  </form>
        <h2>
        <?php
        //select 박스의 선택 내용 가져오기 하면 끝
          if(isset($_POST['selectProv']))  //isset이용
            for ($s = 0;$s < $i ;$s = $s + 1){
              if ($provName[$s] === $_POST['selectProv']){
                $sql = "select * from weather Where province = '" . $provName[$s].  "' order by wdate;";
                break;
              }
            }
          else{
            $provName[$i] = "All";  $s = $i;
            $sql = "select * from weather order by region_code;";
          }
          $resultset = mysqli_query($link, $sql);
          $count = mysqli_num_rows($resultset);
          echo 'Weather table (Currently ' . $count . ') province in database which province is '. $provName[$s] . ' <br>';
        ?>
      </h2>
      <table class="table table-striped">
        <tr>
            <th>region code</th>
            <th>province</th>
            <th>date</th>
            <th>avg temperature</th>
            <th>min temperature</th>
            <th>max temperature</th>
        </tr>
        <?php while ($row = mysqli_fetch_assoc($resultset)) {
            print "<tr>";
            foreach ($row as $key => $val) {
                print "<td>" . $val . "</td>";
            }
            print "</tr>";
        }
        ?>
    </table>
</body>
</html>
