/* Importing Supply Chain Analytics files to a Database */

-- Table 3: store_restaurant --
DROP TABLE IF EXISTS store_restaurant CASCADE;
CREATE TABLE store_restaurant (
  STORE_ADDRESS1        text,
  STORE_ADDRESS2        text,
  DISTRIBUTION_REGION   text            NOT NULL,
  STORE_STATE           text            NOT NULL,
  STORE_CITY            text            NOT NULL,
  STORE_ZIP             integer         NOT NULL,
  STORE_TYPE            text            NOT NULL,
  STORE_LOYALTY_FLAG    boolean         NOT NULL,
  STORE_NUMBER          integer         PRIMARY KEY
);

COPY store_restaurant
FROM '/Users/avi/Dropbox/Users/Avi/MSc/modules/electives/Supply Chain Analytics/indi_proj/data/store_restaurant.csv'
DELIMITER ','
CSV HEADER;

-- Table 1: pos_ordersale --
DROP TABLE IF EXISTS pos_ordersale CASCADE;
CREATE TABLE pos_ordersale (
  MD5KEY_ORDERSALE      text            PRIMARY KEY,
  ChangeReceived        Decimal         NOT NULL,
  OrderNumber           integer         NOT NULL,
  TaxInclusiveAmount    Decimal         NOT NULL,
  TaxAmount             Decimal         NOT NULL,
  MealLocation          boolean         NOT NULL,
  TransactionId         integer         NOT NULL,
  StoreNumber           integer         NOT NULL        REFERENCES store_restaurant(STORE_NUMBER),
  date                  DATE            NOT NULL
);

COPY pos_ordersale
FROM '/Users/avi/Dropbox/Users/Avi/MSc/modules/electives/Supply Chain Analytics/indi_proj/data/pos_ordersale.csv'
DELIMITER ','
CSV HEADER;

-- Table 5: recipes --
DROP TABLE IF EXISTS recipes CASCADE;
CREATE TABLE recipes (
  RecipeName              text          NOT NULL,
  RecipeDescription       text          NOT NULL,
  RecipeId                integer       PRIMARY KEY
);

COPY recipes
FROM '/Users/avi/Dropbox/Users/Avi/MSc/modules/electives/Supply Chain Analytics/indi_proj/data/recipes.csv'
DELIMITER ','
CSV HEADER;

-- Table 4: menu_items --
DROP TABLE IF EXISTS menu_items CASCADE;
CREATE TABLE menu_items (
  MenuItemName            text,
  MenuItemDescription     text         NOT NULL,
  PLU                     integer      NOT NULL,
  MenuItemId              integer      PRIMARY KEY,
  RecipeId                integer      NOT NULL         REFERENCES recipes(RecipeId)
);

COPY menu_items
FROM '/Users/avi/Dropbox/Users/Avi/MSc/modules/electives/Supply Chain Analytics/indi_proj/data/menu_items.csv'
DELIMITER ','
CSV HEADER;

-- Table 2: menuitem --
DROP TABLE IF EXISTS menuitem CASCADE;
CREATE TABLE menuitem (
  MD5KEY_MENUITEM         text          PRIMARY KEY,
  MD5KEY_ORDERSALE        text          NOT NULL        REFERENCES pos_ordersale(MD5KEY_ORDERSALE),
  CategoryDescription     text          NOT NULL,
  DepartmentDescription   text          NOT NULL,
  Description             text          NOT NULL,
  StoreNumber             integer       NOT NULL,
  TaxInclusiveAmount      Decimal       NOT NULL,
  TaxAmount               Decimal       NOT NULL,
  AdjustedPrice           Decimal       NOT NULL,
  DiscountAmount          Decimal,
  Price                   Decimal,
  Quantity                integer,
  PLU                     integer,
  Id                      integer,
  date                    DATE      NOT NULL
);

