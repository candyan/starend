DROP TABLE IF EXISTS `taobao_trades`;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `taobao_trades`(
    `tid` bigint(20) unsigned NOT NULL,
    `num` int(11) NOT NULL,
    `num_iid` big(20) unsigned NOT NULL,
    `status` varchar(32) NOT NULL,
    `buyer_name` varchar(20) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

