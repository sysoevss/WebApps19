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

INSERT INTO booking ( id_room, start_date, end_date, FULL_NAME ) VALUES ( 1, "2018-11-10", "2018-11-15", "user1" );
INSERT INTO booking ( id_room, start_date, end_date, FULL_NAME ) VALUES ( 1, "2018-11-20", "2018-11-25", "user1" );
INSERT INTO booking ( id_room, start_date, end_date, FULL_NAME ) VALUES ( 2, "2018-11-20", "2018-11-25", "user2" );
INSERT INTO booking ( id_room, start_date, end_date, FULL_NAME ) VALUES ( 3, "2018-12-01", "2018-12-10", "user3" );
INSERT INTO booking ( id_room, start_date, end_date, FULL_NAME ) VALUES ( 3, "2018-12-15", "2018-12-20", "user3" );
INSERT INTO booking ( id_room, start_date, end_date, FULL_NAME ) VALUES ( 3, "2018-12-25", "2018-12-30", "user3" );