CREATE DATABASE ficodeDB;
USE ficodeDB;

CREATE TABLE Departments(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(200) NOT NULL,
    BUILDING_NUM INT
	);
    
    CREATE TABLE Employees(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Employees_name VARCHAR(200) NOT NULL,
    Dept_id INT ,
    salary INT,
	FOREIGN KEY(Dept_id) REFERENCES Departments(ID)
    );
    
		CREATE TABLE DepartmentTimings(
        ID INT AUTO_INCREMENT PRIMARY KEY,
        TIME VARCHAR(20),
        Dept_id INT,
		FOREIGN KEY(Dept_id) REFERENCES Departments(ID)
	);
        
	INSERT INTO departments(NAME,BUILDING_NUM) VALUES 
    ('ECE',2),
    ('CSE',3);
        
    INSERT INTO departmenttimings(TIME,Dept_id) VALUES 
    ('2.50',1),
    ('6.40',2);
    
    INSERT INTO employees(Employees_name,salary,Dept_id) VALUES 
    ('Rohit',2000,1),
    ('Deepak',4000,2),
    ('Rohit1',8000,1),
    ('Deepak2',14000,2);
    
    show tables;
    
    
    