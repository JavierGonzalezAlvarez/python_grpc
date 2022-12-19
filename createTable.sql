create table client (
    user_id serial primary key,
    name varchar(20) not null,
    surname varchar(50),
    id_address int not null
);

create table address (
    address_id serial primary key,
    street varchar(20) not null,
    number int,
    city varchar(20)
);