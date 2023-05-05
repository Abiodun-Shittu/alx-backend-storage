-- Write a SQL script that creates a stored procedure AddBonus
CREATE PROCEDURE AddBonus (
	IN user_id INT,
	IN project_name VARCHAR(255),
	IN score INT
) BEGIN
DECLARE project_id INT;
-- Get the project_id if the project already exists, or create it if it doesn't
SELECT id INTO project_id
FROM projects
WHERE name = project_name;
IF project_id IS NULL THEN
INSERT INTO projects (name)
VALUES (project_name);
SET project_id = LAST_INSERT_ID();
END IF;
-- Insert the new correction
INSERT INTO corrections (user_id, project_id, score)
VALUES (user_id, project_id, score);
END
