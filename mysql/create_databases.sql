USE spa;

DROP TABLE booking;

CREATE TABLE booking ( id INT unsigned NOT NULL auto_increment,
					   id_room INT unsigned NOT NULL,
					   start_date DATE NOT NULL,
					   end_date DATE NOT NULL,
					   FULL_NAME VARCHAR(60) NOT NULL,
					   PHONE_NUMBER  VARCHAR(20),
					   CONSTRAINT pk_constraint PRIMARY KEY (id),
					   CONSTRAINT unique_session UNIQUE(id_room, start_date, FULL_NAME, PHONE_NUMBER) );

CREATE TABLE room_type ( id INT unsigned NOT NULL auto_increment,
						 name VARCHAR(30) NOT NULL,
						 cost INT unsigned NOT NULL,
						 CONSTRAINT pk_constraint PRIMARY KEY (id),
						 UNIQUE(name) );

CREATE TABLE rooms ( id INT unsigned NOT NULL auto_increment,
					 id_room INT unsigned NOT NULL,
					 room_type INT NOT NULL,
					 CONSTRAINT pk_constraint PRIMARY KEY (id) );

