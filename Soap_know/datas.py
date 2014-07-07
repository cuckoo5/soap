#coding=utf-8
'''
Created on 2013-12-4

@author: cuckoo5
'''

skin_types = [
    {"id" : "normal_skin", "name" : "中性皮肤", "description" : "健康理想的皮肤，多见于青春发育期前的少女，皮脂分泌量适中，皮肤既不干也不油，皮肤细腻，富不弹性，毛孔细小，对外界刺激不敏感。中性皮肤的PH值为5~5.6之间。"},
    {"id" : "dry_skin", "name" : "干性皮肤", "description" : "皮肤白皙，毛孔细小而不明显。皮脂分泌量少，皮肤比较干燥，容易生细小皱纹。毛细血管表浅，易破裂，对外界刺激比较敏感。干性皮肤可分缺水和缺油两种。缺水干性皮肤多见于35岁以上及老年人。缺油干性皮肤多见于年轻人。（但有部分年轻人的皮肤也会呈现缺水现象，特别是在空调下的人）干性皮肤的PH值为4.5~5之间。"},
    {"id" : "oily_skin", "name" : "油性皮肤", "description" : "肤色较深，毛孔粗大，皮脂分泌量多，皮肤油腻光亮，不容易起皱纹，对外界刺激不敏感。由于皮脂分泌过多，容易生粉刺、痤疮，常见于青春发育期年轻人。油性皮肤的PH值为5.6~6.6之间。"},
    {"id" : "mixed_skin", "name" : "混合性皮肤", "description" : "混合性皮肤兼有油性皮肤和干性皮肤的特征。在面部T区（前额、鼻、下巴）呈油性状态，眼部及两颊呈干性状态。混合性皮肤多见于25~35岁年龄的人。"},
    {"id" : "sensitive_skin", "name" : "敏感性皮肤", "description" : "皮肤较薄，对外界刺激很敏感。当受到外界刺激时，会出现局部发红、红肿、丘疹水疱及刺氧等症状。"}
]

difficulty_level = [
    {"id" : 1, "name" : "新手配方", "star" : "★☆☆☆☆", "description" : ""},
    {"id" : 2, "name" : "适合练手", "star" : "★★☆☆☆", "description" : ""},
    {"id" : 3, "name" : "中等难度", "star" : "★★★☆☆", "description" : ""},
    {"id" : 4, "name" : "高手配方", "star" : "★★★★☆", "description" : ""},
    {"id" : 5, "name" : "皂师配方", "star" : "★★★★★", "description" : ""}
]

formulas = [
    {"id" : 1, "name" : "花梨木滋润活肤皂", "skin_types" : ["normal_skin", "mixed_skin"], "difficulty_level" : "3", "function" : "洁面、沐浴", "efficiency" : "美白淡斑、补水保湿、滋润营养"}
]