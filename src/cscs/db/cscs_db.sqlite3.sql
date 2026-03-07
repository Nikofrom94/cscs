BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "csqt_abilitycategory" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	"cs_page"	varchar(50) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_descriptorcharacteristic" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_i18ncode" (
	"name"	varchar(50) NOT NULL,
	PRIMARY KEY("name")
);
CREATE TABLE IF NOT EXISTS "csqt_i18ncountrycode" (
	"name"	varchar(50) NOT NULL,
	PRIMARY KEY("name")
);
CREATE TABLE IF NOT EXISTS "csqt_initiallink" (
	"id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_language" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_ability_categories" (
	"id"	integer NOT NULL,
	"ability_id"	bigint NOT NULL,
	"abilitycategory_id"	bigint NOT NULL,
	FOREIGN KEY("ability_id") REFERENCES "csqt_ability"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("abilitycategory_id") REFERENCES "csqt_abilitycategory"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_charactertype_abilities_tier1" (
	"id"	integer NOT NULL,
	"charactertype_id"	bigint NOT NULL,
	"ability_id"	bigint NOT NULL,
	FOREIGN KEY("charactertype_id") REFERENCES "csqt_charactertype"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("ability_id") REFERENCES "csqt_ability"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_charactertype_abilities_tier2" (
	"id"	integer NOT NULL,
	"charactertype_id"	bigint NOT NULL,
	"ability_id"	bigint NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("ability_id") REFERENCES "csqt_ability"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("charactertype_id") REFERENCES "csqt_charactertype"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_charactertype_abilities_tier3" (
	"id"	integer NOT NULL,
	"charactertype_id"	bigint NOT NULL,
	"ability_id"	bigint NOT NULL,
	FOREIGN KEY("ability_id") REFERENCES "csqt_ability"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("charactertype_id") REFERENCES "csqt_charactertype"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_charactertype_abilities_tier4" (
	"id"	integer NOT NULL,
	"charactertype_id"	bigint NOT NULL,
	"ability_id"	bigint NOT NULL,
	FOREIGN KEY("ability_id") REFERENCES "csqt_ability"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("charactertype_id") REFERENCES "csqt_charactertype"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_charactertype_abilities_tier5" (
	"id"	integer NOT NULL,
	"charactertype_id"	bigint NOT NULL,
	"ability_id"	bigint NOT NULL,
	FOREIGN KEY("charactertype_id") REFERENCES "csqt_charactertype"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("ability_id") REFERENCES "csqt_ability"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_charactertype_abilities_tier6" (
	"id"	integer NOT NULL,
	"charactertype_id"	bigint NOT NULL,
	"ability_id"	bigint NOT NULL,
	FOREIGN KEY("ability_id") REFERENCES "csqt_ability"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("charactertype_id") REFERENCES "csqt_charactertype"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_descriptor_characteristics" (
	"id"	integer NOT NULL,
	"descriptor_id"	bigint NOT NULL,
	"descriptorcharacteristic_id"	bigint NOT NULL,
	FOREIGN KEY("descriptorcharacteristic_id") REFERENCES "csqt_descriptorcharacteristic"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("descriptor_id") REFERENCES "csqt_descriptor"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_descriptor_initial_links" (
	"id"	integer NOT NULL,
	"descriptor_id"	bigint NOT NULL,
	"initiallink_id"	bigint NOT NULL,
	FOREIGN KEY("descriptor_id") REFERENCES "csqt_descriptor"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("initiallink_id") REFERENCES "csqt_initiallink"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_flavor_abilities_tier1" (
	"id"	integer NOT NULL,
	"flavor_id"	bigint NOT NULL,
	"ability_id"	bigint NOT NULL,
	FOREIGN KEY("flavor_id") REFERENCES "csqt_flavor"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("ability_id") REFERENCES "csqt_ability"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_flavor_abilities_tier2" (
	"id"	integer NOT NULL,
	"flavor_id"	bigint NOT NULL,
	"ability_id"	bigint NOT NULL,
	FOREIGN KEY("flavor_id") REFERENCES "csqt_flavor"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("ability_id") REFERENCES "csqt_ability"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_flavor_abilities_tier3" (
	"id"	integer NOT NULL,
	"flavor_id"	bigint NOT NULL,
	"ability_id"	bigint NOT NULL,
	FOREIGN KEY("flavor_id") REFERENCES "csqt_flavor"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("ability_id") REFERENCES "csqt_ability"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_flavor_abilities_tier4" (
	"id"	integer NOT NULL,
	"flavor_id"	bigint NOT NULL,
	"ability_id"	bigint NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("flavor_id") REFERENCES "csqt_flavor"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("ability_id") REFERENCES "csqt_ability"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_flavor_abilities_tier5" (
	"id"	integer NOT NULL,
	"flavor_id"	bigint NOT NULL,
	"ability_id"	bigint NOT NULL,
	FOREIGN KEY("flavor_id") REFERENCES "csqt_flavor"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("ability_id") REFERENCES "csqt_ability"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_flavor_abilities_tier6" (
	"id"	integer NOT NULL,
	"flavor_id"	bigint NOT NULL,
	"ability_id"	bigint NOT NULL,
	FOREIGN KEY("flavor_id") REFERENCES "csqt_flavor"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("ability_id") REFERENCES "csqt_ability"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_character_skills" (
	"id"	integer NOT NULL,
	"character_id"	bigint NOT NULL,
	"characterskill_id"	bigint NOT NULL,
	FOREIGN KEY("character_id") REFERENCES "csqt_character"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("characterskill_id") REFERENCES "csqt_characterskill"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_focusabilities" (
	"id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_focusabilities_abilities" (
	"id"	integer NOT NULL,
	"focusabilities_id"	bigint NOT NULL,
	"ability_id"	bigint NOT NULL,
	FOREIGN KEY("focusabilities_id") REFERENCES "csqt_focusabilities"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("ability_id") REFERENCES "csqt_ability"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_focusabilities_abilities_to_choose" (
	"id"	integer NOT NULL,
	"focusabilities_id"	bigint NOT NULL,
	"ability_id"	bigint NOT NULL,
	FOREIGN KEY("focusabilities_id") REFERENCES "csqt_focusabilities"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("ability_id") REFERENCES "csqt_ability"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_i18ncharfield50" (
	"id"	integer NOT NULL,
	"content"	varchar(50) NOT NULL,
	"code_id"	varchar(50) NOT NULL,
	"countrycode_id"	varchar(50) NOT NULL,
	FOREIGN KEY("code_id") REFERENCES "csqt_i18ncode"("name") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("countrycode_id") REFERENCES "csqt_i18ncountrycode"("name") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_i18ncharfield200" (
	"id"	integer NOT NULL,
	"content"	varchar(200) NOT NULL,
	"code_id"	varchar(50) NOT NULL,
	"countrycode_id"	varchar(50) NOT NULL,
	FOREIGN KEY("code_id") REFERENCES "csqt_i18ncode"("name") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("countrycode_id") REFERENCES "csqt_i18ncountrycode"("name") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_i18ncharfield20" (
	"id"	integer NOT NULL,
	"content"	varchar(20) NOT NULL,
	"code_id"	varchar(50) NOT NULL,
	"countrycode_id"	varchar(50) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("code_id") REFERENCES "csqt_i18ncode"("name") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("countrycode_id") REFERENCES "csqt_i18ncountrycode"("name") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_i18ntextfield" (
	"id"	integer NOT NULL,
	"content"	text NOT NULL,
	"code_id"	varchar(50) NOT NULL,
	"countrycode_id"	varchar(50) NOT NULL,
	FOREIGN KEY("code_id") REFERENCES "csqt_i18ncode"("name") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("countrycode_id") REFERENCES "csqt_i18ncountrycode"("name") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_initiallinklang" (
	"id"	integer NOT NULL,
	"description"	text NOT NULL,
	"initiallink_id"	bigint,
	"lang_id"	bigint,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("initiallink_id") REFERENCES "csqt_initiallink"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("lang_id") REFERENCES "csqt_language"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_flavorlang" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	"description"	text NOT NULL,
	"flavor_id"	bigint,
	"lang_id"	bigint,
	FOREIGN KEY("flavor_id") REFERENCES "csqt_flavor"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("lang_id") REFERENCES "csqt_language"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_descriptorcharacteristiclang" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	"description"	text NOT NULL,
	"descriptorcharacteristic_id"	bigint,
	"lang_id"	bigint,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("descriptorcharacteristic_id") REFERENCES "csqt_descriptorcharacteristic"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("lang_id") REFERENCES "csqt_language"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_charactertypelang" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	"charactertype_id"	bigint,
	"lang_id"	bigint,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("charactertype_id") REFERENCES "csqt_charactertype"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("lang_id") REFERENCES "csqt_language"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_abilitylang" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	"description"	text NOT NULL,
	"ability_id"	bigint,
	"lang_id"	bigint,
	"stat"	varchar(50),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("ability_id") REFERENCES "csqt_ability"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("lang_id") REFERENCES "csqt_language"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_setting" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	"name_en"	varchar(50) NOT NULL,
	"description"	text NOT NULL,
	"descriptor_id"	bigint,
	"focus_id"	bigint,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("focus_id") REFERENCES "csqt_focus"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("descriptor_id") REFERENCES "csqt_descriptor"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_charactertemplate" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	"name_en"	varchar(50) NOT NULL,
	"description"	text NOT NULL,
	"characterType_id"	bigint,
	"flavor_id"	bigint,
	"focus_id"	bigint,
	FOREIGN KEY("focus_id") REFERENCES "csqt_focus"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("flavor_id") REFERENCES "csqt_flavor"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("characterType_id") REFERENCES "csqt_charactertype"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_charactertemplate_settings" (
	"id"	integer NOT NULL,
	"charactertemplate_id"	bigint NOT NULL,
	"setting_id"	bigint NOT NULL,
	FOREIGN KEY("setting_id") REFERENCES "csqt_setting"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("charactertemplate_id") REFERENCES "csqt_charactertemplate"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_abilitycategorylang" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	"description"	text NOT NULL,
	"lang_id"	bigint,
	"abilitycategory_id"	bigint,
	FOREIGN KEY("lang_id") REFERENCES "csqt_language"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("abilitycategory_id") REFERENCES "csqt_abilitycategory"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_descriptorlang" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	"description"	text NOT NULL,
	"descriptor_id"	bigint,
	"lang_id"	bigint,
	FOREIGN KEY("lang_id") REFERENCES "csqt_language"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("descriptor_id") REFERENCES "csqt_descriptor"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_character_flavors" (
	"id"	integer NOT NULL,
	"character_id"	bigint NOT NULL,
	"flavor_id"	bigint NOT NULL,
	FOREIGN KEY("flavor_id") REFERENCES "csqt_flavor"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("character_id") REFERENCES "csqt_character"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_character_cyphers" (
	"id"	integer NOT NULL,
	"character_id"	bigint NOT NULL,
	"cypher_id"	bigint NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("character_id") REFERENCES "csqt_character"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("cypher_id") REFERENCES "csqt_cypher"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_cypherlang" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	"effect"	text NOT NULL,
	"hint"	text,
	"table"	text,
	"cypher_id"	bigint,
	"lang_id"	bigint,
	FOREIGN KEY("cypher_id") REFERENCES "csqt_cypher"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("lang_id") REFERENCES "csqt_language"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_character_descriptors" (
	"id"	integer NOT NULL,
	"character_id"	bigint NOT NULL,
	"descriptor_id"	bigint NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("character_id") REFERENCES "csqt_character"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("descriptor_id") REFERENCES "csqt_descriptor"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_ability" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	"cs_page"	varchar(20) NOT NULL,
	"tier"	varchar(1),
	"enabled"	bool NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_character" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	"tier"	smallint unsigned NOT NULL CHECK("tier" >= 0),
	"might"	smallint unsigned NOT NULL CHECK("might" >= 0),
	"speed"	smallint unsigned NOT NULL CHECK("speed" >= 0),
	"intellect"	smallint unsigned NOT NULL CHECK("intellect" >= 0),
	"might_edge"	smallint unsigned NOT NULL CHECK("might_edge" >= 0),
	"speed_edge"	smallint unsigned NOT NULL CHECK("speed_edge" >= 0),
	"intellect_edge"	smallint unsigned NOT NULL CHECK("intellect_edge" >= 0),
	"character_type_id"	bigint,
	"focus_id"	bigint,
	"player"	varchar(50) NOT NULL,
	"enabled"	bool NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("focus_id") REFERENCES "csqt_focus"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("character_type_id") REFERENCES "csqt_charactertype"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_charactertype" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	"might_start"	smallint unsigned NOT NULL CHECK("might_start" >= 0),
	"speed_start"	smallint unsigned NOT NULL CHECK("speed_start" >= 0),
	"intellect_start"	smallint unsigned NOT NULL CHECK("intellect_start" >= 0),
	"might_edge_start"	smallint unsigned NOT NULL CHECK("might_edge_start" >= 0),
	"speed_edge_start"	smallint unsigned NOT NULL CHECK("speed_edge_start" >= 0),
	"intellect_edge_start"	smallint unsigned NOT NULL CHECK("intellect_edge_start" >= 0),
	"cyphers_start"	smallint unsigned NOT NULL CHECK("cyphers_start" >= 0),
	"cs_page"	varchar(20) NOT NULL,
	"enabled"	bool NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_cypher" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	"level"	varchar(10) NOT NULL,
	"cs_page"	varchar(50),
	"is_manifeste"	bool NOT NULL,
	"is_fantastic"	bool NOT NULL,
	"is_subtle"	bool NOT NULL,
	"enabled"	bool NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_descriptor" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	"cs_page"	varchar(20) NOT NULL,
	"enabled"	bool NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_flavor" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	"cs_page"	varchar(20) NOT NULL,
	"enabled"	bool NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_focus" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	"abilities_tier1_id"	bigint,
	"abilities_tier2_id"	bigint,
	"abilities_tier3_id"	bigint,
	"abilities_tier4_id"	bigint,
	"abilities_tier5_id"	bigint,
	"abilities_tier6_id"	bigint,
	"cs_page"	varchar(20) NOT NULL,
	"enabled"	bool NOT NULL,
	FOREIGN KEY("abilities_tier4_id") REFERENCES "csqt_focusabilities"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("abilities_tier5_id") REFERENCES "csqt_focusabilities"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("abilities_tier6_id") REFERENCES "csqt_focusabilities"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("abilities_tier3_id") REFERENCES "csqt_focusabilities"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("abilities_tier1_id") REFERENCES "csqt_focusabilities"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("abilities_tier2_id") REFERENCES "csqt_focusabilities"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_focuslang" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	"description"	text NOT NULL,
	"focus_id"	bigint,
	"lang_id"	bigint,
	"gm_intrusion"	text NOT NULL,
	FOREIGN KEY("focus_id") REFERENCES "csqt_focus"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("lang_id") REFERENCES "csqt_language"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "csqt_skill" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	"enabled"	bool NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_charactertemplatelang" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	"charactertemplate_id"	INTEGER,
	"lang_id"	INTEGER,
	FOREIGN KEY("charactertemplate_id") REFERENCES "csqt_charactertemplate"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("lang_id") REFERENCES "csqt_language"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "csqt_characterskill" (
	"id"	integer NOT NULL,
	"level"	varchar(1) NOT NULL,
	"skill_id"	bigint,
	"name"	varchar(50) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("skill_id") REFERENCES "csqt_skill"("id")
);
CREATE TABLE IF NOT EXISTS "csqt_character_abilities" (
	"id"	integer NOT NULL,
	"character_id"	bigint NOT NULL,
	"ability_id"	bigint,
	"name"	varchar(50) NOT NULL,
	"description"	TEXT,
	"stat"	varchar(50),
	"cs_page"	varchar(20),
	"rank"	INTEGER NOT NULL,
	FOREIGN KEY("ability_id") REFERENCES "csqt_ability"("id"),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("character_id") REFERENCES "csqt_character"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
CREATE INDEX IF NOT EXISTS "csqt_abilitycategory_name_367a6d09" ON "csqt_abilitycategory" (
	"name"
);
CREATE INDEX IF NOT EXISTS "csqt_language_name_2eab5632" ON "csqt_language" (
	"name"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_ability_categories_ability_id_abilitycategory_id_9a1af578_uniq" ON "csqt_ability_categories" (
	"ability_id",
	"abilitycategory_id"
);
CREATE INDEX IF NOT EXISTS "csqt_ability_categories_ability_id_8590ca72" ON "csqt_ability_categories" (
	"ability_id"
);
CREATE INDEX IF NOT EXISTS "csqt_ability_categories_abilitycategory_id_24010f10" ON "csqt_ability_categories" (
	"abilitycategory_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_charactertype_abilities_tier1_charactertype_id_ability_id_8d0f8897_uniq" ON "csqt_charactertype_abilities_tier1" (
	"charactertype_id",
	"ability_id"
);
CREATE INDEX IF NOT EXISTS "csqt_charactertype_abilities_tier1_charactertype_id_7937c2e3" ON "csqt_charactertype_abilities_tier1" (
	"charactertype_id"
);
CREATE INDEX IF NOT EXISTS "csqt_charactertype_abilities_tier1_ability_id_57d457fa" ON "csqt_charactertype_abilities_tier1" (
	"ability_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_charactertype_abilities_tier2_charactertype_id_ability_id_b4728580_uniq" ON "csqt_charactertype_abilities_tier2" (
	"charactertype_id",
	"ability_id"
);
CREATE INDEX IF NOT EXISTS "csqt_charactertype_abilities_tier2_charactertype_id_e78f48b8" ON "csqt_charactertype_abilities_tier2" (
	"charactertype_id"
);
CREATE INDEX IF NOT EXISTS "csqt_charactertype_abilities_tier2_ability_id_e607fba8" ON "csqt_charactertype_abilities_tier2" (
	"ability_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_charactertype_abilities_tier3_charactertype_id_ability_id_6db11759_uniq" ON "csqt_charactertype_abilities_tier3" (
	"charactertype_id",
	"ability_id"
);
CREATE INDEX IF NOT EXISTS "csqt_charactertype_abilities_tier3_charactertype_id_134c1f21" ON "csqt_charactertype_abilities_tier3" (
	"charactertype_id"
);
CREATE INDEX IF NOT EXISTS "csqt_charactertype_abilities_tier3_ability_id_3879f7a4" ON "csqt_charactertype_abilities_tier3" (
	"ability_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_charactertype_abilities_tier4_charactertype_id_ability_id_55ec92ec_uniq" ON "csqt_charactertype_abilities_tier4" (
	"charactertype_id",
	"ability_id"
);
CREATE INDEX IF NOT EXISTS "csqt_charactertype_abilities_tier4_charactertype_id_710d23ff" ON "csqt_charactertype_abilities_tier4" (
	"charactertype_id"
);
CREATE INDEX IF NOT EXISTS "csqt_charactertype_abilities_tier4_ability_id_0c4d1fc7" ON "csqt_charactertype_abilities_tier4" (
	"ability_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_charactertype_abilities_tier5_charactertype_id_ability_id_21fbf5e4_uniq" ON "csqt_charactertype_abilities_tier5" (
	"charactertype_id",
	"ability_id"
);
CREATE INDEX IF NOT EXISTS "csqt_charactertype_abilities_tier5_charactertype_id_5b9e44e7" ON "csqt_charactertype_abilities_tier5" (
	"charactertype_id"
);
CREATE INDEX IF NOT EXISTS "csqt_charactertype_abilities_tier5_ability_id_f8e361e3" ON "csqt_charactertype_abilities_tier5" (
	"ability_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_charactertype_abilities_tier6_charactertype_id_ability_id_fabe8873_uniq" ON "csqt_charactertype_abilities_tier6" (
	"charactertype_id",
	"ability_id"
);
CREATE INDEX IF NOT EXISTS "csqt_charactertype_abilities_tier6_charactertype_id_355ce9bb" ON "csqt_charactertype_abilities_tier6" (
	"charactertype_id"
);
CREATE INDEX IF NOT EXISTS "csqt_charactertype_abilities_tier6_ability_id_1822556d" ON "csqt_charactertype_abilities_tier6" (
	"ability_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_descriptor_characteristics_descriptor_id_descriptorcharacteristic_id_3ab96530_uniq" ON "csqt_descriptor_characteristics" (
	"descriptor_id",
	"descriptorcharacteristic_id"
);
CREATE INDEX IF NOT EXISTS "csqt_descriptor_characteristics_descriptor_id_ffc45335" ON "csqt_descriptor_characteristics" (
	"descriptor_id"
);
CREATE INDEX IF NOT EXISTS "csqt_descriptor_characteristics_descriptorcharacteristic_id_34824184" ON "csqt_descriptor_characteristics" (
	"descriptorcharacteristic_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_descriptor_initial_links_descriptor_id_initiallink_id_a1590596_uniq" ON "csqt_descriptor_initial_links" (
	"descriptor_id",
	"initiallink_id"
);
CREATE INDEX IF NOT EXISTS "csqt_descriptor_initial_links_descriptor_id_081857c0" ON "csqt_descriptor_initial_links" (
	"descriptor_id"
);
CREATE INDEX IF NOT EXISTS "csqt_descriptor_initial_links_initiallink_id_038ed062" ON "csqt_descriptor_initial_links" (
	"initiallink_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_flavor_abilities_tier1_flavor_id_ability_id_6634f501_uniq" ON "csqt_flavor_abilities_tier1" (
	"flavor_id",
	"ability_id"
);
CREATE INDEX IF NOT EXISTS "csqt_flavor_abilities_tier1_flavor_id_d0cffce0" ON "csqt_flavor_abilities_tier1" (
	"flavor_id"
);
CREATE INDEX IF NOT EXISTS "csqt_flavor_abilities_tier1_ability_id_e5fd7852" ON "csqt_flavor_abilities_tier1" (
	"ability_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_flavor_abilities_tier2_flavor_id_ability_id_1d1d6520_uniq" ON "csqt_flavor_abilities_tier2" (
	"flavor_id",
	"ability_id"
);
CREATE INDEX IF NOT EXISTS "csqt_flavor_abilities_tier2_flavor_id_f9bd50dd" ON "csqt_flavor_abilities_tier2" (
	"flavor_id"
);
CREATE INDEX IF NOT EXISTS "csqt_flavor_abilities_tier2_ability_id_030810ce" ON "csqt_flavor_abilities_tier2" (
	"ability_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_flavor_abilities_tier3_flavor_id_ability_id_60662f16_uniq" ON "csqt_flavor_abilities_tier3" (
	"flavor_id",
	"ability_id"
);
CREATE INDEX IF NOT EXISTS "csqt_flavor_abilities_tier3_flavor_id_adfe12b0" ON "csqt_flavor_abilities_tier3" (
	"flavor_id"
);
CREATE INDEX IF NOT EXISTS "csqt_flavor_abilities_tier3_ability_id_ad20dba1" ON "csqt_flavor_abilities_tier3" (
	"ability_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_flavor_abilities_tier4_flavor_id_ability_id_90ec2997_uniq" ON "csqt_flavor_abilities_tier4" (
	"flavor_id",
	"ability_id"
);
CREATE INDEX IF NOT EXISTS "csqt_flavor_abilities_tier4_flavor_id_3f1793c7" ON "csqt_flavor_abilities_tier4" (
	"flavor_id"
);
CREATE INDEX IF NOT EXISTS "csqt_flavor_abilities_tier4_ability_id_66515cdc" ON "csqt_flavor_abilities_tier4" (
	"ability_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_flavor_abilities_tier5_flavor_id_ability_id_7706c512_uniq" ON "csqt_flavor_abilities_tier5" (
	"flavor_id",
	"ability_id"
);
CREATE INDEX IF NOT EXISTS "csqt_flavor_abilities_tier5_flavor_id_c005c203" ON "csqt_flavor_abilities_tier5" (
	"flavor_id"
);
CREATE INDEX IF NOT EXISTS "csqt_flavor_abilities_tier5_ability_id_bbd16584" ON "csqt_flavor_abilities_tier5" (
	"ability_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_flavor_abilities_tier6_flavor_id_ability_id_73f154da_uniq" ON "csqt_flavor_abilities_tier6" (
	"flavor_id",
	"ability_id"
);
CREATE INDEX IF NOT EXISTS "csqt_flavor_abilities_tier6_flavor_id_b5ef7082" ON "csqt_flavor_abilities_tier6" (
	"flavor_id"
);
CREATE INDEX IF NOT EXISTS "csqt_flavor_abilities_tier6_ability_id_6a4e0f72" ON "csqt_flavor_abilities_tier6" (
	"ability_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_character_skills_character_id_characterskill_id_54ca3f01_uniq" ON "csqt_character_skills" (
	"character_id",
	"characterskill_id"
);
CREATE INDEX IF NOT EXISTS "csqt_character_skills_character_id_38832929" ON "csqt_character_skills" (
	"character_id"
);
CREATE INDEX IF NOT EXISTS "csqt_character_skills_characterskill_id_b8a5494c" ON "csqt_character_skills" (
	"characterskill_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_focusabilities_abilities_focusabilities_id_ability_id_45a809c6_uniq" ON "csqt_focusabilities_abilities" (
	"focusabilities_id",
	"ability_id"
);
CREATE INDEX IF NOT EXISTS "csqt_focusabilities_abilities_focusabilities_id_1a99f443" ON "csqt_focusabilities_abilities" (
	"focusabilities_id"
);
CREATE INDEX IF NOT EXISTS "csqt_focusabilities_abilities_ability_id_7b6fabec" ON "csqt_focusabilities_abilities" (
	"ability_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_focusabilities_abilities_to_choose_focusabilities_id_ability_id_530d0266_uniq" ON "csqt_focusabilities_abilities_to_choose" (
	"focusabilities_id",
	"ability_id"
);
CREATE INDEX IF NOT EXISTS "csqt_focusabilities_abilities_to_choose_focusabilities_id_11fb08f8" ON "csqt_focusabilities_abilities_to_choose" (
	"focusabilities_id"
);
CREATE INDEX IF NOT EXISTS "csqt_focusabilities_abilities_to_choose_ability_id_b7999d47" ON "csqt_focusabilities_abilities_to_choose" (
	"ability_id"
);
CREATE INDEX IF NOT EXISTS "csqt_i18ncharfield50_code_id_7ba12908" ON "csqt_i18ncharfield50" (
	"code_id"
);
CREATE INDEX IF NOT EXISTS "csqt_i18ncharfield50_countrycode_id_00a0dec9" ON "csqt_i18ncharfield50" (
	"countrycode_id"
);
CREATE INDEX IF NOT EXISTS "csqt_i18ncharfield200_code_id_27c595df" ON "csqt_i18ncharfield200" (
	"code_id"
);
CREATE INDEX IF NOT EXISTS "csqt_i18ncharfield200_countrycode_id_a974a3f0" ON "csqt_i18ncharfield200" (
	"countrycode_id"
);
CREATE INDEX IF NOT EXISTS "csqt_i18ncharfield20_code_id_3f3c195d" ON "csqt_i18ncharfield20" (
	"code_id"
);
CREATE INDEX IF NOT EXISTS "csqt_i18ncharfield20_countrycode_id_7beada20" ON "csqt_i18ncharfield20" (
	"countrycode_id"
);
CREATE INDEX IF NOT EXISTS "csqt_i18ntextfield_code_id_66a0c624" ON "csqt_i18ntextfield" (
	"code_id"
);
CREATE INDEX IF NOT EXISTS "csqt_i18ntextfield_countrycode_id_a30d46a5" ON "csqt_i18ntextfield" (
	"countrycode_id"
);
CREATE INDEX IF NOT EXISTS "csqt_initiallinklang_initiallink_id_9393ad7a" ON "csqt_initiallinklang" (
	"initiallink_id"
);
CREATE INDEX IF NOT EXISTS "csqt_initiallinklang_lang_id_dc90e24f" ON "csqt_initiallinklang" (
	"lang_id"
);
CREATE INDEX IF NOT EXISTS "csqt_flavorlang_flavor_id_3058c189" ON "csqt_flavorlang" (
	"flavor_id"
);
CREATE INDEX IF NOT EXISTS "csqt_flavorlang_lang_id_2644d7ee" ON "csqt_flavorlang" (
	"lang_id"
);
CREATE INDEX IF NOT EXISTS "csqt_descriptorcharacteristiclang_descriptorcharacteristic_id_ed0f0add" ON "csqt_descriptorcharacteristiclang" (
	"descriptorcharacteristic_id"
);
CREATE INDEX IF NOT EXISTS "csqt_descriptorcharacteristiclang_lang_id_9ea60cb5" ON "csqt_descriptorcharacteristiclang" (
	"lang_id"
);
CREATE INDEX IF NOT EXISTS "csqt_charactertypelang_charactertype_id_a081e979" ON "csqt_charactertypelang" (
	"charactertype_id"
);
CREATE INDEX IF NOT EXISTS "csqt_charactertypelang_lang_id_a237bbf3" ON "csqt_charactertypelang" (
	"lang_id"
);
CREATE INDEX IF NOT EXISTS "csqt_abilitylang_name_df11e0ea" ON "csqt_abilitylang" (
	"name"
);
CREATE INDEX IF NOT EXISTS "csqt_abilitylang_ability_id_6940a27e" ON "csqt_abilitylang" (
	"ability_id"
);
CREATE INDEX IF NOT EXISTS "csqt_abilitylang_lang_id_1b97e901" ON "csqt_abilitylang" (
	"lang_id"
);
CREATE INDEX IF NOT EXISTS "csqt_setting_descriptor_id_3760022f" ON "csqt_setting" (
	"descriptor_id"
);
CREATE INDEX IF NOT EXISTS "csqt_setting_focus_id_1101bb62" ON "csqt_setting" (
	"focus_id"
);
CREATE INDEX IF NOT EXISTS "csqt_charactertemplate_characterType_id_d11ac3c9" ON "csqt_charactertemplate" (
	"characterType_id"
);
CREATE INDEX IF NOT EXISTS "csqt_charactertemplate_flavor_id_2aa67534" ON "csqt_charactertemplate" (
	"flavor_id"
);
CREATE INDEX IF NOT EXISTS "csqt_charactertemplate_focus_id_3f67d1ae" ON "csqt_charactertemplate" (
	"focus_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_charactertemplate_settings_charactertemplate_id_setting_id_5f6d87d7_uniq" ON "csqt_charactertemplate_settings" (
	"charactertemplate_id",
	"setting_id"
);
CREATE INDEX IF NOT EXISTS "csqt_charactertemplate_settings_charactertemplate_id_6d9b123a" ON "csqt_charactertemplate_settings" (
	"charactertemplate_id"
);
CREATE INDEX IF NOT EXISTS "csqt_charactertemplate_settings_setting_id_a457c144" ON "csqt_charactertemplate_settings" (
	"setting_id"
);
CREATE INDEX IF NOT EXISTS "csqt_abilitycategorylang_name_19eed14c" ON "csqt_abilitycategorylang" (
	"name"
);
CREATE INDEX IF NOT EXISTS "csqt_abilitycategorylang_lang_id_8102844f" ON "csqt_abilitycategorylang" (
	"lang_id"
);
CREATE INDEX IF NOT EXISTS "csqt_abilitycategorylang_abilitycategory_id_3d7495e5" ON "csqt_abilitycategorylang" (
	"abilitycategory_id"
);
CREATE INDEX IF NOT EXISTS "csqt_descriptorlang_descriptor_id_587439b1" ON "csqt_descriptorlang" (
	"descriptor_id"
);
CREATE INDEX IF NOT EXISTS "csqt_descriptorlang_lang_id_33f4ef0b" ON "csqt_descriptorlang" (
	"lang_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_character_flavors_character_id_flavor_id_5136aeab_uniq" ON "csqt_character_flavors" (
	"character_id",
	"flavor_id"
);
CREATE INDEX IF NOT EXISTS "csqt_character_flavors_character_id_e272302b" ON "csqt_character_flavors" (
	"character_id"
);
CREATE INDEX IF NOT EXISTS "csqt_character_flavors_flavor_id_f864ca79" ON "csqt_character_flavors" (
	"flavor_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_character_cyphers_character_id_cypher_id_f0e98dd8_uniq" ON "csqt_character_cyphers" (
	"character_id",
	"cypher_id"
);
CREATE INDEX IF NOT EXISTS "csqt_character_cyphers_character_id_d93edc54" ON "csqt_character_cyphers" (
	"character_id"
);
CREATE INDEX IF NOT EXISTS "csqt_character_cyphers_cypher_id_49920648" ON "csqt_character_cyphers" (
	"cypher_id"
);
CREATE INDEX IF NOT EXISTS "csqt_cypherlang_cypher_id_269c8466" ON "csqt_cypherlang" (
	"cypher_id"
);
CREATE INDEX IF NOT EXISTS "csqt_cypherlang_lang_id_e9a1f8b4" ON "csqt_cypherlang" (
	"lang_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_character_descriptors_character_id_descriptor_id_3f628345_uniq" ON "csqt_character_descriptors" (
	"character_id",
	"descriptor_id"
);
CREATE INDEX IF NOT EXISTS "csqt_character_descriptors_character_id_881c9c2d" ON "csqt_character_descriptors" (
	"character_id"
);
CREATE INDEX IF NOT EXISTS "csqt_character_descriptors_descriptor_id_ce857bc5" ON "csqt_character_descriptors" (
	"descriptor_id"
);
CREATE INDEX IF NOT EXISTS "csqt_ability_name_dfc8508c" ON "csqt_ability" (
	"name"
);
CREATE INDEX IF NOT EXISTS "csqt_character_character_type_id_5f1e9359" ON "csqt_character" (
	"character_type_id"
);
CREATE INDEX IF NOT EXISTS "csqt_character_focus_id_2b44a363" ON "csqt_character" (
	"focus_id"
);
CREATE INDEX IF NOT EXISTS "csqt_focus_abilities_tier1_id_30907ced" ON "csqt_focus" (
	"abilities_tier1_id"
);
CREATE INDEX IF NOT EXISTS "csqt_focus_abilities_tier2_id_b5526152" ON "csqt_focus" (
	"abilities_tier2_id"
);
CREATE INDEX IF NOT EXISTS "csqt_focus_abilities_tier3_id_4811049c" ON "csqt_focus" (
	"abilities_tier3_id"
);
CREATE INDEX IF NOT EXISTS "csqt_focus_abilities_tier4_id_93d5ec60" ON "csqt_focus" (
	"abilities_tier4_id"
);
CREATE INDEX IF NOT EXISTS "csqt_focus_abilities_tier5_id_80999d2c" ON "csqt_focus" (
	"abilities_tier5_id"
);
CREATE INDEX IF NOT EXISTS "csqt_focus_abilities_tier6_id_b555fa5d" ON "csqt_focus" (
	"abilities_tier6_id"
);
CREATE INDEX IF NOT EXISTS "csqt_focuslang_focus_id_83db3ab7" ON "csqt_focuslang" (
	"focus_id"
);
CREATE INDEX IF NOT EXISTS "csqt_focuslang_lang_id_dc47a182" ON "csqt_focuslang" (
	"lang_id"
);
CREATE INDEX IF NOT EXISTS "csqt_characterskill_skill_id_249410a1" ON "csqt_characterskill" (
	"skill_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "csqt_character_abilities_character_id_ability_id_9f94c81d_uniq" ON "csqt_character_abilities" (
	"character_id",
	"ability_id"
);
CREATE INDEX IF NOT EXISTS "csqt_character_abilities_character_id_c4e27b2d" ON "csqt_character_abilities" (
	"character_id"
);
CREATE INDEX IF NOT EXISTS "csqt_character_abilities_ability_id_21380597" ON "csqt_character_abilities" (
	"ability_id"
);
COMMIT;
