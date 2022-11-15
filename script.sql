INSERT INTO `alternative-db`.`addresses` VALUES
(1, "Dresden", "25783", "Dobrovolná", 130), 
(2, "Brno", "34067", "Hlinky", 34), 
(3, "Dresden", "58315", "Tinková", 52), 
(4, "Brno", "54650", "Nováková", 93), 
(5, "České Budějovice", "50915", "Tinková", 104), 
(6, "Ostrava", "45388", "Novotná", 86), 
(7, "Brno", "65816", "Červinková", 84), 
(8, "Brno", "43564", "Nováková", 182), 
(9, "Brno", "36757", "Mendlová", 160), 
(10, "Pardubice", "88950", "Hlinky", 28); 

INSERT INTO `alternative-db`.`specialities` VALUES
(1, "Surgery", "description"), 
(2, "Pediatry", "description"), 
(3, "Dentistry", "description"); 

INSERT INTO `alternative-db`.`treatments` VALUES
(1, "<tables.entities.specialities.Speciality object at 0x000002153D43CA90>", Chromoendoscopy, "100", 2), 
(2, "<tables.entities.specialities.Speciality object at 0x000002153D43CA90>", Endoscopic Ultrasound, "900", 2), 
(3, "<tables.entities.specialities.Speciality object at 0x000002153D43CA90>", Capsule Endoscopy, "300", 3), 
(4, "<tables.entities.specialities.Speciality object at 0x000002153D43CA90>", Chromoendoscopy, "600", 6), 
(5, "<tables.entities.specialities.Speciality object at 0x000002153D43CDC0>", Endoscopic Suturing, "200", 4); 

INSERT INTO `alternative-db`.`login-data` VALUES
("1", "cekhlpkwny@email.com", "{bcrypt}$2a$10$0YnP.OvKmDCTi2TtsWAcNun9WEQDw7a9Ddt9L3KzLPEgd47oSsw4i", "ROLE_CLIENT"), 
("2", "vaapvjzzbx@email.com", "{bcrypt}$2a$10$0YnP.OvKmDCTi2TtsWAcNun9WEQDw7a9Ddt9L3KzLPEgd47oSsw4i", "ROLE_CLIENT"), 
("3", "ggyxklbdrw@email.com", "{bcrypt}$2a$10$0YnP.OvKmDCTi2TtsWAcNun9WEQDw7a9Ddt9L3KzLPEgd47oSsw4i", "ROLE_CLIENT"), 
("4", "fucfmwhnqk@email.com", "{bcrypt}$2a$10$0YnP.OvKmDCTi2TtsWAcNun9WEQDw7a9Ddt9L3KzLPEgd47oSsw4i", "ROLE_CLIENT"), 
("5", "ndgvoreeeh@email.com", "{bcrypt}$2a$10$0YnP.OvKmDCTi2TtsWAcNun9WEQDw7a9Ddt9L3KzLPEgd47oSsw4i", "ROLE_CLIENT"), 
("6", "buqhtzeyfh@email.com", "{bcrypt}$2a$10$0YnP.OvKmDCTi2TtsWAcNun9WEQDw7a9Ddt9L3KzLPEgd47oSsw4i", "ROLE_CLIENT"), 
("7", "rpsdjbncba@email.com", "{bcrypt}$2a$10$0YnP.OvKmDCTi2TtsWAcNun9WEQDw7a9Ddt9L3KzLPEgd47oSsw4i", "ROLE_CLIENT"), 
("8", "unybdzqrud@email.com", "{bcrypt}$2a$10$0YnP.OvKmDCTi2TtsWAcNun9WEQDw7a9Ddt9L3KzLPEgd47oSsw4i", "ROLE_CLIENT"), 
("9", "ehhgczmanu@email.com", "{bcrypt}$2a$10$0YnP.OvKmDCTi2TtsWAcNun9WEQDw7a9Ddt9L3KzLPEgd47oSsw4i", "ROLE_DOCTOR"), 
("10", "ybxcphahbg@email.com", "{bcrypt}$2a$10$0YnP.OvKmDCTi2TtsWAcNun9WEQDw7a9Ddt9L3KzLPEgd47oSsw4i", "ROLE_DOCTOR"); 

