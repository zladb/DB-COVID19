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
  <!-- 여기 드롭다운 박스 1)infection case 2)province 3)나이대랑 같이 보이기-->
  <h1> month와 infection_case를 선택하세요! <br> </h1>

  <?php
    $i = 0;
    //group by state
    $sql = "select * from weather group by province;";
    $result = mysqli_query($link, $sql);
    ?>
    <form method="post">
      <select name="selectProv">
          <option value="" selected disabled hidden>==지역을 선택하세요 ==</option>
        <?php while( $row = mysqli_fetch_array($result) ){
                $provName[$i] = $row['province']; $i = $i + 1;?>
                <option value="<?php echo $row['province']; ?>"> <?php echo $row['province']; ?></option>
              <?php } ?>
            </select>
            <input type="submit" value="Submit"/>
          </form>
  <?php
    $i = 0;
    //group by infection_case
    if(isset($_POST['selectProv']))
      $sql = "select * from cases where province = '".$_POST['selectProv']. "' group by infection_case;";
    else
      $sql = "select * from patientinfo group by infection_case;";
    $result = mysqli_query($link, $sql);  ?>
    <form method="post">
      <select name="infCase">
          <option value="" selected disabled hidden>== 케이스를 선택하세요 ==</option>
        <?php while( $row = mysqli_fetch_array($result) ){
                $caseName[$i] = $row['infection_case']; $i = $i + 1;?>
                <option value="<?php echo $row['infection_case']; ?>"> <?php echo $row['infection_case']; ?></option>
              <?php } ?>
            </select>
            <input type="submit" value="Submit"/>
          </form>

          -

    <?php
    if(isset($_POST['selectProv'])){  //지역만 선택 ?>
      <h2> 지역의 나이대별 <br> </h2>
      <?php
      echo 'province_age table patients in database which porvince is '. $_POST['selectProv'] . ' <br>';
      $sql = "select age, count(*) from patientinfo Where province = '". $_POST['selectProv']."' group by age;";
      $resultset = mysqli_query($link, $sql);
        ?>
        <table class="table table-striped">
          <tr>
            <th>age</th>
            <th>count</th>
          </tr>
        <?php while ($row = mysqli_fetch_assoc($resultset)) {
            print "<tr>";
            foreach ($row as $key => $val) {
                print "<td>" . $val . "</td>";
            }
            print "</tr>";
        }?>
        </table>
      <?php }
      else if(isset($_POST['infCase'])){  //케이스만 선택 ?>
        <h2> 케이스의 나이대별 <br> </h2>
        <?php
        echo 'case_age table patients in database which case is '. $_POST['infCase'] . ' <br>';
        $sql = "select age, count(*) from patientinfo Where infection_case = '". $_POST['infCase']."' group by age;";
        //echo $sql;
        //echo $sql;
          $resultset = mysqli_query($link, $sql);
          ?>
          <table class="table table-striped">
            <tr>
              <th>age</th>
              <th>count</th>
            </tr>
          <?php while ($row = mysqli_fetch_assoc($resultset)) {
              print "<tr>";
              foreach ($row as $key => $val) {
                  print "<td>" . $val . "</td>";
              }
              print "</tr>";
          }?>
          </table>
        <?php }
        else if(isset($_POST['infCase']) && isset($_POST['selectProv'])){  //지역, 케이스 모두 선택 ?>
          <h2> 해당 지역에 속한 케이스의 나이대별 <br> </h2>
          <?php
          echo 'province_case_age table patients in database which porvince is '. $_POST['selectProv'] . ' <br>';
          $sql = "select age, count(*) from patientinfo Where province = '". $_POST['selectProv']."' && Where infection_case = '". $_POST['infCase']."' group by age;";
          //echo $sql;
          $resultset = mysqli_query($link, $sql);
          ?>
          <table class="table table-striped">
            <tr>
              <th>age</th>
              <th>count</th>
            </tr>
          <?php while ($row = mysqli_fetch_assoc($resultset)) {
              print "<tr>";
              foreach ($row as $key => $val) {
                  print "<td>" . $val . "</td>";
              }
              print "</tr>";
          }?>
          </table>
        <?php }
        else {  //아무것도 선택하지 않았을때 ?>
              <h2> 나이대별 모든 테이블 <br> </h2>
              <?php
              echo 'All tables of patient info <br>';
              $sql = "select age, count(*) from patientinfo group by age;";
              //echo $sql;
              $resultset = mysqli_query($link, $sql);
              ?>
              <table class="table table-striped">
                <tr>
                  <th>age</th>
                  <th>count</th>
                </tr>
              <?php while ($row = mysqli_fetch_assoc($resultset)) {
                  print "<tr>";
                  foreach ($row as $key => $val) {
                      print "<td>" . $val . "</td>";
                  }
                  print "</tr>";
              }?>
              </table>
            <?php } ?>




</body>
</html>
