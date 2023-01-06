CREATE TABLE `undergraduate`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `jobname` VARCHAR(20) NOT NULL,
   `keyword` VARCHAR(15) NOT NULL,
   `salary` VARCHAR(10) NOT NULL,
   `city` VARCHAR(6) NOT NULL,
   `company` VARCHAR(15) NOT NULL,
   `skills` VARCHAR(30) NOT NULL,
   `experience` VARCHAR(10) NOT NULL,
   `type` VARCHAR(5) NOT NULL,
   `industrial_chain` VARCHAR(10) NOT NULL,
   `description` VARCHAR(500) NOT NULL,
   `upload_date` DATE NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `postgraduate`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `jobname` VARCHAR(20) NOT NULL,
   `keyword` VARCHAR(15) NOT NULL,
   `salary` VARCHAR(10) NOT NULL,
   `city` VARCHAR(6) NOT NULL,
   `company` VARCHAR(15) NOT NULL,
   `skills` VARCHAR(30) NOT NULL,
   `experience` VARCHAR(10) NOT NULL,
   `type` VARCHAR(5) NOT NULL,
   `industrial_chain` VARCHAR(10) NOT NULL,
   `description` VARCHAR(500) NOT NULL,
   `upload_date` DATE NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
