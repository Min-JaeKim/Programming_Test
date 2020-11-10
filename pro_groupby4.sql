-- 코드를 입력하세요
set @hour := -1;
SELECT (@hour := @hour + 1) as hour,
(select count(*) from animal_outs where hour(datetime) = @hour) as count
from animal_outs
where @hour < 23

/*
1. set꼭 쓰기
2. set에 꼭 ; 쓰기
3. := 와 = 구분하기
4. 괄호 꼭 치기
*/ 
