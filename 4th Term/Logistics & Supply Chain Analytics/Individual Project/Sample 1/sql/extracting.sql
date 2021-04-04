-- Extracting data from sca_ind Database

-- View Table:1
SELECT *
FROM pos_ordersale
LIMIT 1000;

-- View Table:2
SELECT *
FROM menuitem
LIMIT 1000;

-- View Table:3
SELECT *
FROM store_restaurant
LIMIT 10;

-- View Table:4
SELECT *
FROM menu_items
LIMIT 10;

-- View Table:5
SELECT *
FROM recipes
LIMIT 10;

-- View Table:6
SELECT *
FROM recipes_ingredient_assignments
LIMIT 10;

-- View Table:7
SELECT *
FROM recipe_sub_recipe_assignments
LIMIT 10;

-- View Table:8
SELECT *
FROM sub_recipes
LIMIT 10;

-- View Table:9
SELECT *
FROM sub_recipe_ingr_assignments
LIMIT 10;

-- View Table:10
SELECT *
FROM ingredients
WHERE ingredientname LIKE '%Lettuce%'
LIMIT 10;

-- View Table:11
SELECT *
FROM portion_uom_types


-- Separate Table

-- Recipe
DROP VIEW IF EXISTS recipe_lettuce_dd CASCADE;
CREATE VIEW recipe_lettuce_dd AS(
SELECT
  pos_ordersale.date AS Date,
  menuitem.storenumber,
  menuitem.quantity AS order_quantity,
  CAST(recipes_ingredient_assignments.quantity AS NUMERIC) AS recipe_quantity,
  recipes_ingredient_assignments.ingredientid AS recipe_in_id,
  ingredients.ingredientname AS recipe_ingredient

FROM pos_ordersale
INNER JOIN menuitem
ON pos_ordersale.md5key_ordersale = menuitem.md5key_ordersale
INNER JOIN menu_items
ON menuitem.id = menu_items.menuitemid
INNER JOIN recipes_ingredient_assignments
ON menu_items.recipeid = recipes_ingredient_assignments.recipeid
INNER JOIN ingredients
ON recipes_ingredient_assignments.ingredientid = ingredients.ingredientid
WHERE ingredients.ingredientid = 27
);

DROP VIEW IF EXISTS recipe_final CASCADE;
CREATE VIEW recipe_final AS(
SELECT date, storenumber, SUM(recipe_quantity * order_quantity) AS recipe_quanity_f
FROM recipe_lettuce_dd
GROUP BY date, storenumber
ORDER BY date
);


DROP VIEW IF EXISTS recipe_final_outlier CASCADE;
CREATE VIEW recipe_final_outlier AS(
SELECT date, storenumber, (recipe_quantity * order_quantity) AS t_recipe
FROM recipe_lettuce_dd
);

DROP VIEW IF EXISTS recipe_without_outlier CASCADE;
CREATE VIEW recipe_without_outlier AS(
SELECT date, storenumber, SUM(t_recipe) AS recipe_quanity_f
FROM recipe_final_outlier
WHERE t_recipe<= 11
GROUP BY date, storenumber
ORDER BY date
);

-- Subreciipe
DROP VIEW IF EXISTS sub_recipe_lettuce_dd CASCADE;
CREATE VIEW sub_recipe_lettuce_dd AS(
SELECT
  pos_ordersale.date AS Date,
  menuitem.storenumber,
  menuitem.quantity AS order_quantity,
  recipe_sub_recipe_assignments.factor AS sub_factor,
  sub_recipe_ingr_assignments.quantity AS sub_recipe_quantity,
  portion_uom_types.coversion_t_ounces AS to_ounces,
  sub_recipe_ingr_assignments.ingredientid AS sub_recipe_in_id,
  ingredients.ingredientshortdescription AS ingredient_name,
  portion_uom_types.portiontypedescription AS measurement

FROM pos_ordersale
INNER JOIN menuitem
ON pos_ordersale.md5key_ordersale = menuitem.md5key_ordersale
INNER JOIN menu_items
ON menuitem.id = menu_items.menuitemid
INNER JOIN recipe_sub_recipe_assignments
ON menu_items.recipeid = recipe_sub_recipe_assignments.recipeid
INNER JOIN sub_recipe_ingr_assignments
ON recipe_sub_recipe_assignments.subrecipeid = sub_recipe_ingr_assignments.subrecipeid
INNER JOIN ingredients
ON sub_recipe_ingr_assignments.ingredientid = ingredients.ingredientid
INNER JOIN portion_uom_types
ON ingredients.portionuomtypeid = portion_uom_types.portionuomtypeid
WHERE ingredients.ingredientid IN (27, 291)
);


DROP VIEW IF EXISTS sub_recipe_total CASCADE;
CREATE VIEW sub_recipe_total AS(
SELECT *, (CAST(order_quantity AS NUMERIC) * CAST(sub_recipe_quantity AS NUMERIC) * CAST(sub_factor AS NUMERIC)) AS total_lettuce_sub_recipe
FROM sub_recipe_lettuce_dd
);

