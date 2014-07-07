DROP TABLE IF EXISTS "formula";
CREATE TABLE "formula" ("id" TEXT NOT NULL , "name" TEXT NOT NULL , "formula" TEXT NOT NULL , "skin_type" TEXT NOT NULL , "formula_type" text not null , "sub_formula_type" text not null );
INSERT INTO "formula" VALUES('horse_oil_soap','经典马油皂','橄榄油，麻油','dry_skin', '');

DROP TABLE IF EXISTS "formula_type";
CREATE TABLE "formula_type" ("id" TEXT PRIMARY KEY  NOT NULL  UNIQUE , "name" TEXT NOT NULL );
INSERT INTO "formula_type" VALUES('operation','操作难度');
INSERT INTO "formula_type" VALUES('function','功能');
INSERT INTO "formula_type" VALUES('efficacy','功效');
INSERT INTO "formula_type" VALUES('skin','肤质');

DROP TABLE IF EXISTS "sub_formula_type";
CREATE TABLE "sub_formula_type" ("id" TEXT NOT NULL , "parent_id" TEXT NOT NULL , "name" TEXT NOT NULL , "description" TEXT NOT NULL );

DROP TABLE IF EXISTS "skin_type";
CREATE TABLE skin_type ("id" TEXT NOT NULL, "name" TEXT NOT NULL , "description" TEXT NOT NULL );
INSERT INTO skin_type VALUES("normal_skin", "中性皮肤", "健康理想的皮肤，多见于青春发育期前的少女，皮脂分泌量适中，皮肤既不干也不油，皮肤细腻，富不弹性，毛孔细小，对外界刺激不敏感。中性皮肤的PH值为5~5.6之间。");
INSERT INTO skin_type VALUES("dry_skin", "干性皮肤", "皮肤白皙，毛孔细小而不明显。皮脂分泌量少，皮肤比较干燥，容易生细小皱纹。毛细血管表浅，易破裂，对外界刺激比较敏感。干性皮肤可分缺水和缺油两种。缺水干性皮肤多见于35岁以上及老年人。缺油干性皮肤多见于年轻人。（但有部分年轻人的皮肤也会呈现缺水现象，特别是在空调下的人）干性皮肤的PH值为4.5~5之间。");
INSERT INTO skin_type VALUES("oily_skin", "油性皮肤", "肤色较深，毛孔粗大，皮脂分泌量多，皮肤油腻光亮，不容易起皱纹，对外界刺激不敏感。由于皮脂分泌过多，容易生粉刺、痤疮，常见于青春发育期年轻人。油性皮肤的PH值为5.6~6.6之间。");
INSERT INTO skin_type VALUES("mixed_skin", "混合性皮肤", "混合性皮肤兼有油性皮肤和干性皮肤的特征。在面部T区（前额、鼻、下巴）呈油性状态，眼部及两颊呈干性状态。混合性皮肤多见于25~35岁年龄的人。");
INSERT INTO skin_type VALUES("sensitive_skin", "敏感性皮肤", "皮肤较薄，对外界刺激很敏感。当受到外界刺激时，会出现局部发红、红肿、丘疹水疱及刺氧等症状。");




http://www.360doc.com/content/11/0304/16/1136134_98101755.shtml