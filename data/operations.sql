USE scooby_doo;

SELECT *
FROM episode_details
WHERE episode_id = 501;

SELECT *
FROM settings;

SELECT setting_id
FROM settings
WHERE setting_place = 'United States'
    AND setting_terrain = 'Urban';

# can be done without a place but there has to be terrain
delimiter $$
CREATE PROCEDURE Create_Setting(
    IN terrain varchar(60),
        place varchar(60),
    OUT S_id int)
BEGIN
    INSERT INTO settings (setting_terrain, setting_place)
        VALUES (terrain, place);

    SELECT setting_id
        INTO S_id
        FROM settings
        WHERE setting_place = place
        AND setting_terrain = terrain;
end $$

delimiter $$
DROP PROCEDURE Create_Culprit;
CREATE PROCEDURE Create_Culprit(
    IN name varchar(60),
        gender varchar(15)
)
BEGIN
    DECLARE c_id int;

    START TRANSACTION;
        INSERT INTO culprits (culprit_name, culprit_gender)
            VALUES (name, gender);

        SELECT culprit_id INTO c_id
        FROM culprits
        WHERE culprit_name = name
        AND culprit_gender = gender;

        IF c_id > 0 THEN
            COMMIT;
        ELSE
            ROLLBACK;
        END IF;
end $$

delimiter $$
CREATE PROCEDURE Create_Monster(
    IN name varchar(60),
        gender varchar(10),
        type varchar(40),
        subtype varchar(40),
        species varchar(40),
    OUT M_id int
)
BEGIN
    INSERT INTO monsters (monster_name, monster_gender, monster_type, monster_subtype, monster_species)
        VALUES (name, gender, type, subtype, species);
    SELECT monster_id
    INTO M_id
    FROM monsters
    WHERE monster_name = name
    AND monster_gender = gender
    AND monster_type = type
    AND monster_subtype = subtype
    AND monster_species = species;
end $$

delimiter $$
CREATE PROCEDURE Create_Actor(
    IN name_character varchar(60),
        actor varchar(60),
    OUT VA_id int
)
BEGIN
    INSERT INTO voice_actors (character_name, actor_name)
        VALUES (name_character, actor);
    SELECT actor_id
    INTO VA_id
    FROM voice_actors
    WHERE character_name = name_character
    AND actor_name = actor;
end $$

delimiter $$
CREATE PROCEDURE Create_Episode(
    IN series varchar(60),
        season_num int,
        ep_name varchar(60),
        date varchar(30),
        time int,
        monster varchar(15),
        cause varchar(30),
    OUT VA_id int
)
BEGIN
    INSERT INTO episode_details (series_name, season, title, date_aired, run_time, monster_real, motive)
        VALUES (series, season_num, ep_name, date, time, monster, cause);
    SELECT episode_id
    INTO VA_id
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
CREATE PROCEDURE Add_Culprit(
    IN episode int,
     culprit int
)
BEGIN
    INSERT INTO episode_culprits (episode_id, culprit_id)
        VALUES (episode, culprit);
end $$

delimiter $$
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
CREATE PROCEDURE Add_Monster(
    IN episode int,
     monster int
)
BEGIN
    INSERT INTO episode_monsters (episode_id, monster_id)
        VALUES (episode, monster);
end $$

delimiter $$
CREATE PROCEDURE Add_Actor(
    IN episode int,
     actor int
)
BEGIN
    INSERT INTO episode_actors (episode_id, actor_id)
        VALUES (episode, actor);
end $$
