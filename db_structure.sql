DROP TABLE IF EXISTS "user";
CREATE TABLE user (
	id INTEGER PRIMARY KEY, 
	username VARCHAR(25) UNIQUE, 
	password VARCHAR(25), 
	email VARCHAR(132),  
	UNIQUE (username)
);


DROP TABLE IF EXISTS "bookmark";
CREATE TABLE bookmark (
	id INTEGER PRIMARY KEY, 
	url VARCHAR(1024) NOT NULL, 
	description TEXT, 
	pub_date DATETIME, 
	author_id INTEGER, 
	FOREIGN KEY(author_id) REFERENCES user (id)
);
