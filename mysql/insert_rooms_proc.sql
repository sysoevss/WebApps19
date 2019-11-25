USE spa;

DELIMITER $$

DROP PROCEDURE IF EXISTS myproc$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `myproc`()
BEGIN
	DECLARE i INT DEFAULT 0;
	test_loop : LOOP
		IF (i >= 400) THEN
			LEAVE test_loop;
		END IF;
		
        IF (((i DIV 20) MOD 2) = 0) THEN
			INSERT INTO rooms ( id_room, room_type ) VALUES ( i, 1 );
        END IF;
		SET i = i + 1;
	END LOOP;
END $$

DELIMITER ;

call `myproc`;