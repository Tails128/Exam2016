#how to use

1. install python
2. test by using this line:


cat mapreduce.css | python map.py | sort -k1,1 | python reduce.py

simple and clean.

##IMPORTANT


the input file must be submitted with the following criteria


- no  heading
- values as follow
Date; UserID; User's origin country; StructureID; Check-in; Check-out; Ticket Amout
- datatypes as follow
date;int;string;int;date;date;int (or money)