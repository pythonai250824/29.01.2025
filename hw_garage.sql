CREATE TABLE garage (
    fix_id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_number TEXT UNIQUE NOT NULL,
    car_problem TEXT NOT NULL,
    fixed BOOLEAN DEFAULT FALSE,
    owner_ph TEXT NOT NULL
);


INSERT INTO garage (car_number, car_problem, fixed, owner_ph)
VALUES 
('23', 'Engine overheating after long drives', TRUE, '555-1023');

INSERT INTO garage (car_number, car_problem, fixed, owner_ph)
VALUES 
('34', 'Brake pads worn out, needs replacement', TRUE, '555-1034');

INSERT INTO garage (car_number, car_problem, fixed, owner_ph)
VALUES 
('30', 'Check engine light on, possible sensor issue', TRUE, '555-1030');

INSERT INTO garage (car_number, car_problem, fixed, owner_ph)
VALUES 
('24', 'Battery drains overnight, needs diagnosis', FALSE, '555-1024');

INSERT INTO garage (car_number, car_problem, fixed, owner_ph)
VALUES 
('3', 'Strange noise from suspension when turning', FALSE, '555-1003');
