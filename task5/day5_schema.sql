

CREATE TABLE IF NOT EXISTS `TweetInformation` 
(
    `id` INT NOT NULL AUTO_INCREMENT,
    `clean_text` TEXT DEFAULT NULL,
    `polarity` FLOAT DEFAULT NULL,
    `subjectivity` FLOAT DEFAULT NULL,
    `language` TEXT DEFAULT NULL,
    
    PRIMARY KEY (`id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
