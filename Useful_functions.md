## A list of useful SQL functions ##

**NVL(variable, substitute)** \
If a variable value is NULL return the substitute value, otherwise returns the variable value

**NULIF(var1, var2)** \
Returns a null if the first two variables are equal

**COALESCE(var1, var2, var3,  ... varn)** \
Returns the first non null input from the inputs

**SQUARE(var1)** \
Returns the square of a numeric var1 variable

**DATEADD(datepart , number , date)**  \
Increments a date by a part of the date e.g. if datepart = months and number is -24 then DATEADD returns the date from 24 months ago

**DATEDIFF(datepart, startdate, enddate)** \
Calculates the difference between the startdate and the enddate, datepart indicates the unit,

**DATE_TRUNC(text, timestamp)** \
Truncates a timestamp at a given level e.g. DATE_TRUNC('hour', '2002-09-17 19:27:45') gives '2002-09-17 19:00'

**FLOOR(number)** \
The FLOOR() function returns the largest integer value smaller than or equal to the number it has input

**GRANT** \
GRANT command gives specific privileges on a database object to one or more roles. 

**LEAST(variable)** \
Returns the smallest value. If there is a NULL value in the variable this will be returned

**RANK() OVER (PARTITION BY partition_expression) ORDER BY sort_expression [ASC|DSC]** \
Creates a rank variable for a given variable e.g. 1,2,3,4 etc specified by the sort_expression
if partition is not specified then the partition is each row, otherwise the ranking is applied within the categories specified by partition_expression.
e.g. if the partition was over say cities where cities is city A, city B, city C then the RANK would return the rank within a city for a given variable

**NTILE(number_expression) OVER (PARTITION BY partition_expression) ORDER BY sort_expression [ASC|DSC]** \
Creates a partition into number_expression values e.g. number_expression=5  then values=1,2,3,4,5
ORDER BY specifies the order in which the NTILE is applied e.g. ascending or descenting 
PARTITION BY splits the rows into the  partitions into which the NTILE function is applied. This is optional

**ROW_NUMBER() OVER([PARTITION BY column_1, column_2,…] [ORDER BY column_3,column_4,…])** \
Calculate row numbers over the ORDER BY columns, Partition by is optional and will apply the row_numbering within the variables categories
specified in the partition

**TRIM(string, 'characters')** \
Removes characters from a string if no characters removes blank spaces
