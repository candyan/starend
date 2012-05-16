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
    `user_name` varchar(20) NOT NULL,
    PRIMARY KEY (`tid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

