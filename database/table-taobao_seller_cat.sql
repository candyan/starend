DROP TABLE IF EXISTS `taobao_seller_cat`;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `taobao_seller_cat`(
    `cid` bigint(20) unsigned NOT NULL,
    `parent_cid` bigint(20) unsigned NOT NULL,
    `name` varchar(128) NOT NULL,
    `sort_order` int(11) unsigned,
    `cat_type` varchar(16),
    `pic_url` varchar(256),
    `user_name` varchar(20) NOT NULL,
    PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

