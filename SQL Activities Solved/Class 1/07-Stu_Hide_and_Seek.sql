DROP TABLE movie_words_comparison;

CREATE TABLE movie_words_comparison (
    rater_id INTEGER,
    reference_title VARCHAR,
    soft_attribute VARCHAR,
    less_than VARCHAR,
    about_as VARCHAR,
    more_than VARCHAR
);

SELECT * FROM movie_words_comparison;

SELECT *
FROM movie_words_comparison
WHERE reference_title = 'Home Alone (1990)';

SELECT *
FROM movie_words_comparison
WHERE rater_id >= 10 AND rater_id <= 15;

SELECT *
FROM movie_words_comparison
WHERE soft_attribute LIKE '%artsy%' OR soft_attribute LIKE '%heartfelt%';