DROP VIEW IF EXISTS sub_recipe_final CASCADE;
CREATE VIEW sub_recipe_final AS(
SELECT date, storenumber, SUM(total_lettuce_sub_recipe) AS lettuce_total
FROM sub_recipe_total
GROUP BY date, storenumber
ORDER BY date
);

DROP VIEW IF EXISTS sub_recipe_without_outlier CASCADE;
CREATE VIEW sub_recipe_without_outlier AS(
SELECT date, storenumber, SUM(total_lettuce_sub_recipe) AS lettuce_total
FROM sub_recipe_total
WHERE total_lettuce_sub_recipe<= 18
GROUP BY date, storenumber
ORDER BY date
);





-- Creating Tables

DROP TABLE IF EXISTS results CASCADE;
CREATE TABLE results AS (
SELECT DATE(sub_recipe_final.date), sub_recipe_final.storenumber, CAST((CAST(lettuce_total AS NUMERIC) + coalesce(CAST(recipe_quanity_f AS NUMERIC), 0)) AS INTEGER) AS total_lettuce
FROM sub_recipe_final
LEFT JOIN recipe_final
ON  sub_recipe_final.storenumber = recipe_final.storenumber AND sub_recipe_final.date = recipe_final.date
ORDER BY date
);


DROP TABLE IF EXISTS sub_transactions CASCADE;
CREATE TABLE sub_transactions AS (
SELECT DATE(sub_recipe_lettuce_dd.date), sub_recipe_lettuce_dd.storenumber, CAST(CAST(sub_recipe_lettuce_dd.order_quantity AS NUMERIC) * CAST(sub_recipe_lettuce_dd.sub_recipe_quantity AS NUMERIC) * CAST(sub_recipe_lettuce_dd.sub_factor AS NUMERIC) AS NUMERIC) AS total_lettuce_trans_sub
FROM sub_recipe_lettuce_dd
ORDER BY sub_recipe_lettuce_dd.date, sub_recipe_lettuce_dd.storenumber
);

COPY sub_transactions TO '/Users/avi/Dropbox/Users/Avi/MSc/modules/electives/Supply Chain Analytics/indi_proj/results/sub_transactions.csv' DELIMITER ',' CSV HEADER;


DROP TABLE IF EXISTS rep_transactions CASCADE;
CREATE TABLE rep_transactions AS (
SELECT DATE(recipe_lettuce_dd.date), recipe_lettuce_dd.storenumber, CAST(coalesce(CAST(recipe_lettuce_dd.recipe_quantity * recipe_lettuce_dd.order_quantity AS NUMERIC), 0) AS INTEGER) AS total_lettuce_trans_rep
FROM recipe_lettuce_dd
ORDER BY recipe_lettuce_dd.date, recipe_lettuce_dd.storenumber
);

COPY rep_transactions TO '/Users/avi/Dropbox/Users/Avi/MSc/modules/electives/Supply Chain Analytics/indi_proj/results/rep_transactions.csv' DELIMITER ',' CSV HEADER;


-- Creating 12631 Table
DROP TABLE IF EXISTS results_12631 CASCADE;
CREATE TABLE results_12631 AS (
SELECT DATE(sub_recipe_final.date), CAST((CAST(lettuce_total AS NUMERIC) + coalesce(CAST(recipe_quanity_f AS NUMERIC), 0)) AS INTEGER) AS total_lettuce
FROM sub_recipe_final
LEFT JOIN recipe_final
ON  sub_recipe_final.storenumber = recipe_final.storenumber AND sub_recipe_final.date = recipe_final.date
WHERE sub_recipe_final.storenumber = 12631
ORDER BY date
);

COPY results_12631 TO '/Users/avi/Dropbox/Users/Avi/MSc/modules/electives/Supply Chain Analytics/indi_proj/results/12631.csv' DELIMITER ',' CSV HEADER;

-- Creating 12631 Table without outlier
DROP TABLE IF EXISTS results_12631_wo CASCADE;
CREATE TABLE results_12631_wo AS (
SELECT DATE(sub_recipe_without_outlier.date), CAST((CAST(lettuce_total AS NUMERIC) + coalesce(CAST(recipe_quanity_f AS NUMERIC), 0)) AS INTEGER) AS total_lettuce
FROM sub_recipe_without_outlier
LEFT JOIN recipe_without_outlier
ON  sub_recipe_without_outlier.storenumber = recipe_without_outlier.storenumber AND sub_recipe_without_outlier.date = recipe_without_outlier.date
WHERE sub_recipe_without_outlier.storenumber = 12631
ORDER BY date
);

COPY results_12631_wo TO '/Users/avi/Dropbox/Users/Avi/MSc/modules/electives/Supply Chain Analytics/indi_proj/results/12631_wo.csv' DELIMITER ',' CSV HEADER;



