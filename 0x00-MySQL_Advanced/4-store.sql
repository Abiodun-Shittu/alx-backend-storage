-- Write a SQL script that creates a trigger
CREATE TRIGGER IF NOT EXISTS decrease_quantity
AFTER
INSERT ON orders FOR EACH ROW BEGIN
UPDATE items
SET quantity = quantity - NEW.quantity
WHERE name = NEW.item_name;
END;
