Example application which reads a CSV file containing URLs of websites and using Beautifulsoup to scrap a website title & body. The script stores the title & body in a MySQL database. Please follow the robots.txt for each webpage before you do any scraping.

The MySQL table looks as follows:
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

The DBConfig is expected in a JSON file. The JSON file format should look like the following:
{"dbconfig":  {"host": "127.0.0.1",
            "user": "user",
            "password": "password",
            "database": "website"}}
