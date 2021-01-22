# select    `questionid`,`challengeid` from `stuchallenged` where code is null order by id limit 10
 #select  * from `stuchallenged` where challengeid=1074766
# select * from `stuchallenged` where stuno='204215091001'
#insert into lx01(aaa)values('aaa')
#select count(*) from `stuchallenged` where code is null
# select * from `stuchallenged` where codelength>1000

#select  stuno,questionid,challtime from stuchallenged where questionid  not in (select questionid from stuchallenged where result='答案正确')#查询学生没有解决的问题
#查询学生的代码抄袭情况
# select a.challengeid aid,b.challengeid bid from stuchallenged a inner join stuchallenged b on a.questionid=b.questionid and a.code=b.code and a.challtime<>b.challtime
# select ta.questionid,ta.challengeid taid,tb.challengeid tbid,ta.stuno tastu,tb.stuno bstu, ta.challtime tatime,tb.challtime tbtime from stuchallenged ta inner join stuchallenged tb on ta.questionid=tb.questionid where ta.code=tb.code and ta.challtime>tb.challtime and ta.stuno<>tb.stuno
#查询学生做题的各种情况
# select distinct result from stuchallenged
#查询各种情况的数量
# select result,count(result) from stuchallenged group by result
# 查询B20软工1班男女生分布情况,男生14人，女生20人
# select gender,count(gender) from student where banjiid=1 group by gender 
# 查询学生做的题
# select stuno,gender,accept from student where banjiid=1 order by gender
#查询B20软工二班男生女生平均做题数
# select gender,avg(accept) from student where banjiid=1 group by gender
# 查询每道题学生做了多少次成功
select questionid,count(questionid) as c from stuchallenged where stuno in(select stuno from student where banjiid=1) group by questionid order by c desc
