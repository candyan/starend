DROP TABLE IF EXISTS `taobao_items`;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `taobao_items`(
    `num_iid`   bigint(20) unsigned NOT NULL,
    `detail_url` varchar(256) NOT NULL,
    `title` varchar(60) NOT NULL,
    `user_name` varchar(20) NOT NULL,
    `item_type` varchar(8),
    `item_desc` MEDIUMTEXT,
    `auction_point` int(11) unsigned,
    `property_alias` varchar(512),
    `cid` bigint(20) unsigned,
    `seller_cid` varchar(256),
    `pic_url` varchar(256),
    `item_num` bigint(20) unsigned,
    `valid_thru` int(11) unsigned,
    `list_time` Datetime,
    `delist_time` Datetime,
    `stuff_status` varchar(8),
    `price` float(12,2),
    `post_fee` float(12,2),
    `express_fee` float(12,2),
    `ems_fee` float(12,2),
    `has_discount` tinyint(1),
    `freight_payer` varchar(8),
    `approve_status` varchar(8),
    `auto_fill` varchar(16),
    PRIMARY KEY (`num_iid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

