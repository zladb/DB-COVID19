CREATE TABLE IF NOT EXISTS HOSPITAL(
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(60) NOT NULL,
    province VARCHAR(50) NULL,
    city VARCHAR(15) NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    capacity INT NOT NULL,
    current INT NULL
);
