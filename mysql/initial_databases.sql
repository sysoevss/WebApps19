CREATE DATABASE spa;
USE spa;

CREATE TABLE users ( id INT unsigned not null auto_increment,
					 user_name VARCHAR(30) not null,
					 password VARCHAR(30) not null,
					 constraint pk_example primary key (id) );
INSERT INTO users ( user_name, password ) VALUES ( "sysoev", "123" );
