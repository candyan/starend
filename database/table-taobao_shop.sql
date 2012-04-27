DROP TABLE IF EXISTS `taobao_shop`;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `taobao_shop`(
    `sid` bigint(20) unsigned NOT NULL,
    `cid` bigint(20) unsigned NOT NULL,
    `user_name` varchar(20) NOT NULL,
    `title` varchar(64) NOT NULL,
    `shop_desc` varchar(256),
    `bulletin` varchar(256),
    `pic_path` varchar(64),
    `shop_score_item` varchar(3),
    `shop_score_service` varchar(3),
    `shop_score_delivery` varchar(3),
    PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

