DROP table IF EXISTS posts;
	CREATE table posts (
		id integer primary key autoincrement,
		name TEXT not null, 
		content TEXT not null
);
