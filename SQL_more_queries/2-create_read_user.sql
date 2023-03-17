-- create database and new user

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

USE hbtn_0d_2;

CREATE USER IF NOT EXISTS 'user_0d_2'@'%' IDENTIFIED BY 'user_0d_2_pwd';
GRANT USAGE ON *.* TO 'user_0d_2'@'%';
GRANT SELECT ON 'user_0d_2'.* TO 'user_0d_2'@'%';
FLUSH PRIVILEGES;