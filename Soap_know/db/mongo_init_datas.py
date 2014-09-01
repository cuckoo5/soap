#coding=utf-8

from pymongo import MongoClient

import db_config as config
#auth start
tb_user = 'user'
tb_user_base = 'user_base'
#auth end
tb_formula_type = 'formula_type'
tb_skin_type = 'skin_type'
tb_oil = 'oil'
tb_essential_oil = 'essential_oil'
tb_essential_oil_usage = 'essential_oil_usage'

tables = {
    tb_user : [
        {'user_id' : 1, 'name' : 'admin', 'password' : '', 'email' : 'cuckoo5@sina.cn', 'create_date' : '', 'last_login_date' : None, 'online_status' : 0}
    ],
    tb_user_base : [
        {'user_id' : 1, }
    ],
    tb_formula_type : [
        {'name' : '操作难度'}, {'name' : '功能'}, {'name' : '功效'}, {'name' : '适合肤质'}
    ],
    tb_skin_type : [
        {'name' : '干性皮肤', 'description' : '皮肤白皙，毛孔细小而不明显。皮脂分泌量少，皮肤比较干燥，容易生细小皱纹。毛细血管表浅，易破裂，对外界刺激比较敏感。干性皮肤可分缺水和缺油两种。缺水干性皮肤多见于35岁以上及老年人。缺油干性皮肤多见于年轻人。（但有部分年轻人的皮肤也会呈现缺水现象，特别是在空调下的人）干性皮肤的PH值为4.5~5之间。'},
        {'name' : '中性皮肤', 'description' : '健康理想的皮肤，多见于青春发育期前的少女，皮脂分泌量适中，皮肤既不干也不油，皮肤细腻，富不弹性，毛孔细小，对外界刺激不敏感。中性皮肤的PH值为5~5.6之间。'},
        {'name' : '油性皮肤', 'description' : '肤色较深，毛孔粗大，皮脂分泌量多，皮肤油腻光亮，不容易起皱纹，对外界刺激不敏感。由于皮脂分泌过多，容易生粉刺、痤疮，常见于青春发育期年轻人。油性皮肤的PH值为5.6~6.6之间。'},
        {'name' : '混合性皮肤', 'description' : '混合性皮肤兼有油性皮肤和干性皮肤的特征。在面部T区（前额、鼻、下巴）呈油性状态，眼部及两颊呈干性状态。混合性皮肤多见于25~35岁年龄的人。'},
        {'name' : '敏感性皮肤', 'description' : '皮肤较薄，对外界刺激很敏感。当受到外界刺激时，会出现局部发红、红肿、丘疹水疱及刺氧等症状。'}
    ],
    #精油：中文名称、英文名称、萃取部位、挥发度、气味、皮肤方面、身体方面、心灵与情绪、生活中的应用方式、注意事项
    tb_essential_oil : [
       {'name' : '罗勒', 'name_en' : 'Basil', 'extraction_part' : '花的顶端、叶', 'volatility' : '高', 'smell' : '非常清甜，略带香辛料的味道。', 'for_skin' : '对下垂、阻塞的皮肤有紧实的作用并清洁毛孔闭塞或底层循环不洁皮肤。', 'for_body' : '缓解头疼和改善偏头痛的一级品，改善耳痛。改善因压力而造成的过敏现象。改善喉部不适，咳嗽、伤风、气喘、百曰咳及流行性感冒。助消化不良、打嗝等消化异常也很有效。缓解经前所引致的不适，如月经量过少、乳房胀痛等。舒解痛风和肌肉疼痛。', 'for_emotion' : '令头脑清醒，加强记忆，令精神集中，消除沮丧。', 'for_life' : '蒸薰、吸入、浸浴、按摩、涂抹。', 'notice' : '怀孕初期尤其要低剂量使用，因对皮肤可能会有刺激感，所以用量不宜过高。'},
       {'name' : '月桂', 'name_en' : 'Bay', 'extraction_part' : '叶', 'volatility' : '高', 'smell' : '甜甜的香料味，有点像肉桂。', 'for_skin' : '对粉刺、青春痘的皮肤，能帮助消炎、愈合伤口；能促进毛发生长去头皮屑。', 'for_body' : '改善扭伤、风湿痛的现象。帮助开胃、消胀气，安抚胃痛。对女性有助益，能调节月经量过少。调节体温，促进排汗、使身体舒适。', 'for_emotion' : '放松紧绷心情，平静缓和心灵，让人精神愉快，提高工作效率。', 'for_life' : '吸入、沐浴、热敷。', 'notice' : '会刺激皮肤，因此敏感性肌肤须低剂量使用：为免对孕妇造成不适，孕妇在怀孕前5个月禁用。'},
       {'name' : '安息香', 'name_en' : 'Benzoin', 'extraction_part' : '树脂', 'volatility' : '低', 'smell' : '甜，似香草。', 'for_skin' : '有益于龟裂、干燥皮肤，使皮肤恢复弹性并改善皮肤发红、发痒。', 'for_body' : '缓解一般的疼痛及关节炎。帮助消化，对胃部有安抚作用，可排除胀气。润肺并改善气喘、咳嗽、感冒、喉炎。', 'for_emotion' : '舒缓紧张与压力，安抚悲伤和沮丧的情绪。', 'for_life' : '按摩、蒸薰、沐浴、冷（热）敷、坐浴、涂抹。', 'notice' : '需集中注意力时避免使用，否则会分散注意力。'},
       {'name' : '佛手柑', 'name_en' : 'Bergamot', 'extraction_part' : '果皮', 'volatility' : '高', 'smell' : '清新，有些类似橙和柠檬，又还点花香。', 'for_skin' : '深层清洁油性皮肤及暗疮皮肤，平衡油脂分泌，收紧肌肤。', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '黑胡椒', 'name_en' : 'Blackperpper', 'extraction_part' : '果实', 'volatility' : '中', 'smell' : '非常强烈的辛味。', 'for_skin' : '有益于消退瘀血', 'for_body' : '帮助排气，强力改善肠胃的问题，促进食欲。消除多余的脂肪，促进血液循环，使身体温暖。舒缓因感冒所引起的头痛、肌肉酸痛、疲累四肢和肌肉紧绷很有帮助。', 'for_emotion' : '净化心灵，舒解压力，赋予活力。', 'for_life' : '蒸薰、按摩、涂抹、浸浴。', 'notice' : '使用不宜过频繁或过量，否则会伤害肾脏，对皮肤也会有刺激感。'},
       {'name' : '胡萝卜籽', 'name_en' : 'CarrotSeed', 'extraction_part' : '果实', 'volatility' : '中', 'smell' : '略甜而干燥的味道。', 'for_skin' : '调理敏感脆弱的肌肤，活化肌肤，防止皱纹产生，淡化老人斑改善皮肤发炎的伤口促进伤口结疤。', 'for_body' : '消除胀气、增进食欲。有调理荷尔蒙的功效，助受孕。极佳的身体净化油，减少体内废物垢囤积。有助改善流行性感冒，支气管炎。调理敏感脆弱的肌肤，活化肌肤，防止皱纹产生，淡化老人斑，改善皮肤发炎的伤口，促进伤口结疤。', 'for_emotion' : '净化心灵，舒解压力，赋予活力。', 'for_life' : '按摩、沐浴、冷（热）敷。', 'notice' : '使用不宜过频繁或过量，否则会伤害肾脏，对皮肤也会有刺激感。'},
       {'name' : '雪松', 'name_en' : 'Cedarwood', 'extraction_part' : '木材', 'volatility' : '低', 'smell' : '木质香，有点像檀香的味道。', 'for_skin' : '调理油性皮肤，收敛毛孔，清除面皰和暗疮皮肤；改善油性发质，减少头皮屑。', 'for_body' : '改善失眠。改善体内多余的橘皮组织。疏散感染、放松紧张的肌肉。', 'for_emotion' : '有助于冥想沉思，安抚精神紧张和焦虑，鼓舞沮丧的内心。', 'for_life' : '按摩、沐浴、蒸薰法、浸浴、做成保养品。', 'notice' : '可能对孕妇造成不适，孕妇禁用。'},
       {'name' : '洋甘菊', 'name_en' : 'Chamomile', 'extraction_part' : '花朵', 'volatility' : '中', 'smell' : '似苹果的气味。', 'for_skin' : '舒缓脆弱的敏感皮肤，加强皮肤的吸收能力，适用于干燥皮肤、微细血管破裂及暗疮发炎皮肤。', 'for_body' : '帮助改善失眠现象。舒缓生理痛及更年期所引致的不适。缓解肌肉疼痛、头痛、偏头痛、神经痛、牙痛。', 'for_emotion' : '绝佳的安抚效果抚平情绪，使人感觉祥和。', 'for_life' : '蒸薰、按摩、沐浴、冷（热）敷。', 'notice' : '具通经作用，孕妇禁用。'},
       {'name' : '快乐鼠尾草', 'name_en' : 'Clarysage', 'extraction_part' : '开花的顶端和叶', 'volatility' : '高－中', 'smell' : '药草气息，又带点坚果香。', 'for_skin' : '适用于发炎及红肿的皮肤，收敛毛孔，并能促进细胞再生；有利于毛发生长，改善头皮皮脂过多的分泌。', 'for_body' : '舒缓胀痛、胃部不适。是子宫有益的补品，平衡荷尔蒙。助产、并可安抚产后忧郁的情绪。改善因压力引起的偏头痛，并放松紧张的肌肉。', 'for_emotion' : '平衡神经紧张，极佳的振奋剂，可以缓解紧张、惊慌失措的状态。', 'for_life' : '蒸薰、淋浴、按摩、做成保养品。', 'notice' : '镇静效果强烈，孕妇禁用，在开车前及饮洒后不能使用，否则会影响注意力难以集中，造成反胃及头痛不舒服。'},
       {'name' : '丝柏', 'name_en' : 'Cypress', 'extraction_part' : '叶或毬果', 'volatility' : '中－低', 'smell' : '木头香，清澈而振奋。', 'for_skin' : '收紧毛孔及调理成熟肌肤，收紧眼袋，改善敏感脆弱的皮肤；促进伤口结疤。', 'for_body' : '改善体内多余的橘皮脂及水肿。有助改善静脉曲张和痔疮。平衡荷尔蒙，舒缓经痛，可调理卵巢功能。能改善流感引致的咳嗽，支气管炎。', 'for_emotion' : '平静情绪松弛紧张，净化心灵。', 'for_life' : '蒸薰、吸入、浸浴、足浴、涂抹、喷雾。', 'notice' : '具通经作用，孕妇禁用。'},
       {'name' : '尤加利', 'name_en' : 'Eucalyptus', 'extraction_part' : '叶', 'volatility' : '高', 'smell' : '澄清、略冲鼻、有穿透力。', 'for_skin' : '改善阻塞的皮肤，平衡皮脂分泌，特别能滋养肌肤。', 'for_body' : '去除体内异味。缓解神经痛、偏头痛、喉咙痛。缓解感冒，对发烧、肌肉酸痛很有帮助', 'for_emotion' : '可使头脑清醒，集中注意力，舒缓疲累感。', 'for_life' : '吸入、蒸薰、浸浴、涂抹、按摩。', 'notice' : '一种强效的精油，高血压，癫痫人士，婴儿避免使用。'},
       {'name' : '茴香', 'name_en' : 'Fennel', 'extraction_part' : '种子', 'volatility' : '高－中', 'smell' : '花香、草味、稍带香辛料。', 'for_skin' : '肌肤净化油，能疏通阻塞的毛孔，对皮肤有良好的滋养防皱效果。', 'for_body' : '改善胀气、胃部不适、促进消化。绝佳的身体净化油，并改善体内多余的橘皮脂肪。缓解经前引致的月经不适，如流量少，更年期等。', 'for_emotion' : '镇定情绪，顿时可给予力量和勇气。', 'for_life' : '按摩、浸浴、冷（热）敷、涂抹。', 'notice' : '一种强效的清油，使用过量，会引发毒性，导致皮肤敏感，让人昏昏沉沉，'},
       {'name' : '乳香', 'name_en' : 'Frankingcense', 'extraction_part' : '树皮', 'volatility' : '低－中', 'smell' : '带木香及香料味，甚至有一点柠檬的味道。', 'for_skin' : '对老化肌肤起收紧防皱、抚平皱纹并增加皮肤弹性，平衡油性皮肤，促进伤口愈合。', 'for_body' : '子宫的补药。改善喉咙痛、咳嗽。促进均衡，有镇定及安抚作用。能改善月经不顺等常见困扰现象。帮助消化，改善消化不良和打嗝。', 'for_emotion' : '赋予希望使心情好转，平静不安的情绪。', 'for_life' : '蒸薰、吸入、浸浴、涂抹、按摩。', 'notice' : '在使用上没有特殊的禁忌。'},
       {'name' : '天竺葵', 'name_en' : 'Geranium', 'extraction_part' : '花和叶', 'volatility' : '中', 'smell' : '甜而略重，有点像玫瑰。', 'for_skin' : '可以平衡皮脂腺分泌，适合各种肤质。更有良好的清洁作用，对松弛、毛孔阻塞及油性皮肤良好的效果。', 'for_body' : '改善水肿现象，帮助伤口愈合。能舒缓喉咙痛及肠胃的不舒服。增强免疫力；消除各种疼痛引起致的不适。舒缓经痛，对经前所产生的不适十分有帮助。', 'for_emotion' : '营造友善的气氛，令人心情愉快，平衡情绪。', 'for_life' : '蒸薰、浸浴、按摩、涂抹。', 'notice' : '因能调节荷尔蒙，所以孕妇避免使用；而对某些敏感皮肤，可能有刺激性宜剂量使用。'},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '','for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''},
       {'name' : '', 'name_en' : '', 'extraction_part' : '', 'volatility' : '', 'smell' : '', 'for_skin' : '', 'for_body' : '', 'for_emotion' : '', 'for_life' : '', 'notice' : ''}
    ],
    
    #竟有使用方法：精油名称、功效、方式、配方、使用方法
    tb_essential_oil_usage : [
        {'essential_oil_name' : 'Basil', 'efficasy' : '帮助冥想并消除身心疲劳', 'use_pattern' : '蒸薰', 'formula' : '罗勒1滴，檀香1滴，迷迭香3滴。', 'operation' : '只须在香薰炉上方的盛水皿中加八分满热水，在香薰炉台底部点燃蜡烛加温或插电，再依配方添加精油即可。'},
        {'essential_oil_name' : 'Bay', 'efficasy' : '舒缓头痛', 'use_pattern' : '蒸薰', 'formula' : '月桂1滴，薰衣草3滴。', 'operation' : '只须在香薰炉上方的盛水皿中加八分满热水，在香薰炉台底部点燃蜡烛加温或插电，再依配方添加精油即可。'},
        {'essential_oil_name' : 'Bay', 'efficasy' : '缓解风湿痛', 'use_pattern' : '热敷', 'formula' : '月桂2滴、玫瑰1滴、杜松1滴。', 'operation' : '将精油滴在一盆热水中，将精油混和并浸入毛巾吸取油份，稍微拧干，直接敷在疼痛的关节上。（如：膝关节、肘关节、肩膀等关节）'},
        {'essential_oil_name' : 'Benzoin', 'efficasy' : '改善脸部、手背的黑斑', 'use_pattern' : '涂抹', 'formula' : '安息香4滴，柠檬2滴，小麦胚芽油2滴，甜杏仁油12ml。', 'operation' : '将精油调匀后，取适量涂抹于脸部或手背的皮肤轻按至吸收即可。（为免影晌使用效果，经稀释后的精油须在两周内使用完。）'},
        {'essential_oil_name' : 'Benzoin', 'efficasy' : '舒缓感冒', 'use_pattern' : '蒸薰', 'formula' : '安息香5滴，一碗热水。', 'operation' : '将精油滴入一碗热水中，然后嗅蒸出来的热气即可。'},
        {'essential_oil_name' : 'Bergamot', 'efficasy' : '缓解腹痛、腹泻', 'use_pattern' : '按摩', 'formula' : '佛手柑2滴，甜杏仁5ml。', 'operation' : '将精油调匀后取适量以顺时针上的方向在腹部，轻柔打圈2-3分钟即可。（为免影响使用效果，按摩后6小时内不宜洗澡及稀释后的精油须在两周内使用完。）'},
        {'essential_oil_name' : 'Bergamot', 'efficasy' : '空气清新剂', 'use_pattern' : '喷雾', 'formula' : '佛手柑、薄荷、茴香各2滴，30ml矿泉水一瓶。', 'operation' : '将精油滴入矿泉水中，在每次使用前请先摇匀，然后喷洒于室内，使芳香气味飘散即可。'},
        {'essential_oil_name' : 'Blackperpper', 'efficasy' : '帮助消化', 'use_pattern' : '按摩', 'formula' : '黑胡椒3滴，迷迭香2滴，甜杏仁油10ml。', 'operation' : '将精油调匀后，取适量以顺时针方向按摩腹部，轻柔打圈2-3分钟即可。（为免影响使用效果，按摩后6小时内不宜洗澡及稀释后的精油须在两周内使用完。）'},
        {'essential_oil_name' : 'Cedarwood', 'efficasy' : '改善湿疹，皮肤轻微发炎', 'use_pattern' : '涂抹', 'formula' : '雪松4滴，小麦胚芽油2滴,杏仁油10ml。', 'operation' : '将精油调匀后，取适量涂抹于患处至吸收即可。'},
        {'essential_oil_name' : 'Cedarwood', 'efficasy' : '清爽发质', 'use_pattern' : '洗发', 'formula' : '雪松2滴，无香精洗发乳约5ml。', 'operation' : '将精油与洗发乳调匀后，依照一般程序洗发即可。'},
        {'essential_oil_name' : 'Chamomile', 'efficasy' : '改善过敏、暗疮等各种问题', 'use_pattern' : '涂抹', 'formula' : '洋甘菊5滴，荷荷芭油15ml', 'operation' : '将精油与荷荷油混合后，装入小玻璃瓶中，需要的时候涂抹即可。（为免影响使用效果，经稀释后的精油须在两周内使用完。）'},
        {'essential_oil_name' : 'Clarysage', 'efficasy' : '预防掉发', 'use_pattern' : '做成保养品', 'formula' : '快乐鼠尾草2滴，薰衣草5滴，迷迭香3滴。', 'operation' : '头发洗净后，将精油滴入一盆温热水中，然后浸泡头发2-3分钟即可，无需冲洗。'},
        {'essential_oil_name' : 'Clarysage', 'efficasy' : '缓和生理痛', 'use_pattern' : '淋浴', 'formula' : '快乐鼠尾草2滴，马郁兰2滴。', 'operation' : '浴缸中注入温热水，将精油滴入后调匀。将身体冲净后，再用勺子一勺勺将缸里的水冲在身上及腹部即可。'},
        {'essential_oil_name' : 'Cypress', 'efficasy' : '增加皮肤弹性', 'use_pattern' : '涂抹', 'formula' : '丝柏2滴，荷荷芭油5ml。', 'operation' : '将丝柏精油与荷荷芭油混合，取适量涂抹脸部轻按至吸收即可。（为免影响使用效果，经稀释后的精油须在两周内使用完。）'},
        {'essential_oil_name' : 'Cypress', 'efficasy' : '驱虫止臭', 'use_pattern' : '喷雾', 'formula' : '丝柏2滴，佛手柑2滴，桔子2滴，酒精10ml（浓度为75％），蒸馏水20ml。', 'operation' : '将精油与酒精、水装入喷瓶中，混合均匀后在家中，防止蚊虫。'},
        {'essential_oil_name' : 'Eucalyptus', 'efficasy' : '缓解感冒所带来的不适感', 'use_pattern' : '按摩', 'formula' : '尤加利2滴，柠檬3滴，茶树1滴，甜杏仁油12ml。', 'operation' : '将精油调匀后，取适量按摩于前后胸腔、脖颈、鼻梁及耳后2-3分钟即可。'},
        {'essential_oil_name' : 'Eucalyptus', 'efficasy' : '提高工作效率', 'use_pattern' : '蒸薰', 'formula' : '尤加利、薄荷各2滴，薰衣草、迷迭香各1滴。', 'operation' : '只须在香薰炉上方的盛水皿中加八分满热水，在香薰炉台底部点燃蜡烛加滥加或插电，再依配方添加精油即可。（为免影响使用效果，按摩后6小时内不宜洗澡及经稀释后的精油须在两周内使用完。）'},
        {'essential_oil_name' : 'Fennel', 'efficasy' : '平静好眠', 'use_pattern' : '按摩', 'formula' : '茴香2滴，马郁兰4滴，薄荷2滴，荷荷芭油15ml。', 'operation' : '将精油及荷荷芭油混合，在沐浴后，取适量按摩胸口和脚底。'},
        {'essential_oil_name' : 'Fennel', 'efficasy' : '改善便秘', 'use_pattern' : '按摩', 'formula' : '茴香3滴，紫苏5滴，荷荷芭油15ml。', 'operation' : '将精油调匀后，每次取5滴按摩油，以顺时针方向按摩腹部，再按摩臂部、背部下方，连续使用3次。（为免影响使用效果，按摩后6小时内不宜洗澡及经稀释后的精油须在两周内使用完。）'},
        {'essential_oil_name' : 'Frankingcense', 'efficasy' : '改善松弛肌肤，增加肌肤弹性及紧实', 'use_pattern' : '按摩', 'formula' : '乳香3滴，柠檬香芧2滴，玫瑰1滴，小麦胚芽2滴，甜杏仁油15ml。', 'operation' : '调匀后取适量在局部按摩5－10分钟，（为免影响使用效果，按摩后6小时内不宜洗澡及经稀释后的精油须在两周内使用完。）'},
        {'essential_oil_name' : 'Geranium', 'efficasy' : '安抚争躁的情绪', 'use_pattern' : '蒸薰', 'formula' : '天竺葵3滴，乳香3滴，安息香2滴。', 'operation' : '只须在香薰炉上方的盛水皿中八分热水，在香薰炉台底部点燃蜡烛加温或插电，再依配方添加精油即可。（在需要的时候蒸薰，但一天最多3次。）'},
        {'essential_oil_name' : 'Geranium', 'efficasy' : '舒缓经前紧张', 'use_pattern' : '按摩', 'formula' : '天竺葵3滴，佛手柑3滴，鼠尾草2滴，甜杏仁油10ml。', 'operation' : '调匀后取适量按摩于腹部2－3分钟，（为避免影响使用效果，按摩后6小时内不宜洗澡及经稀释后的精油须在两周内使用完.）'},
        {'essential_oil_name' : '', 'efficasy' : '', 'use_pattern' : '', 'formula' : '', 'operation' : ''},
        {'essential_oil_name' : '', 'efficasy' : '', 'use_pattern' : '', 'formula' : '', 'operation' : ''},
        {'essential_oil_name' : '', 'efficasy' : '', 'use_pattern' : '', 'formula' : '', 'operation' : ''},
        {'essential_oil_name' : '', 'efficasy' : '', 'use_pattern' : '', 'formula' : '', 'operation' : ''},
        {'essential_oil_name' : '', 'efficasy' : '', 'use_pattern' : '', 'formula' : '', 'operation' : ''},
        {'essential_oil_name' : '', 'efficasy' : '', 'use_pattern' : '', 'formula' : '', 'operation' : ''},
        {'essential_oil_name' : '', 'efficasy' : '', 'use_pattern' : '', 'formula' : '', 'operation' : ''},
        {'essential_oil_name' : '', 'efficasy' : '', 'use_pattern' : '', 'formula' : '', 'operation' : ''},
        
        {'essential_oil_name' : '', 'efficasy' : '', 'use_pattern' : '', 'formula' : '', 'operation' : ''}
    ],
          
          
          
    #油脂：名称、英文名称、皂化价(NaOH)、皂化价(KOH)、INS、是否可用于超脂、建议用量
    tb_oil : [
        {'name' : '', 'name_en' : '', 'naoh' : 0, 'koh' : 0, 'ins' : 0, 'super_fatting' : False, 'suggested_usage' :  ''},
        {}
    ]
}

def init_all_datas():
    client = MongoClient(config.uri, config.port)
    db = client[config.db_name]
    for (tb_name, datas) in tables.items():
        table = db[tb_name]
        if (table.count() == 0 and datas):
            ids = table.insert(datas)
            print 'ids = ', ids

def init_table(tb_name):
    client = MongoClient(config.uri, config.port)
    db = client[config.db_name]
    table = db[tb_name]
    datas = tables[tb_name]
    table.insert(datas)

if __name__ == '__main__':
    init_all_datas()
