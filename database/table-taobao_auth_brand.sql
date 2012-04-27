DROP TABLE IF EXISTS `taobao_auth_brands`;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `taobao_auth_brands`(
    `vid` bigint(20) unsigned NOT NULL,
    `name` varchar(128) NOT NULL,
    `pid` bigint(20) unsigned NOT NULL,
    `prop_name` varchar(8),
    `user_name` varchar(20) NOT NULL,
    PRIMARY KEY (`vid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

