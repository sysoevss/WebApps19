Database (MySQL)
Schema: markbook

CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `comment` varchar(128) DEFAULT NULL,
  `is_admin` int(11) NOT NULL DEFAULT '0',
  `login` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `login_UNIQUE` (`login`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

CREATE TABLE `courses` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(145) NOT NULL,
  `id_instructor` int(11) DEFAULT NULL,
  `exam_1` datetime DEFAULT NULL,
  `exam_2` datetime DEFAULT NULL,
  `exam_3` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

CREATE TABLE `course_student` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `id_course` int(11) NOT NULL,
  `id_student` int(11) NOT NULL,
  `mark_type` int(11) NOT NULL DEFAULT '0',
  `mark` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
