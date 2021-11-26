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
        <h1> Case 선택하세요 <br> </h1>
        <!-- 여기 드롭다운 박스-->

          <?php
            $i = 0;
            //group by state
            $sql = "select * from cases group by infection_case;";
            $result = mysqli_query($link, $sql);
            ?>
            <form method="post">
              <select name="infCase">
                <?php while( $row = mysqli_fetch_array($result) ){
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
            <th>case_id</th>
            <th>province</th>
            <th>city</th>
            <th>infection group</th>
            <th>infection case</th>
            <th>confirmed</th>
            <th>latitude</th>
            <th>longitude</th>
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