-- Creating 46673 Table
DROP TABLE IF EXISTS results_46673 CASCADE;
CREATE TABLE results_46673 AS (
SELECT DATE(sub_recipe_final.date), CAST((CAST(lettuce_total AS NUMERIC) + coalesce(CAST(recipe_quanity_f AS NUMERIC), 0)) AS INTEGER) AS total_lettuce
FROM sub_recipe_final
LEFT JOIN recipe_final
ON  sub_recipe_final.storenumber = recipe_final.storenumber AND sub_recipe_final.date = recipe_final.date
WHERE sub_recipe_final.storenumber = 46673
ORDER BY date
);

COPY results_46673 TO '/Users/avi/Dropbox/Users/Avi/MSc/modules/electives/Supply Chain Analytics/indi_proj/results/46673.csv' DELIMITER ',' CSV HEADER;


-- Creating 46673 Table without outlier
DROP TABLE IF EXISTS results_46673_wo CASCADE;
CREATE TABLE results_46673_wo AS (
SELECT DATE(sub_recipe_without_outlier.date), CAST((CAST(lettuce_total AS NUMERIC) + coalesce(CAST(recipe_quanity_f AS NUMERIC), 0)) AS INTEGER) AS total_lettuce
FROM sub_recipe_without_outlier
LEFT JOIN recipe_without_outlier
ON  sub_recipe_without_outlier.storenumber = recipe_without_outlier.storenumber AND sub_recipe_without_outlier.date = recipe_without_outlier.date
WHERE sub_recipe_without_outlier.storenumber = 46673
ORDER BY date
);

COPY results_46673_wo TO '/Users/avi/Dropbox/Users/Avi/MSc/modules/electives/Supply Chain Analytics/indi_proj/results/46673_wo.csv' DELIMITER ',' CSV HEADER;


-- Creating 20974 Table
DROP TABLE IF EXISTS results_20974 CASCADE;
CREATE TABLE results_20974 AS (
SELECT DATE(sub_recipe_final.date), CAST((CAST(lettuce_total AS NUMERIC) + coalesce(CAST(recipe_quanity_f AS NUMERIC), 0)) AS INTEGER) AS total_lettuce
FROM sub_recipe_final
LEFT JOIN recipe_final
ON  sub_recipe_final.storenumber = recipe_final.storenumber AND sub_recipe_final.date = recipe_final.date
WHERE sub_recipe_final.storenumber = 20974
ORDER BY date
);

COPY results_20974 TO '/Users/avi/Dropbox/Users/Avi/MSc/modules/electives/Supply Chain Analytics/indi_proj/results/20974.csv' DELIMITER ',' CSV HEADER;


-- Creating 20974 Table without outlier
DROP TABLE IF EXISTS results_20974_wo CASCADE;
CREATE TABLE results_20974_wo AS (
SELECT DATE(sub_recipe_without_outlier.date), CAST((CAST(lettuce_total AS NUMERIC) + coalesce(CAST(recipe_quanity_f AS NUMERIC), 0)) AS INTEGER) AS total_lettuce
FROM sub_recipe_without_outlier
LEFT JOIN recipe_without_outlier
ON  sub_recipe_without_outlier.storenumber = recipe_without_outlier.storenumber AND sub_recipe_without_outlier.date = recipe_without_outlier.date
WHERE sub_recipe_without_outlier.storenumber = 20974
ORDER BY date
);

COPY results_20974_wo TO '/Users/avi/Dropbox/Users/Avi/MSc/modules/electives/Supply Chain Analytics/indi_proj/results/20974_wo.csv' DELIMITER ',' CSV HEADER;


-- Creating 4904 Table
DROP TABLE IF EXISTS results_4904 CASCADE;
CREATE TABLE results_4904 AS (
SELECT DATE(sub_recipe_final.date), CAST((CAST(lettuce_total AS NUMERIC) + coalesce(CAST(recipe_quanity_f AS NUMERIC), 0)) AS INTEGER) AS total_lettuce
FROM sub_recipe_final
LEFT JOIN recipe_final
ON  sub_recipe_final.storenumber = recipe_final.storenumber AND sub_recipe_final.date = recipe_final.date
WHERE sub_recipe_final.storenumber = 4904
ORDER BY date
);

COPY results_4904 TO '/Users/avi/Dropbox/Users/Avi/MSc/modules/electives/Supply Chain Analytics/indi_proj/results/4904.csv' DELIMITER ',' CSV HEADER;


-- Creating 4904 Table without outlier
DROP TABLE IF EXISTS results_4904_wo CASCADE;
CREATE TABLE results_4904_wo AS (
SELECT DATE(sub_recipe_without_outlier.date), CAST((CAST(lettuce_total AS NUMERIC) + coalesce(CAST(recipe_quanity_f AS NUMERIC), 0)) AS INTEGER) AS total_lettuce
FROM sub_recipe_without_outlier
LEFT JOIN recipe_without_outlier
ON  sub_recipe_without_outlier.storenumber = recipe_without_outlier.storenumber AND sub_recipe_without_outlier.date = recipe_without_outlier.date
WHERE sub_recipe_without_outlier.storenumber = 4904
ORDER BY date
);

COPY results_4904_wo TO '/Users/avi/Dropbox/Users/Avi/MSc/modules/electives/Supply Chain Analytics/indi_proj/results/4904_wo.csv' DELIMITER ',' CSV HEADER;
