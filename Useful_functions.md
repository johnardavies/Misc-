##A list of useful SQL functions##

**NULIF(var1, var2)**
Returns a null if the first two variables are equal

**SQUARE(var1)**
Returns the square of a numeric var1 variable

**COALESCE(var1, var2, var3,   ... varn)**
Returns the first non null input from the inputs

**DATEDIFF(datepart, startdate, enddate)**
Calculates the difference between the startdate and the enddate. Datepart indicates the unit,

**DATE_TRUNC(text, timestamp)**
Truncates a timestamp at a given level e.g. DATE_TRUNC('hour', '2002-09-17 19:27:45') gives '2002-09-17 19:00'

**NTILE(number_expression) OVER (PARTITION BY partition_expression) ORDER BY sort expression [ASC|DSC]**
creates a partition into number_expression values e.g. number_expression=5  then values=1,2,3,4,5
ORDER BY specifies the order in which the NTILE is applied e.g. ascending or descenting 
PARTITION BY splits the rows into the  partitions into which the NTILE function is applied. This is optional
