Create table runs(
id serial primary key
,race_id integer
,horse_no integer
,horse_id integer
,result integer
,won integer
,lengths_behind numeric(18,2)
,horse_age numeric(18,2)
,horse_country varchar(100)
,horse_type varchar(100)
,horse_rating numeric(18,2)
,horse_gear varchar(100)
,declared_weight integer
,actual_weight integer
,draw integer
,position_sec1 integer
,position_sec2 integer
,position_sec3 integer
,position_sec4 integer
,position_sec5 integer
,position_sec6 integer
,behind_sec1 numeric(18,2)
,behind_sec2 numeric(18,2)
,behind_sec3 numeric(18,2)
,behind_sec4 numeric(18,2)
,behind_sec5 numeric(18,2)
,behind_sec6 numeric(18,2)
,time1 numeric(18,2)
,time2 numeric(18,2)
,time3 numeric(18,2)
,time4 numeric(18,2)
,time5 numeric(18,2)
,time6 numeric(18,2)
,finish_time numeric(18,2)
,win_odds numeric(18,2)
,place_odds numeric(18,2)
,trainer_id integer
,jockey_id integer);

create table races(
id serial primary key
,race_id integer
,date date
,venue varchar(100)
,race_no integer
,config varchar(100)
,surface integer
,distance varchar(100)
,going varchar(100)
,horse_ratings varchar(100)
,prize integer
,race_class integer
,sec_time1 numeric(18,2)
,sec_time2 numeric(18,2)
,sec_time3 numeric(18,2)
,sec_time4 numeric(18,2)
,sec_time5 numeric(18,2)
,sec_time6 numeric(18,2)
,sec_time7 numeric(18,2)
,time1 numeric(18,2)
,time2 numeric(18,2)
,time3 numeric(18,2)
,time4 numeric(18,2)
,time5 numeric(18,2)
,time6 numeric(18,2)
,time7 numeric(18,2)
,place_combination1 integer
,place_combination2 integer
,place_combination3 integer
,place_combination4 integer
,place_dividend1 numeric(18,2)
,place_dividend2 numeric(18,2)
,place_dividend3 numeric(18,2)
,place_dividend4 numeric(18,2)
,win_combination1 integer
,win_dividend1 numeric(18,2)
,win_combination2 integer
,win_dividend2 numeric(18,2)
);


create table raceruns (
id serial primary key
,race_id integer
,won integer
--,date date
--,venue varchar(100)
,race_no integer
--,config varchar(100)
,surface integer
,distance varchar(100)
--,going varchar(100)
--,horse_ratings varchar(100)
--,prize integer
,race_class integer
,sec_time1 numeric(18,2)
,sec_time2 numeric(18,2)
,sec_time3 numeric(18,2)
,sec_time4 numeric(18,2)
,rc_time1 numeric(18,2)
,rc_time2 numeric(18,2)
,rc_time3 numeric(18,2)
,rc_time4 numeric(18,2)
,place_combination1 integer
,place_combination2 integer
,place_combination3 integer
,place_dividend1 numeric(18,2)
,place_dividend2 numeric(18,2)
,place_dividend3 numeric(18,2)
,win_combination1 integer
,win_dividend1 numeric(18,2)
,horse_no integer
,horse_id integer
,result integer
,lengths_behind numeric(18,2)
,horse_age numeric(18,2)
--,horse_country varchar(100)
,horse_rating numeric(18,2)
,declared_weight integer
,actual_weight integer
,draw integer
,position_sec1 integer
,position_sec2 integer
,position_sec3 integer
,position_sec4 integer
,behind_sec1 numeric(18,2)
,behind_sec2 numeric(18,2)
,behind_sec3 numeric(18,2)
,behind_sec4 numeric(18,2)
,rn_time1 numeric(18,2)
,rn_time2 numeric(18,2)
,rn_time3 numeric(18,2)
,rn_time4 numeric(18,2)
,finish_time numeric(18,2)
,win_odds numeric(18,2)
,place_odds numeric(18,2)
,trainer_id integer
,jockey_id integer);


INSERT INTO raceruns (race_id, date, venue, race_no, config,surface,distance,going,horse_ratings
                     ,prize,race_class,sec_time1,sec_time2,sec_time3,sec_time4
                     ,rc_time1,rc_time2,rc_time3,rc_time4
                     ,place_combination1,place_combination2,place_combination3,place_dividend1,place_dividend2,place_dividend3
                     ,win_combination1,win_dividend1
                     ,horse_no,horse_id,result,won,lengths_behind,horse_age,horse_country,horse_rating
                     ,declared_weight,actual_weight,draw
                     ,position_sec1,position_sec2,position_sec3,position_sec4
                     ,behind_sec1,behind_sec2,behind_sec3,behind_sec4
                     ,rn_time1,rn_time2,rn_time3,rn_time4
                     ,finish_time,win_odds,place_odds,trainer_id,jockey_id)
                     
