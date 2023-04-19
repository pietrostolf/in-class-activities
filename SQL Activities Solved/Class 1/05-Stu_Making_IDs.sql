-- DROP TABLE programming_languages;

CREATE TABLE programming_languages (
    id SERIAL PRIMARY KEY,
    language VARCHAR(20),
    rating INTEGER
);

INSERT INTO programming_languages (language, rating)
VALUES ('HTML', 95),
       ('JS', 99),
       ('JQuery', 98),
       ('MySQL', 70),
       ('MySQL', 70);

SELECT * FROM programming_languages
WHERE language = 'MySQL';

DELETE FROM programming_languages
WHERE id = (
    SELECT id FROM programming_languages
    WHERE language = 'MySQL'
    ORDER BY id DESC
    LIMIT 1
);

INSERT INTO programming_languages (language, rating)
VALUES ('Python', 85),
       ('Java', 80),
       ('C++', 75);

UPDATE programming_languages
SET language = 'JavaScript'
WHERE language = 'JS';

UPDATE programming_languages
SET rating = 90
WHERE language = 'HTML';

SELECT * from programming_languages
ORDER BY id;