DROP TABLE IF EXISTS patients;

CREATE TABLE patients (
  patient_id integer PRIMARY KEY UNIQUE,
  first_name text,
  last_name text,
  gender text,
  date_of_birth
);

CREATE INDEX patients_PK ON patients (patient_id);



DROP TABLE IF EXISTS practices;

CREATE TABLE practices (
  practice_id integer PRIMARY KEY UNIQUE,
  name text,
  location text
);

CREATE INDEX practices_PK ON practices (practice_id);



DROP TABLE IF EXISTS encounters;

CREATE TABLE encounters (
  encounter_id integer PRIMARY KEY UNIQUE,
  patient_id integer,
  practice_id integer,
  timestamp text,
  FOREIGN KEY(patient_id) REFERENCES patients(patient_id),
  FOREIGN KEY(practice_id) REFERENCES practices(practice_id)
);

CREATE INDEX encounters_PK ON encounters (encounter_id);

CREATE INDEX encounters_FK_patient_id ON patients (patient_id);
CREATE INDEX encounters_FK_practice_id ON practices (practice_id);


DROP TABLE IF EXISTS cvx_codes;

CREATE TABLE cvx_codes (
  code              INTEGER PRIMARY KEY UNIQUE,
  short_description TEXT,
  full_vaccine_name TEXT,
  notes             TEXT,
  status            TEXT,
  non_vaccine       TEXT,
  last_updated      TEXT
);

CREATE UNIQUE INDEX cvx_codes_PK ON cvx_codes(code);

