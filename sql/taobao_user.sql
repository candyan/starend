create table taobao_user(
    user_id int not null primary key,
    user_name varchar(20) not null,
    zip varchar(6),
    address varchar(256),
    city varchar(32),
    state varchar(32),
    country varchar(32),
    district varchar(32),
    seller_credit_level int,
    seller_credit_score int,
    seller_credit_total int,
    seller_credit_good int
);