INSERT INTO `alternative-db`.`contact` VALUES
(1, "Lenka", "Sedláčková", "Dentistry", "description"), 
(2, "Václav", "Horák", "Surgery", "description"), 
(3, "Marie", "Marková", "Pediatry", "description"), 
(4, "Pavel", "Marek", "Pediatry", "description"), 
(5, "Anna", "Hájková", "Dentistry", "description"), 
(6, "Ondřej", "Beneš", "Pediatry", "description"), 
(7, "Meredith", "Pospíšilová", "Surgery", "description"), 
(8, "Ladislav", "Hájek", "Pediatry", "description"), 
(9, "Ekaterina", "Němcová", "Pediatry", "description"), 
(10, "Jaroslav", "Horák", "Dentistry", "description"); 

INSERT INTO `alternative-db`.`clients` VALUES
(1, "Svetlana", "Sedláčková", "giwffxlpcd@email.com"), 
(2, "Roman", "Procházka", "upphnqacng@email.com"), 
(3, "Anna", "Fialová", "gemvwjnime@email.com"), 
(4, "Tomáš", "Veselý", "ykrdqcbpsf@email.com"), 
(5, "Jana", "Benešová", "dcshiyzgyg@email.com"), 
(6, "Jan", "Dvořák", "zbmhymdyyb@email.com"), 
(7, "Hana", "Králová", "wmvyogoqab@email.com"), 
(8, "Jiří", "Beneš", "mhibpcgfjw@email.com"); 

INSERT INTO `alternative-db`.`doctors` VALUES
(1, "9", "description_slot", "1", "3", "1"), 
(2, "10", "description_slot", "1", "6", "1"); 

INSERT INTO `alternative-db`.`visits` VALUES
(1, 3, 2, 3, 300, "2022-09-18 15:00:00"), 
(2, 3, 1, 1, 100, "2022-11-14 16:00:00"), 
(3, 7, 1, 5, 200, "2022-12-09 14:00:00"), 
(4, 7, 1, 2, 900, "2022-11-23 15:00:00"), 
(5, 4, 1, 5, 200, "2022-09-28 15:00:00"), 
(6, 2, 2, 2, 900, "2022-09-13 15:00:00"), 
(7, 5, 2, 4, 600, "2022-11-19 09:00:00"), 
(8, 1, 2, 1, 100, "2022-09-15 14:00:00"), 
(9, 5, 1, 3, 300, "2022-11-24 09:00:00"), 
(10, 5, 1, 4, 600, "2022-10-20 16:00:00"), 
(11, 2, 1, 4, 600, "2022-09-02 09:00:00"), 
(12, 5, 1, 3, 300, "2022-10-20 10:00:00"), 
(13, 1, 1, 5, 200, "2022-09-08 09:00:00"), 
(14, 6, 1, 5, 200, "2022-10-23 13:00:00"), 
(15, 3, 2, 1, 100, "2022-11-06 17:00:00"), 
(16, 3, 2, 3, 300, "2022-12-04 16:00:00"), 
(17, 5, 2, 5, 200, "2022-10-04 17:00:00"), 
(18, 1, 1, 2, 900, "2022-09-13 16:00:00"), 
(19, 6, 1, 2, 900, "2022-09-13 11:00:00"), 
(20, 2, 1, 4, 600, "2022-12-01 17:00:00"), 
(21, 3, 1, 1, 100, "2022-09-26 11:00:00"), 
(22, 6, 1, 3, 300, "2022-09-16 11:00:00"), 
(23, 7, 1, 1, 100, "2022-09-11 11:00:00"), 
(24, 4, 2, 5, 200, "2022-12-24 13:00:00"), 
(25, 2, 1, 2, 900, "2022-11-14 17:00:00"), 
(26, 6, 2, 2, 900, "2022-12-14 16:00:00"), 
(27, 1, 1, 4, 600, "2022-09-07 13:00:00"), 
(28, 4, 2, 3, 300, "2022-09-29 17:00:00"), 
(29, 7, 2, 5, 200, "2022-12-10 17:00:00"), 
(30, 5, 1, 2, 900, "2022-10-23 15:00:00"); 

