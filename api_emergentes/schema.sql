CREATE TABLE IF NOT EXISTS "admin" (
	"ID"	INTEGER NOT NULL,
	"username"	TEXT NOT NULL,
	"password"	TEXT NOT NULL,
	"admin_api_key"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
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
	PRIMARY KEY("location_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "sensor" (
	"location_id"	INTEGER NOT NULL,
	"sensor_id"	INTEGER NOT NULL,
	"sensor_name"	INTEGER NOT NULL,
	"sensor_category"	TEXT NOT NULL,
	"sensor_meta"	TEXT,
	"sensor_api_key"	TEXT,
	PRIMARY KEY("sensor_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "sensordata" (
	"ID"	INTEGER NOT NULL,
	"sensor_id"	TEXT NOT NULL,
	"medicion1"	TEXT NOT NULL,
	"medicion2"	TEXT,
	"medicion3"	TEXT,
	"date"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT)
);