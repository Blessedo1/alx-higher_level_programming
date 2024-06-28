-- lists the number of records with the same score in the table 'second_table' of the database 'hbtn_0c_0' in mysql server
-- the list should display the score and number of records for this score with the laabel number
-- the list should be sorted by the number of records (descending)
-- The database name will be passed as an argument to the mysql command

SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC
