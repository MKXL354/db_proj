create table log(
    action char(6) not null,
    affected_table varchar(20) not null,
    time datetime not null,
    primary key(action, affected_table, time)
);

create trigger insert_users after insert on users for each row
    begin
        insert into log values('insert', 'users', now());
    end;

create trigger update_users after insert on users for each row
    begin
        insert into log values('update', 'users', now());
    end;

create trigger delete_users after insert on users for each row
    begin
        insert into log values('delete', 'users', now());
    end;