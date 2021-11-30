// DB_TEAM PROJECT #3-3, 5팀 (김유진, 이지원)
// elderly_city.php의 Readme.md

노령인구의 비율이 20퍼센트 이상인 도시의 case를 나타내었다.
사용한 테이블 -> region, patientinfo

create or replace view elderly_city as 
        select p.province, p.city, p.infection_case, r.elderly_population_ratio 
        from REGION as r join PATIENTINFO as p on r.city=p.city 
        where r.elderly_population_ratio>'20'
        group by city, infection_case;
        
 
region.elderly_population_ratio > 20인 데이터를 
region과 patient의 city를 기준으로 join하였으며,
(city, infection_case)를 그룹으로 묶었다.
