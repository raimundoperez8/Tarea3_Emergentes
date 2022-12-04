CREATE TABLE IF NOT EXISTS "company" (
	"ID"	INTEGER NOT NULL,
	"company_name"	TEXT NOT NULL,
	"company_api_key"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "location" (
	"company_id"	INTEGER NOT NULL,
	"location_id"	INTEGER NOT NULL,
	"location_name"	TEXT NOT NULL,
	"location_country"	TEXT NOT NULL,
	"location_city"	TEXT NOT NULL,
	"location_meta"	TEXT,
	PRIMARY KEY("company_id","location_id")
);
CREATE TABLE IF NOT EXISTS "sensor" (
	"location_id"	INTEGER NOT NULL,
	"sensor_id"	INTEGER NOT NULL,
	"sensor_name"	INTEGER NOT NULL,
	"sensor_category"	TEXT NOT NULL,
	"sensor_meta"	TEXT,
	"sensor_api_key"	TEXT,
	PRIMARY KEY("location_id","sensor_id")
);