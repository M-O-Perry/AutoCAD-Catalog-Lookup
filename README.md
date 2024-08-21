# AutoCAD-Catalog-Lookup
A program that looks through the AutoCAD Electrical Catalog and tells the user where the part is


7/28/2022

This is a search tool made to look through the AutoCAD Electrical Catalog.
It takes in a keyword (Manufacturer, Part Number, M&O Perry Number, Title, anything really) and browses through all the rows of the tables in the database.
Upon finding the keyword, it outputs the name of the table that the keyword is located in.
Any repeated occurrences of the keyword in the database will be displayed.

I've included an additional feature where typing an * at the end of a keyword will search and autofill for any similar keywords.
For example, typing 7825-9A-12* will search and autofill anything with 7825-9A-12XX.

Whether you like it or not, all searches must be at least 2 characters long.
The database directory is hardcoded to E:\Public\AutoCADShare\AeData\en-US\Catalogs\default_cat.mdb

If you are getting an error message about being unable to access the database:
-Check if you are connected to the company’s internet & server.
-Check your Read permissions. My intern Windows account did not work but an admin account did.
-Check if the database is still located at the same directory.
-Check if the name of the database is still "default_cat.mdb".
-Check the source code with someone who knows what they're doing (not me)

Useful Links:
pypi.org/project/pyodbc
github.com/mkleehammer/pyodbc

I used pyinstaller to turn the program into .exe

