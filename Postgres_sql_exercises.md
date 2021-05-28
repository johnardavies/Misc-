##Solutions to exercies from https://pgexercises.com/##


***There are three tables a members table, a bookings table and a facilities table***

***How can you produce a list of the start times for bookings by members named 'David Farrell'?***

```
select starttime from cd.members

join cd.bookings

on cd.bookings.memid=cd.members.memid

WHERE CONCAT(firstname, surname) LIKE 'DavidFarrell';
```

***How can you produce a list of the start times for bookings for tennis courts, for the date '2012-09-21'? Return a list of start time and facility name pairings, ordered
by the time***

```
select  starttime, name from cd.members

join cd.bookings

on cd.bookings.memid=cd.members.memid 

join cd.facilities

on cd.bookings.facid=cd.facilities.facid

WHERE cd.facilities.name LIKE 'Tennis Court%' AND (CAST(starttime AS date)='2012-09-21')
 
ORDER BY starttime ASC;
```

***How can you output a list of all members who have recommended another member? Ensure that there are no duplicates in the list, 
and that results are ordered by (surname, firstname).***


```
SELECT DISTINCT mem2.firstname as firstname, mem2.surname as surname
FROM cd.members 
inner join cd.members as mem2 
on cd.members.recommendedby=mem2.memid 
WHERE cd.members.recommendedby >0 
ORDER BY mem2.surname ASC , mem2.firstname  DESC;
```

***How can you output a list of all members, including the individual who recommended them (if any)?***
***Ensure that results are ordered by (surname, firstname).***

```
SELECT cd.members.firstname as memfname, cd.members.surname as memsname ,  mem2.firstname as recfname, mem2.surname as recsname 
FROM cd.members. 
left outer join cd.members as mem2 
on cd.members.recommendedby=mem2.memid 
ORDER BY memsname, memfname ASC;
``` 

***How can you produce a list of all members who have used a tennis court? Include in your output the name of the court, and the name of the member formatted as a single column. Ensure no duplicate data, and order by the member name followed by the facility name.***

```
SELECT DISTINCT CONCAT(firstname, ' ', surname) as member, 
(SELECT DISTINCT CONCAT(firstname, ' ', surname) as recommender FROM cd.members as mem2
	 where cd.members.recommendedby=mem2.memid
	   ) 
FROM cd.members
ORDER BY member , recommender;    join
    cd.bookings bk
    on bk.memid=cd.members.memid
    join
    cd.facilities fac
    on bk.facid=fac.facid
    WHERE fac.name LIKE 'Tennis Court%' 
    ORDER BY member , facility ASC ;
 ```
*** How can you produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than 30? ***
Remember that guests have different costs to members the listed costs are per half-hour 'slot', and the guest user is always ID 0. Include in your output the name of the facility, the name of the member formatted as a single column, and the cost. Order by descending cost, and do not use any subqueries. ***

```

SELECT CONCAT (cd.members.firstname,' ',cd.members.surname) as member, fac.name, 
CASE bk.memid
     WHEN 0 THEN fac.guestcost*bk.slots
     ELSE fac.membercost*bk.slots
	 END AS cost
	 
FROM cd.members
	join cd.bookings bk
	  on cd.members.memid=bk.memid
	join cd.facilities fac
	  on bk.facid=fac.facid
  
WHERE (CAST(starttime AS date)='2012-09-14') and ((bk.memid=0 and fac.guestcost*bk.slots>30) or (bk.memid>0 and fac.membercost*bk.slots>30))
ORDER BY cost DESC;
```
***How can you output a list of all members, including the individual who recommended them (if any), without using any joins? Ensure that there are no duplicates in the list, and that each firstname + surname pairing is formatted as a column and ordered.***

```
SELECT DISTINCT CONCAT(firstname, ' ', surname) as member, recommendedby ,
CASE 
     WHEN recommendedby IS NULL THEN ' '
     WHEN recommendedby IS NOT NULL THEN (
	 SELECT  CONCAT(firstname, ' ', surname) FROM cd.members
	 where cd.members.recommendedby=cd.members.memid
	   )
END as recommender
FROM cd.members
ORDER BY member;
```

***How can you output a list of all members, including the individual who recommended them (if any), without using any joins? Ensure that there are no duplicates in the list, and that each firstname + surname pairing is formatted as a column and ordered.***

```
SELECT DISTINCT CONCAT(firstname, ' ', surname) as member, recommendedby ,
CASE 
     WHEN recommendedby IS NULL THEN ' '
     WHEN recommendedby IS NOT NULL THEN (
	 SELECT  CONCAT(firstname, ' ', surname) FROM cd.members
	 where cd.members.recommendedby=cd.members.memid
	   )
END as recommender
FROM cd.members
ORDER BY member;

```

***The Produce a list of costly bookings exercise contained some messy logic: we had to calculate the booking cost in both the WHERE clause and the CASE statement. Try to simplify this calculation using subqueries. For reference, the question was:
How can you produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than $30? Remember that guests have different costs to members (the listed costs are per half-hour 'slot'), and the guest user is always ID 0. Include in your output the name of the facility, the name of the member formatted as a single column, and the cost. Order by descending cost.
***
```
SELECT  member, name,cost
FROM (
SELECT CONCAT (cd.members.firstname,' ',cd.members.surname) as member, fac.name, 
CASE bk.memid
WHEN 0 THEN fac.guestcost*bk.slots
ELSE fac.membercost*bk.slots
end as cost

FROM cd.members
	join cd.bookings bk
	  on cd.members.memid=bk.memid
	join cd.facilities fac
	  on bk.facid=fac.facid
  
WHERE (CAST(starttime AS date)='2012-09-14')
ORDER BY cost DESC ) as tam
WHERE cost >30;
```

