CREATE DATABASE IF NOT EXISTS db3;
USE db3;
CREATE TABLE IF NOT EXISTS investments (
    investment_id VARCHAR(20) PRIMARY KEY,
    investment_type VARCHAR(50),
    amount DECIMAL(10, 2),              
    investor_name VARCHAR(100),               
    interest_rate DECIMAL(5, 2),             
    duration INT,                            
    start_date DATE                          
);
INSERT INTO investments (investment_id, investment_type, amount, investor_name, interest_rate, duration, start_date)
VALUES
('INV001', 'Bitcoins', 10000.00, 'John Doe', 5.5, 12, '2023-01-01'),
('INV002', 'Shares', 5000.00, 'Jane Smith', 4.0, 24, '2023-06-15'),
('INV003', 'Money', 20000.00, 'Michael Johnson', 6.0, 36, '2022-10-30'),
('INV004', 'Bitcoins', 15000.00, 'Sarah Lee', 7.2, 18, '2023-03-10');
select * from investments;
