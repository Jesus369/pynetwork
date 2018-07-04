
drop table if exists posts;
	create table posts (
		id integer primary key autoincrement,
		name text non null,
		context text non null
);

