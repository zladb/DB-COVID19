<!DOCTYPE html>
<html lang="ko">
<head>
<title>구글지도사용하기</title>
<meta charset = 'utf-8'>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script type="text/javascript" src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
<script type="text/javascript" src="http://maps.google.com/maps/api/js?key=AIzaSyAEP5HR3NjkLK66-7NbtpKiik3uPecNh1g" >//키를 발급받아 사용하세요</script>
<style>
#map_ma {width:100%; height:400px; clear:both; border:solid 1px red;}
</style>

</head>
<body>
<div id="map_ma"></div>
<script type="text/javascript">

// 파라미터를 얻는 함수
function getParam(sname) 
{
    var params = location.search.substr(location.search.indexOf("?") + 1);
    var sval = "";
    params = params.split("&");
    for (var i = 0; i < params.length; i++) {
        temp = params[i].split("=");
        if ([temp[0]] == sname) { sval = temp[1]; }
    }
    return sval;
}   

// alert(getParam("x"))
// alert(getParam("y"))
// alert(getParam("name"))

String.prototype.replaceAll = function(org, dest) {
    return this.split(org).join(dest);
}

var hospital_name=getParam("name");
hospital_name = hospital_name.replaceAll("%20", " ");
//alert(hospital_name)

$(document).ready(function() {
        var myLatlng = new google.maps.LatLng(getParam("y"), getParam("x")); // 위치값 위도 경도
   var Y_point         =  getParam("y");      // Y 좌표
   var X_point         =  getParam("x");      // X 좌표
   var zoomLevel        = 18;            // 지도의 확대 레벨 : 숫자가 클수록 확대정도가 큼
   var markerTitle      = hospital_name;      // 현재 위치 마커에 마우스를 오버을때 나타나는 정보
   var markerMaxWidth   = 300;            // 마커를 클릭했을때 나타나는 말풍선의 최대 크기

// 말풍선 내용
   var contentString   = '<div>' +
   '<h2>' + hospital_name + '</h2>'+
   //'<p>안녕하세요. 구글지도입니다.</p>' +
   
   '</div>';
   var myLatlng = new google.maps.LatLng(Y_point, X_point);
   var mapOptions = {
                  zoom: zoomLevel,
                  center: myLatlng,
                  mapTypeId: google.maps.MapTypeId.ROADMAP
               }
   var map = new google.maps.Map(document.getElementById('map_ma'), mapOptions);
   var marker = new google.maps.Marker({
                                 position: myLatlng,
                                 map: map,
                                 title: markerTitle
   });
   var infowindow = new google.maps.InfoWindow(
                                    {
                                       content: contentString,
                                       maxWizzzdth: markerMaxWidth
                                    }
         );
   google.maps.event.addListener(marker, 'click', function() {
      infowindow.open(map, marker);
   });
});
      </script>
</body>
</html>
