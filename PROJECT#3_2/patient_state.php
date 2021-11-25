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
        <h1> state를 선택하세요 <br> </h1>
        <!-- 여기 드롭다운 박스-->

          <?php
            $i = 0;
            //group by state
            $sql = "select * from PatientInfo group by state;";
            $result = mysqli_query($link, $sql);
            ?>
            <form method="post">
              <select name="stateVal">
                <?php while( $row = mysqli_fetch_array($result) ){
                        $state[$i] = $row['state']; $i = $i + 1;?>
                        <option value="<?php echo $row['state']; ?>"> <?php echo $row['state']; ?></option>
                      <?php } ?>
                    </select>
                    <input type="submit" value="Submit"/>
                  </form>
        <h2>
        <?php
        //select 박스의 선택 내용 가져오기 하면 끝
          if(isset($_POST['stateVal']))  //isset이용
            for ($s = 0; ;$s = $s + 1){
              if ($state[$s] === $_POST['stateVal']){
                $sql = "select * from PatientInfo Where state = '" . $state[$s].  "' order by patient_id ;";
                break;
              }
            }
          else{
            $sql = "select * from PatientInfo order by patient_id ;";
          }
          $resultset = mysqli_query($link, $sql);
          $count = mysqli_num_rows($resultset);
          echo 'PatientInfo table (Currently ' . $count . ') patientin database which state is '. $state[$s] . ' <br>';
        ?>
      </h2>
      <table class="table table-striped">
        <tr>
            <th>Patient ID</th>
            <th>Sex</th>
            <th>Age</th>
            <th>Country</th>
            <th>Rating</th>
            <th>Infection case</th>
            <th>Infected by</th>
            <th>Contact number</th>
            <th>Symptom onset date</th>
            <th>Contirmed date</th>
            <th>Released date</th>
            <th>Deceased date</th>
            <th>state</th>
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
