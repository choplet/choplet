CREATE TABLE IF NOT EXISTS shortener(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	original_url TEXT NOT NULL,
	short_url TEXT NOT NULL,
	created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO shortener (original_url, short_url) 
	VALUES ('Выучить историю земель царских', 'учеба')

