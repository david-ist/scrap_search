Example application which reads a CSV file containing URLs and using Beautifulsoup to scrap a website title & body. It stores these in MySQL database. Please follow the robots.txt for each webpage before you do an scraping.

The MySQL table is simple, looks as follows:
CREATE TABLE `site` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `WEBSITE_URL` varchar(90) DEFAULT NULL,
  `WEBSITE_TITLE` mediumtext,
  `SITE_BODY` longtext,
  `SITE_HTML` longtext,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID_UNIQUE` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=209 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

The CSV file expecting a comma and than enter separated domain list.

ReadCSV.py -> read the CSV file and store it in the database
queries.py -> contains all the query functions used in the scripts
dbuse.py -> contex manager created for the database
lookup.py -> doing the actual lookup and storing it in a dictionary. 
