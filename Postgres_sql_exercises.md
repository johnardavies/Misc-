##Solutions to exercies from https://pgexercises.com/##


***There are three tables a members table, a bookings table and a facilities table***

***How can you produce a list of the start times for bookings by members named 'David Farrell'?***

```select starttime from cd.members

join cd.bookings

on cd.bookings.memid=cd.members.memid

WHERE CONCAT(firstname, surname) LIKE 'DavidFarrell';
```

***How can you produce a list of the start times for bookings for tennis courts, for the date '2012-09-21'? Return a list of start time and facility name pairings, ordered
by the time***

```select  starttime, name from cd.members

join cd.bookings

on cd.bookings.memid=cd.members.memid 

join cd.facilities

on cd.bookings.facid=cd.facilities.facid

WHERE cd.facilities.name LIKE 'Tennis Court%' AND (CAST(starttime AS date)='2012-09-21')
 
ORDER BY starttime ASC;
```

***How can you output a list of all members who have recommended another member? Ensure that there are no duplicates in the list, 
and that results are ordered by (surname, firstname).***


```SELECT DISTINCT mem2.firstname as firstname, mem2.surname as surname
FROM cd.members 
inner join cd.members as mem2 
on cd.members.recommendedby=mem2.memid 
WHERE cd.members.recommendedby >0 
ORDER BY mem2.surname ASC , mem2.firstname  DESC;
```

***How can you output a list of all members, including the individual who recommended them (if any)?***
***Ensure that results are ordered by (surname, firstname).***

```SELECT cd.members.firstname as memfname, cd.members.surname as memsname ,  mem2.firstname as recfname, mem2.surname as recsname 
FROM cd.members. 
left outer join cd.members as mem2 
on cd.members.recommendedby=mem2.memid 
ORDER BY memsname, memfname ASC;
``` 

***How can you produce a list of all members who have used a tennis court? Include in your output the name of the court, and the name of the member formatted as a single column. Ensure no duplicate data, and order by the member name followed by the facility name.***

```SELECT DISTINCT CONCAT(firstname,' ', surname) as member , fac.name as facility FROM cd.members 
    join 
    cd.bookings bk 
    on bk.memid=cd.members.memid 
    join 
    cd.facilities fac 
    on bk.facid=fac.facid 
    WHERE fac.name LIKE 'Tennis Court%' 
    ORDER BY member , facility ASC ;
    ```

