USE scooby_doo;

ALTER TABLE Culprits
    ADD COLUMN is_deleted INT NOT NULL DEFAULT 0;

ALTER TABLE Monsters
    ADD COLUMN is_deleted INT NOT NULL DEFAULT 0;

ALTER TABLE Settings
    ADD COLUMN is_deleted INT NOT NULL DEFAULT 0;

ALTER TABLE Voice_Actors
    ADD COLUMN is_deleted INT NOT NULL DEFAULT 0;

ALTER TABLE Episode_Details
    ADD COLUMN is_deleted INT NOT NULL DEFAULT 0;

ALTER TABLE Episode_Actors
    ADD COLUMN is_deleted INT NOT NULL DEFAULT 0;

ALTER TABLE Episode_Culprits
    ADD COLUMN is_deleted INT NOT NULL DEFAULT 0;

ALTER TABLE Episode_Monsters
    ADD COLUMN is_deleted INT NOT NULL DEFAULT 0;

SELECT *
FROM Episode_Monsters;

SELECT *
FROM settings;

SELECT setting_id
FROM settings
WHERE setting_place = 'United States'
    AND setting_terrain = 'Urban';

delimiter $$
DROP PROCEDURE IF EXISTS Create_Setting $$
CREATE PROCEDURE Create_Setting(
    IN terrain varchar(60),
        place varchar(60))
BEGIN
    DECLARE s_id int;

    START TRANSACTION;
    INSERT INTO settings (setting_terrain, setting_place)
        VALUES (terrain, place);

    SELECT setting_id
        INTO s_id
        FROM settings
        WHERE setting_place = place
        AND setting_terrain = terrain;

    IF s_id > 0 THEN
            COMMIT;
        ELSE
            ROLLBACK;
        END IF;
end $$

delimiter $$
DROP PROCEDURE IF EXISTS Create_Culprit $$
CREATE PROCEDURE Create_Culprit(
    IN name varchar(60),
        gender varchar(15)
)
BEGIN
        INSERT INTO culprits (culprit_name, culprit_gender)
            VALUES (name, gender);

        SELECT culprit_id
        FROM culprits
        WHERE culprit_name = name
        AND culprit_gender = gender;

end $$

delimiter $$
DROP PROCEDURE IF EXISTS Create_Monster $$
CREATE PROCEDURE Create_Monster(
    IN name varchar(60),
        gender varchar(10),
        type varchar(40),
        subtype varchar(40),
        species varchar(40)
)
BEGIN
    DECLARE m_id int;

    START TRANSACTION;
    INSERT INTO monsters (monster_name, monster_gender, monster_type, monster_subtype, monster_species)
        VALUES (name, gender, type, subtype, species);

    SELECT monster_id INTO m_id
    FROM monsters
    WHERE monster_name = name
    AND monster_gender = gender
    AND monster_type = type
    AND monster_subtype = subtype
    AND monster_species = species;

    IF m_id > 0 THEN
            COMMIT;
        ELSE
            ROLLBACK;
        END IF;
end $$

delimiter $$
DROP PROCEDURE IF EXISTS Create_Actor $$
CREATE PROCEDURE Create_Actor(
    IN name_character varchar(60),
        actor varchar(60)
)
BEGIN
    DECLARE a_id int;

    START TRANSACTION;
    INSERT INTO voice_actors (character_name, actor_name)
        VALUES (name_character, actor);

    SELECT actor_id INTO a_id
    FROM voice_actors
    WHERE character_name = name_character
    AND actor_name = actor;

    IF a_id > 0 THEN
            COMMIT;
        ELSE
            ROLLBACK;
        END IF;
end $$

delimiter $$
DROP PROCEDURE IF EXISTS Create_Episode $$
CREATE PROCEDURE Create_Episode(
    IN series varchar(60),
        season_num int,
        ep_name varchar(60),
        date varchar(30),
        time int,
        monster varchar(15),
        cause varchar(30)
)
BEGIN
    INSERT INTO episode_details (series_name, season, title, date_aired, run_time, monster_real, motive)
        VALUES (series, season_num, ep_name, date, time, monster, cause);

    SELECT episode_id
    FROM episode_details
    WHERE series_name = series
    AND season = season_num
    AND title = ep_name
    and date_aired = date
    and run_time = time
    and monster_real = monster
    and motive = cause;
end $$

delimiter $$
DROP PROCEDURE IF EXISTS Add_Culprit $$
CREATE PROCEDURE Add_Culprit(
    IN episode int,
     culprit int
)
BEGIN
    INSERT INTO episode_culprits (episode_id, culprit_id)
        VALUES (episode, culprit);
end $$

delimiter $$
DROP PROCEDURE IF EXISTS Add_Setting $$
CREATE PROCEDURE Add_Setting(
    IN episode int,
     setting int
)
BEGIN
    UPDATE episode_details
        SET setting_id = setting
    WHERE episode_id = episode;
end $$

delimiter $$
DROP PROCEDURE IF EXISTS Add_Monster $$
CREATE PROCEDURE Add_Monster(
    IN episode int,
     monster int
)
BEGIN
    INSERT INTO episode_monsters (episode_id, monster_id)
        VALUES (episode, monster);
end $$

delimiter $$
DROP PROCEDURE IF EXISTS Add_Actor $$
CREATE PROCEDURE Add_Actor(
    IN episode int,
     actor int
)
BEGIN
    INSERT INTO episode_actors (episode_id, actor_id)
        VALUES (episode, actor);
end $$
