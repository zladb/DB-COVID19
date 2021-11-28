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
  <!-- 여기 드롭다운 박스-->
  <h1> month와 infection_case를 선택하세요! <br> </h1>
  <form method = "post">
    
    <select name = "month">
      <option value="1월">1월</option>
      <option value="2월">2월</option>
      <option value="3월">3월</option>
      <option value="4월">4월</option>
      <option value="5월">5월</option>
      <option value="6월">6월</option>
    </select>
    
    <?php
      $i = 0;
      //group by state
      $sql = "select * from cases group by infection_case;";
      $result = mysqli_query($link, $sql);
    ?>
    <select name = "infCase">
    <?php while( $row = mysqli_fetch_array($result))
    {
      $caseName[$i] = $row['infection_case']; $i = $i + 1;?>
      <option value="<?php echo $row['infection_case']; ?>"> <?php echo $row['infection_case']; ?></option>
    <?php } ?>
    </select>
    <input type="submit" value="Submit"/>
  </form>

        <h2>
        <?php
        //select 박스의 선택 내용 가져오기 하면 끝
          if(isset($_POST['infCase']))  //isset이용
            for ($s = 0; ;$s = $s + 1){
              if ($caseName[$s] === $_POST['infCase']){
                $sql = "select * from cases Where infection_case = '" . $caseName[$s].  "' order by infection_case ;";
                break;
              }
            }
          else{
            $caseName[$i] = "All";  $s = $i;
            $sql = "select * from cases order by infection_case ;";
          }
          $resultset = mysqli_query($link, $sql);
          $count = mysqli_num_rows($resultset);
          echo 'Cases table (Currently ' . $count . ') case in database which case is '. $caseName[$s] . ' <br>';
        ?>
      </h2>
      <table class="table table-striped">
        <tr>
            <th>Age</th>
            <th>Count</th>
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
