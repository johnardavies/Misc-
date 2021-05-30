## Solutions to exercies from https://pgexercises.com/ ##


***There are three tables a members table (cd.members), a bookings table (cd.bookings) and a facilities table (cd.facilities)***

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
***How can you produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than 30? Remember that guests have different costs to members the listed costs are per half-hour 'slot', and the guest user is always ID 0 Include in your output the name of the facility, the name of the member formatted as a single column, and the cost. Order by descending cost, and do not use any subqueries.***

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
How can you produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than $30? Remember that guests have different costs to members (the listed costs are per half-hour 'slot'), and the guest user is always ID 0. Include in your output the name of the facility, the name of the member formatted as a single column, and the cost. Order by descending cost.***

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
***Produce a list of facilities along with their total revenue. The output table should consist of facility name and revenue sorted by revenue. Remember that there is a different cost for guests and members***
```
SELECT  name, sum(cost) as revenue
FROM (
SELECT fac.name, 
CASE bk.memid
WHEN 0 THEN fac.guestcost*bk.slots
ELSE fac.membercost*bk.slots
end as cost

FROM cd.members
	join cd.bookings bk
	  on cd.members.memid=bk.memid
	join cd.facilities fac
	  on bk.facid=fac.facid
 

) as tam

GROUP BY tam.name 
ORDER BY revenue ASC
```
***Produce a list of facilities with a total revenue less than 1000. Produce an output table consisting of facility name and revenue sorted by revenue. Remember that there's a different cost for guests and members.***
```
SELECT  name, revenue
FROM (
SELECT  name, sum(cost) as revenue
FROM (
SELECT fac.name, 
CASE bk.memid
WHEN 0 THEN fac.guestcost*bk.slots
ELSE fac.membercost*bk.slots
end as cost

FROM cd.members
	join cd.bookings bk
	  on cd.members.memid=bk.memid
	join cd.facilities fac
	  on bk.facid=fac.facid
 

) as tam

GROUP BY tam.name) as tam2
where revenue<1000

ORDER BY revenue ASC;
```
***Produce a list of the total number of hours booked per facility, remembering that a slot lasts half an hour. The output table should consist of the facility id, name, and hours booked, sorted by facility id. Try formatting the hours to two decimal places.***
```
SELECT  bk.facid, fac.name, ROUND(sum(slots*0.5),2) as "Total Hours"

FROM cd.bookings as bk
   join cd.facilities fac
	  on bk.facid=fac.facid
GROUP BY  bk.facid, fac.name 
ORDER BY bk.facid;
```
***Produce a list of each member name, id, and their first booking after September 1st 2012. Order by member ID.***

```
SELECT surname, firstname, mem.memid, MIN(book.starttime)
 FROM cd.bookings as book
    join cd.members as mem
    on mem.memid=book.memid 

  WHERE CAST(starttime AS date)>'2012-08-31'
  GROUP BY mem.memid, mem.surname, mem.firstname
  ORDER BY mem.memid
```
***Produce a list of member names, with each row containing the total member count. Order by join date, and include guest members.***
over is used as you can have aggregated and non aggregated values in same table, unlike group
```
SELECT COUNT(*) over(), firstname, surname  
 FROM cd.members
ORDER BY joindate
```
***Produce a monotonically increasing numbered list of members (including guests), ordered by their date of joining. Remember that member IDs are not guaranteed to be sequential.***
```
SELECT  RANK() OVER(ORDER BY joindate ASC) AS row_number, firstname, surname
FROM cd.members;
```
***Output the facility id that has the highest number of slots booked. Ensure that in the event of a tie, all tieing results get output.***
```
SELECT facid, total FROM (
	SELECT facid, sum(slots) total, rank() OVER (ORDER BY SUM(slots) desc) rank
        	FROM cd.bookings
		GROUP BY facid
	) as ranked
	WHERE rank = 1 
```

***Produce a list of members (including guests), along with the number of hours they've booked in facilities, rounded to the nearest ten hours. Rank them by this rounded figure, producing output of first name, surname, rounded hours, rank. Sort by rank, surname, and first name.***
```
SELECT firstname, surname, ROUND(SUM(slots*0.5),-1) as hours, RANK() OVER(ORDER BY ROUND(SUM(slots*0.5),-1) DESC) 
FROM cd.bookings book
  join cd.members as mem
      on mem.memid=book.memid
GROUP BY mem.memid
ORDER BY rank, surname, firstname;
```
***Produce a list of the top three revenue generating facilities (including ties). Output facility name and rank, sorted by rank and facility name.***
```
SELECT name, RANK() OVER(ORDER BY revenue DESC) rank
  FROM (
  SELECT  name, sum(cost) as revenue
  FROM (
SELECT fac.name, 
CASE bk.memid
WHEN 0 THEN fac.guestcost*bk.slots
ELSE fac.membercost*bk.slots
end as cost

FROM cd.members
	join cd.bookings bk
	  on cd.members.memid=bk.memid
	join cd.facilities fac
	  on bk.facid=fac.facid
 

  ) as tam

GROUP BY tam.name) as tam2
limit 3;
```
***Classify facilities into equally sized groups of high, average, and low based on their revenue. Order by classification and facility name.***
```
SELECT name,
/* creates the factor revenue variable */
CASE class
WHEN 3 THEN 'high'
WHEN 2 THEN 'average'
ELSE 'low'
end as revenue

FROM (
 
/* Selects the name and the tertile variab;e */
SELECT  name, NTILE(3) OVER(ORDER BY sum(cost)) as  class
  FROM (
SELECT fac.name, 
/* Creates the revenue variable */
CASE bk.memid
WHEN 0 THEN fac.guestcost*bk.slots
ELSE fac.membercost*bk.slots
end as cost

/* Joins the tables on the memid and the facilities ids */
FROM cd.members
	join cd.bookings bk
	  on cd.members.memid=bk.memid
	join cd.facilities fac
	  on bk.facid=fac.facid
 
  ) as table_use
  
  GROUP BY table_use.name
  ) as table_use1
  
 /* orders by the class and the name */
 ORDER BY class DESC, name
```
***Based on the 3 complete months of data so far, calculate the amount of time each facility will take to repay its cost of ownership. Remember to take into account ongoing monthly maintenance. Output facility name and payback time in months, order by facility name.***
```
SELECT fac.name as name, 

/* Calculates the months to make back the initial outlay */
fac.initialoutlay/((sum(
CASE  /* the results of the CASE calculation by 3 to convert into monthly terms */
WHEN memid=0 THEN fac.guestcost*bk.slots
ELSE fac.membercost*bk.slots
END )/3) - fac.monthlymaintenance) as months

/* Joins the bookings table and the facilities tables */
FROM cd.bookings bk
	join cd.facilities fac
	  on bk.facid=fac.facid
				   
/* Does the sum calculation for distinct facilities */  
 GROUP BY fac.facid
  
/* orders by the name */
 ORDER BY name
 ```

