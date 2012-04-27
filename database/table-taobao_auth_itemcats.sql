DROP TABLE IF EXISTS `taobao_auth_itemcats`;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `taobao_auth_itemcats`(
    `cid` bigint(20) unsigned NOT NULL,
    `parent_cid` bigint(20) unsigned NOT NULL,
    `name` varchar(128) NOT NULL,
    `is_parent` tinyint(1),
    `status` varchar(8),
    `sort_order` int(11) unsigned,
    `user_name` varchar(20) NOT NULL,
    PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

