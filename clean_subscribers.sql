#Code used to normalize/clean data

#Normalizes those who put their birth years as ages
UPDATE subscribers
SET age = 2020 - age
WHERE age > 1800 AND age < 2020;


#Removes those that are greater than 120 (arbituarily chosen as a cutoff point))
UPDATE subscribers
SET age = ""
WHERE age > 120 AND age != "";

#Cleans those with negative Join Fees (doesnt make sense)
#Set to NULL (empty)
UPDATE subscribers
SET join_fee = join_fee * -1
WHERE join_fee < 0;

#Where cancellation date is before account creation
SELECT COUNT(*) FROM subscribers
WHERE account_creation_date < cancel_date
AND account_creation_date != ""
AND cancel_date != "";

#Where weekly_consumption_hour is negative
#Multiply by *-1 to get a positive hour
SELECT COUNT(*) FROM subscribers
WHERE weekly_consumption_hour < 0;

UPDATE subscribers
SET weekly_consumption_hour = weekly_consumption_hour * -1
WHERE weekly_consumption_hour < 0;

UPDATE subscribers
SET num_ideal_streaming_services  = num_ideal_streaming_services * -1
WHERE num_ideal_streaming_services < 0;

