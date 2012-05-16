DROP DATABASE IF EXISTS `starend`;
CREATE DATABASE `starend` DEFAULT CHARSET=utf8;

USE starend;

DROP TABLE IF EXISTS `taobao_user`;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `taobao_user`(
    `user_id`   bigint(20) unsigned NOT NULL,
    `user_name` varchar(20) NOT NULL,
    `city` varchar(32),
    `state` varchar(32),
    `seller_credit_level` tinyint(3) unsigned,
    `seller_credit_score` int(11) unsigned,
    `seller_credit_total` bigint(20) unsigned,
    `seller_credit_good` bigint(20) unsigned,
    PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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

DROP TABLE IF EXISTS `taobao_trades`;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `taobao_trades`(
    `tid` bigint(20) unsigned NOT NULL,
    `num` int(11) unsigned NOT NULL,
    `num_iid` bigint(20) unsigned NOT NULL,
    `status` varchar(32) NOT NULL,
    `title` varchar(128) NOT NULL,
    `buyer_name` varchar(20) NOT NULL,
    `trade_type` varchar(32),
    `price` float(11,2),
    `point_fee` int(11) unsigned,
    `create_time` Datetime,
    `pay_time` Datetime,
    `end_time` Datetime,
    `payment` float(11,2),
    `consign_time` Date,
    `buyer_message`MEDIUMTEXT,
    `post_fee` float(11,2),
    `seller_alipay_no` varchar(128),
    `seller_name` varchar(64),
    `seller_mobile` varchar(11),
    `seller_email` varchar(128),
    `receiver_name` varchar(64),
    `receiver_state` varchar(32),
    `receiver_city` varchar(32),
    `receiver_district` varchar(32),
    `receiver_address` varchar(128),
    `receiver_zip` varchar(11),
    `shipping_type` varchar(16),
    `user_name` varchar(20) NOT NULL,
    PRIMARY KEY (`tid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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

USE mysql;

DELETE FROM user WHERE User='simple' and Host='loaclhost';
FLUSH PRIVILEGES;

GRANT SELECT, INSERT, DELETE ON starend.* to `simple`@`localhost` IDENTIFIED BY "156324";
