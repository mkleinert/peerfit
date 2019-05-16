CREATE TABLE `Class` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `class_tag` varchar(63) UNIQUE ON CONFLICT IGNORE
);

CREATE TABLE `Club_Reservation` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `member_id` int,
  `studio_id` int,
  `class_id` int,
  `instructor_full_name` varchar(63),
  `level` int,
  `canceled` varchar(63),
  `reserved_for` text,
  `signed_in_at` text
);

CREATE TABLE `MBO_Reservations` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `member_id` int,
  `studio_id` int,
  `class_id` int,
  `viewed_at` text,
  `reserved_at` text,
  `canceled_at` text,
  `class_time_at` text,
  `checked_in_at` text
);

CREATE TABLE "Studio" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"studio_key"	TEXT UNIQUE ON CONFLICT IGNORE,
	"studio_address_street"	TEXT,
	"studio_address_city"	TEXT,
	"studio_address_state"	TEXT,
	"studio_address_zip"	BIGINT
);