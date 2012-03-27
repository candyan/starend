DROP TABLE IF EXISTS `taobao_user`;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `taobao_user`(
    `user_id`   bigint(20) unsigned NOT NULL,
    `user_name` varchar(20) NOT NULL,
    `zip` varchar(6),
    `address` varchar(256),
    `city` varchar(32),
    `state` varchar(32),
    `country` varchar(32),
    `district` varchar(32),
    `seller_credit_level` tinyint(3) unsigned,
    `seller_credit_score` int(11) unsigned,
    `seller_credit_total` bigint(20) unsigned,
    `seller_credit_good` bigint(20) unsigned,
    PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