COPY menuitem
FROM '/Users/avi/Dropbox/Users/Avi/MSc/modules/electives/Supply Chain Analytics/indi_proj/data/menuitem.csv'
DELIMITER ','
CSV HEADER;

-- Table 11: portion_uom_types --
DROP TABLE IF EXISTS portion_uom_types CASCADE;
CREATE TABLE portion_uom_types (
  PortionTypeDescription  text          NOT NULL,
  PortionUOMTypeId        integer       PRIMARY KEY,
  coversion_t_ounces      Decimal
);

COPY portion_uom_types
FROM '/Users/avi/Dropbox/Users/Avi/MSc/modules/electives/Supply Chain Analytics/indi_proj/data/portion_uom_types.csv'
DELIMITER ','
CSV HEADER;

-- Table 10: ingredients --
DROP TABLE IF EXISTS ingredients CASCADE;
CREATE TABLE ingredients (
  IngredientName                    text,
  IngredientShortDescription        text          NOT NULL,
  IngredientId                      integer       PRIMARY KEY,
  PortionUOMTypeId                  integer       DEFAULT NULL  REFERENCES portion_uom_types(PortionUOMTypeId)
);

COPY ingredients
FROM '/Users/avi/Dropbox/Users/Avi/MSc/modules/electives/Supply Chain Analytics/indi_proj/data/ingredients.csv'
DELIMITER ','
CSV HEADER;

-- Table 6: recipes_ingredient_assignments --
DROP TABLE IF EXISTS recipes_ingredient_assignments CASCADE;
CREATE TABLE recipes_ingredient_assignments (
  RecipeId         integer          REFERENCES recipes(RecipeId),
  IngredientId     integer          NOT NULL                          REFERENCES  ingredients(IngredientId),
  Quantity          text            NOT NULL
);

COPY recipes_ingredient_assignments
FROM '/Users/avi/Dropbox/Users/Avi/MSc/modules/electives/Supply Chain Analytics/indi_proj/data/recipe_ingredient_assignments.csv'
DELIMITER ','
CSV HEADER;

-- Table 8: sub_recipes --
DROP TABLE IF EXISTS sub_recipes CASCADE;
CREATE TABLE sub_recipes (
  SubRecipeName            text          NOT NULL,
  SubRecipeDescription     text          NOT NULL,
  SubRecipeId              integer       PRIMARY KEY
);

COPY sub_recipes
FROM '/Users/avi/Dropbox/Users/Avi/MSc/modules/electives/Supply Chain Analytics/indi_proj/data/sub_recipes.csv'
DELIMITER ','
CSV HEADER;

-- Table 9: sub_recipe_ingr_assignments --
DROP TABLE IF EXISTS sub_recipe_ingr_assignments CASCADE;
CREATE TABLE sub_recipe_ingr_assignments (
  SubRecipeId            integer              REFERENCES  sub_recipes(SubRecipeId),
  IngredientId           integer              REFERENCES  ingredients(IngredientId),
  Quantity               decimal
);

COPY sub_recipe_ingr_assignments
FROM '/Users/avi/Dropbox/Users/Avi/MSc/modules/electives/Supply Chain Analytics/indi_proj/data/sub_recipe_ingr_assignments.csv'
DELIMITER ','
CSV HEADER;

-- Table 7: recipe_sub_recipe_assignments --
DROP TABLE IF EXISTS recipe_sub_recipe_assignments CASCADE;
CREATE TABLE recipe_sub_recipe_assignments (
  RecipeId               integer              REFERENCES  recipes(RecipeId),
  SubRecipeID            integer              REFERENCES  sub_recipes(SubRecipeID),
  Factor                 decimal
);

COPY recipe_sub_recipe_assignments
FROM '/Users/avi/Dropbox/Users/Avi/MSc/modules/electives/Supply Chain Analytics/indi_proj/data/recipe_sub_recipe_assignments.csv'
DELIMITER ','
CSV HEADER;
