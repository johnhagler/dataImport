DROP TABLE patients IF EXISTS;

CREATE TABLE patients (
  patient_id integer PRIMARY KEY UNIQUE,
  first_name text,
  last_name text,
  gender text,
  date_of_birth
);

CREATE INDEX patients_PK ON patients (patient_id);


DROP TABLE encounters IF EXISTS;

CREATE TABLE encounters (
  encounter_id integer PRIMARY KEY UNIQUE,
  patient_id integer,
  timestamp text,
  FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
);

CREATE INDEX encounters_PK ON patients (encounter_id);