SELECT
 rc.race_id
,rn.won
--,rc.date
--,rc.venue
,rc.race_no
--,rc.config
,rc.surface
,rc.distance
--,rc.going
--,rc.horse_ratings
--,rc.prize
,rc.race_class
,rc.sec_time1
,rc.sec_time2
,rc.sec_time3
,rc.sec_time4
,rc.time1 ldr_time1
,rc.time2 ldr_time2
,rc.time3 ldr_time3
,rc.time4 ldr_time4
,rc.place_combination1
,rc.place_combination2
,rc.place_combination3
,rc.place_dividend1
,rc.place_dividend2
,rc.place_dividend3
,rc.win_combination1
,rc.win_dividend1
,rn.horse_no
,rn.horse_id
,rn.result
,rn.lengths_behind
,rn.horse_age
--,rn.horse_country
,rn.horse_rating
,rn.declared_weight
,rn.actual_weight
,rn.draw
,rn.position_sec1
,rn.position_sec2
,rn.position_sec3
,rn.position_sec4
,rn.behind_sec1
,rn.behind_sec2
,rn.behind_sec3
,rn.behind_sec4
,rn.time1
,rn.time2
,rn.time3
,rn.time4
,rn.finish_time
,rn.win_odds
,rn.place_odds
,rn.trainer_id
,rn.jockey_id

INTO raceruns
FROM races rc
JOIN runs rn ON rc.race_id = rn.race_id


                     


SELECT
 rc.race_id
,rn.won
--,rc.date
--,rc.venue
--,rc.race_no
--,rc.config
--,rc.surface
,rc.distance
--,rc.going
--,rc.horse_ratings
--,rc.prize
,rc.race_class
,rc.sec_time1
,rc.sec_time2
,rc.sec_time3
,rc.sec_time4
,rc.time1 ldr_time1
,rc.time2 ldr_time2
,rc.time3 ldr_time3
,rc.time4 ldr_time4
,rc.place_combination1
,rc.place_combination2
,rc.place_combination3
,rc.place_dividend1
,rc.place_dividend2
,rc.place_dividend3
,rc.win_combination1
,rc.win_dividend1
,rn.horse_no
,rn.horse_id
--,rn.result
--,rn.lengths_behind
,rn.horse_age
--,rn.horse_country
,rn.horse_rating
,rn.declared_weight
,rn.actual_weight
,rn.draw
,rn.position_sec1
,rn.position_sec2
,rn.position_sec3
,rn.position_sec4
--,rn.behind_sec1
--,rn.behind_sec2
--,rn.behind_sec3
--,rn.behind_sec4
,rn.time1
,rn.time2
,rn.time3
,rn.time4
,rn.finish_time
,rn.win_odds
,rn.place_odds
,rn.trainer_id
,rn.jockey_id

INTO training_data
FROM races rc
JOIN runs rn ON rc.race_id = rn.race_id





SELECT
 rc.race_id
,rn.won
--,rc.date
--,rc.venue
--,rc.race_no
--,rc.config
--,rc.surface
,rc.distance
--,rc.going
--,rc.horse_ratings
--,rc.prize
,rc.race_class
,rc.sec_time1
,rc.sec_time2
,rc.sec_time3
,rc.sec_time4
,rc.time1 ldr_time1
,rc.time2 ldr_time2
,rc.time3 ldr_time3
,rc.time4 ldr_time4
--,rc.place_combination1
--,rc.place_combination2
--,rc.place_combination3
--,rc.place_dividend1
--,rc.place_dividend2
--,rc.place_dividend3
--,rc.win_combination1
--,rc.win_dividend1
--,rn.horse_no
--,rn.horse_id
,rn.result
,rn.lengths_behind
--,rn.horse_age
--,rn.horse_country
--,rn.horse_rating
--,rn.declared_weight
--,rn.actual_weight
--,rn.draw
--,rn.position_sec1
--,rn.position_sec2
--,rn.position_sec3
--,rn.position_sec4
,rn.behind_sec1
,rn.behind_sec2
,rn.behind_sec3
,rn.behind_sec4
,rn.time1
,rn.time2
,rn.time3
,rn.time4
--,rn.finish_time
,rn.win_odds
,rn.place_odds
--,rn.trainer_id
--,rn.jockey_id


INTO best_ranked_data
FROM races rc
JOIN runs rn ON rc.race_id = rn.race_id