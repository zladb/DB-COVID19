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
      <option value="" selected disabled hidden>== 달을 선택하세요 ==</option>
      <option value="01"<?php if($_POST['month']=='01') echo " selected";?>>1월</option>
      <option value="02"<?php if($_POST['month']=='02') echo " selected";?>>2월</option>
      <option value="03"<?php if($_POST['month']=='03') echo " selected";?>>3월</option>
      <option value="04"<?php if($_POST['month']=='04') echo " selected";?>>4월</option>
      <option value="05"<?php if($_POST['month']=='05') echo " selected";?>>5월</option>
      <option value="06"<?php if($_POST['month']=='06') echo " selected";?>>6월</option>
    </select>

    <input type="submit" value="Submit"/>
  </form>


  <?php
    if(isset($_POST['month'])){  //isset이용
      //echo $_POST['month'];
      $month = $_POST['month'];
      $sql = "select infection_case from patientinfo where confirmed_date like '%-{$month}-%' group by infection_case;";
      $result = mysqli_query($link, $sql);
    }
  ?>

  <form>
      <select name = "infCase">
      <option value="" selected disabled hidden>== 케이스를 선택하세요 ==</option>
      <?php while( $row = mysqli_fetch_array($result))
      {
        $caseName[$i] = $row['infection_case']; $i = $i + 1;?>
        <option value="<?php echo $row['infection_case']; ?>"> <?php echo $row['infection_case']; ?></option>
      <?php } ?>
      </select>
    <input type="submit" value="Submit2"/>
  </form>


  <?php
    //echo $month;

    if(isset($_POST['infCase'])){  //isset이용
      //echo $_POST['month'];
      //$sql = "select infection_case from patientinfo where confirmed_date like '%-{$_POST['month']}-%' group by infection_case;";
      //$result = mysqli_query($link, $sql);'
      echo 'here!!!!!!!';
    }
  ?>

    <?php
      //echo '<h2>';
      //select 박스의 선택 내용 가져오기 하면 끝

      if(isset($_POST['infCase'])){  //isset이용
        $sql = "select age, count(*) from patientinfo Where infection_case = '{$_POST['infCase']}' and confirmed_date like '%-{$_POST['month']}-%' group by age;";
        echo $sql;
        $resultset = mysqli_query($link, $sql);
        $count = mysqli_num_rows($resultset);
        //echo "Cases table (Currently ' . $count . ') case in database which case is '. $_POST['infCase'] .' <br>";
    
      //echo '</h2>';

        echo 'what the fuck';
        echo '<table class="table table-striped">';
        echo '<tr>';
        echo '<th>Age</th>';
        echo '<th>Count</th>';
        echo '</tr>';
          while ($row = mysqli_fetch_assoc($resultset)) 
          {
            print "<tr>";
            foreach ($row as $key => $val) 
            {
                print "<td>" . $val . "</td>";
            }
            print "</tr>";
          }
        echo '</table>';
      }
      else {
        echo 'what the fuck';
        $val = isset($_POST['infCase']);
        echo $val;
      }
    ?>
</body>
</html>
