USE scooby_doo;

# PROCEDURES

-- CULPRITS --


DELIMITER ;;
DROP PROCEDURE IF EXISTS Query_Culprits ;;
CREATE PROCEDURE Query_Culprits(
        IN cn VARCHAR(60),
        IN cg VARCHAR(20)
    )
    BEGIN
        SELECT *
        FROM Culprits
        WHERE 1 = 1
        AND (cn IS NULL OR cn = culprit_name)
        AND (cg IS NULL OR cg = culprit_gender)
        AND is_deleted = 0;
END;;

-- MONSTERS --


DELIMITER ;;
DROP PROCEDURE IF EXISTS Query_Monsters ;;
CREATE PROCEDURE Query_Monsters(
        IN mn VARCHAR(60),
        IN mg VARCHAR(20),
        IN mt VARCHAR(60),
        IN ms VARCHAR(60),
        IN mst VARCHAR(60)
    )
    BEGIN
        SELECT *
        FROM Monsters
        WHERE 1 = 1
        AND (mn IS NULL OR mn = monster_name)
        AND (mg IS NULL OR mg = monster_gender)
        AND (mt IS NULL OR mt = monster_type)
        AND (ms IS NULL OR ms = monster_species)
        AND (mst IS NULL OR mst = monster_subtype)
        AND is_deleted = 0;
END;;

-- ACTORS --


DELIMITER ;;
DROP PROCEDURE IF EXISTS Query_Actors ;;
CREATE PROCEDURE Query_Actors(
        IN an VARCHAR(60),
        IN cn VARCHAR(30)
    )
    BEGIN
        SELECT *
        FROM Voice_Actors
        WHERE 1 = 1
        AND (an IS NULL OR an = actor_name)
        AND (cn IS NULL OR cn = character_name)
        AND is_deleted = 0;
END;;

-- SETTINGS --


DELIMITER ;;
DROP PROCEDURE IF EXISTS Query_Settings ;;
CREATE PROCEDURE Query_Settings(
        IN st VARCHAR(60),
        IN sp VARCHAR(20)
    )
    BEGIN
        SELECT *
        FROM Settings
        WHERE 1 = 1
        AND (st IS NULL OR st = setting_terrain)
        AND (sp IS NULL OR sp = setting_place)
        AND is_deleted = 0;
END;;

-- EPISODE --

DROP PROCEDURE IF EXISTS Query_Episodes;

DELIMITER ;;
DROP PROCEDURE IF EXISTS Query_Episodes ;;
CREATE PROCEDURE Query_Episodes(
        IN sn VARCHAR(60),
        IN s INT,
        IN t VARCHAR(60),
        IN da VARCHAR(30),
        IN rt INT,
        IN mr VARCHAR(5),
        IN m VARCHAR(30)
    )
    BEGIN
        SELECT *
        FROM Episode_Details
        WHERE 1 = 1
        AND (sn IS NULL OR sn = series_name)
        AND (s IS NULL OR s = season)
        AND (t IS NULL OR t = title)
        AND (da IS NULL OR da = date_aired)
        AND (rt IS NULL OR rt = run_time)
        AND (mr IS NULL OR mr = monster_real)
        AND (m IS NULL OR m = motive)
        AND is_deleted = 0;
END;;

-- FULL CALL --

USE scooby_doo;



DELIMITER ;;
DROP PROCEDURE IF EXISTS Query_All ;;
CREATE PROCEDURE Query_All(
        IN SeriesName VARCHAR(60),
        IN Season_ INT,
        IN Title_ VARCHAR(60),
        IN DateAired VARCHAR(30),
        IN Runtime_ INT,
        IN MonsterReal VARCHAR(5),
        IN Motive_ VARCHAR(30),
        IN SettingTerrain VARCHAR(60),
        IN SettingPlace VARCHAR(20),
        IN ActorName VARCHAR(60),
        IN CharacterName VARCHAR(30),
        IN MonsterName VARCHAR(60),
        IN MonsterGender VARCHAR(20),
        IN MonsterType VARCHAR(60),
        IN MonsterSpecies VARCHAR(60),
        IN MonsterSubtype VARCHAR(60),
        IN CulpritName VARCHAR(60),
        IN CulpritGender VARCHAR(20)
)
BEGIN
    SELECT DISTINCT *
    FROM Episode_Details AS ed
    INNER JOIN (
        SELECT *
        FROM Settings AS s
        WHERE 1 = 1
        AND (SettingTerrain IS NULL OR SettingTerrain = s.setting_terrain)
        AND (SettingPlace IS NULL OR SettingPlace = s.setting_place)
        AND s.is_deleted = 0
    ) AS Queried_Settings
        USING (setting_id)
    INNER JOIN (
        SELECT *
        FROM Episode_Monsters
        INNER JOIN (
            SELECT *
            FROM Monsters AS m
            WHERE 1 = 1
            AND (MonsterName IS NULL OR MonsterName = m.monster_name)
            AND (MonsterGender IS NULL OR MonsterGender = m.monster_gender)
            AND (MonsterType IS NULL OR MonsterType = m.monster_type)
            AND (MonsterSpecies IS NULL OR MonsterSpecies = m.monster_species)
            AND (MonsterSubtype IS NULL OR MonsterSubtype = m.monster_subtype)
            AND m.is_deleted = 0
        ) AS Queried_Monsters
            USING (monster_id)
    ) AS Queried_Episode_Monsters
        USING (episode_id)
    INNER JOIN (
        SELECT *
        FROM Episode_Actors
        INNER JOIN (
            SELECT *
            FROM Voice_Actors AS va
            WHERE 1 = 1
            AND (ActorName IS NULL OR ActorName = va.actor_name)
            AND (CharacterName IS NULL OR CharacterName = va.character_name)
            AND va.is_deleted = 0
        ) AS Queried_Actors
            USING (actor_id)
    ) AS Queried_Episode_Actors
        USING (episode_id)
    INNER JOIN (
        SELECT *
        FROM Episode_Culprits
        INNER JOIN (
            SELECT *
            FROM Culprits AS c
            WHERE 1 = 1
            AND (CulpritName IS NULL OR CulpritName = c.culprit_name)
            AND (CulpritGender IS NULL OR CulpritGender = c.culprit_gender)
            AND c.is_deleted = 0
        ) AS Queried_Culprits
            USING (culprit_id)
    ) AS Queried_Episode_Culprits
        USING (episode_id)
    WHERE 1 = 1
    AND (SeriesName IS NULL OR SeriesName = ed.series_name)
    AND (Season_ IS NULL OR Season_ = ed.season)
    AND (Title_ IS NULL OR Title_ = ed.title)
    AND (MonsterReal IS NULL OR MonsterReal = ed.monster_real)
    AND (Motive_ IS NULL OR Motive_ = ed.motive)
    AND ed.is_deleted = 0;
END;;


CALL Query_All(NULL, 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL,
    NULL, 'Male', NULL, NULL, NULL, NULL, 'NULL')