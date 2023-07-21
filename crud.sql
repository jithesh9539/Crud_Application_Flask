CREATE database CRUD;

USE	CRUD;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255),
    phone VARCHAR(20)
) AUTO_INCREMENT = 10;

 
 DROP TABLE STUDENTS;
 
 INSERT INTO students (id, name, email, phone) VALUES
(1, 'Abhi', 'abhi@gmail.com', '908393481'),
(8, 'Raj', 'raj1@gmail.com', '8989898909'),
(6, 'Jith', 'jith@gmail.com', '7333392987'),
(5, 'Akash', 'aksha@gmail.com', '2341234567'),
(4, 'James', 'james@gmail.com', '234567890'),
(12, 'Tim', 'tim@gmail.com', '2222222222'),
(19, 'Steven', 'steven@gmail.com', '9876543210'),
(25, 'Ian', 'ian@gmail.com', '0987654353');


  
select * from students;