-- Drop table if exists
DROP TABLE IF EXISTS road_accidents;

DROP TABLE IF EXISTS accidents_by_state;

-- Create new tables to import data
CREATE TABLE road_accidents (
	_id	INT PRIMARY KEY,
	Year INT,
	Registered_Vehicles	INT,
	Population INT,
	Road_Crashes INT,
	Road_Deaths INT,
	Serious_Injury INT,
	Slight_Injury INT,
	Index_per_10000_Vehicles DEC,
	Index_per_100000_Population DEC,	
	Index_per_billion_VKT DEC
);

CREATE TABLE accidents_by_state (
	Year INT,
	MYS_State VARCHAR,
	Road_Crashes INT,
	Road_Deaths INT,
	Serious_Injury INT,
	Slight_Injury INT
);

-- Import data from mys_road_accidents.csv
-- View the table to ensure all data has been imported correctly
SELECT * FROM road_accidents;

-- Import data from mys_accidents_by_state.csv
-- View the table to ensure all data has been imported correctly
SELECT * FROM accidents_by_state;

SELECT *
FROM road_accidents
WHERE road_crashes = 0;

DELETE FROM accidents_by_state
WHERE year <> 2017;

SELECT 
    SUM(serious_injury) AS serious_injury,
    SUM(slight_injury) AS slight_injury,
    SUM(road_deaths) AS road_deaths
FROM 
    accidents_by_state;
	
UPDATE road_accidents
SET serious_injury = 3310, slight_injury = 6539, road_crashes = 533875
WHERE year = 2017;

SELECT * FROM road_accidents
WHERE year = 2017;
