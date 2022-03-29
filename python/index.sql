/*exécuter ces commandes sur votre terminal*/
/*1- $ sudo mysql */
/*2- $ source /le chemin ou ce trouve ce fichier/identifiat.sql*/

DROP DATABASE if exists File ;
CREATE DATABASE File;
USE File;

create user python3 identified by 'python3';
grant all privileges on File.* to python3;


drop table if exists liste_mots;
CREATE TABLE liste_mots (
  id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  words varchar(100) NOT NULL,
  number_of_words int NOT NULL,
  file_name varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

