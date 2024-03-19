CREATE DATABASE IF NOT EXISTS Inventory;
CREATE USER IF NOT EXISTS 'dev'@'localhost' IDENTIFIED BY 'dev123';
GRANT ALL PRIVILEGES ON `Inventory`.* TO 'dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'dev'@'localhost';
FLUSH PRIVILEGES;