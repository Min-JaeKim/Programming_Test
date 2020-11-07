-- 코드를 입력하세요
SELECT ins.animal_id, ins.name
from animal_ins ins, animal_outs outs
where ins.animal_id = outs.animal_id and outs.datetime < ins.datetime
order by ins.datetime;

-- 코드를 입력하세요
SELECT outs.animal_id, outs.name
from animal_ins ins left join animal_outs outs
on outs.animal_id = ins.animal_id
where outs.datetime < ins.datetime 
order by ins.datetime


/*
join을 사용할 때는 on이 꼭 있어야 하고
join을 사용하지 않을 때에는 on이 있으면 오류가 난다.
*/