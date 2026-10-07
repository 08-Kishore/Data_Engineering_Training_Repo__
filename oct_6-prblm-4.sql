SET SQL_SAFE_UPDATES = 0;
CREATE TABLE vehicles (
    vehicle_id INT PRIMARY KEY,
    vehicle_name VARCHAR(100),
    vehicle_type VARCHAR(50),
    daily_rate DECIMAL(10,2),
    available_status VARCHAR(20)
);
INSERT INTO vehicles VALUES
(1, 'Honda City', 'Car', 2500, 'Available'),
(2, 'Toyota Innova', 'Car', 3500, 'Available'),
(3, 'Royal Enfield', 'Bike', 1200, 'Rented'),
(4, 'Activa', 'Scooter', 700, 'Available'),
(5, 'Mahindra Thar', 'SUV', 4500, 'Rented'),
(6, 'Hyundai Creta', 'SUV', 3200, 'Available'),
(7, 'KTM Duke', 'Bike', 1500, 'Available');

delimiter // 
create procedure GetAllVehicles()
begin
	select * from vehicles;
end//
delimiter ;

delimiter //
create procedure GetAvailableVehicles()
begin
	select * from vehicles where available_status='Available';
end //
delimiter ;

delimiter //
create procedure GetVehiclesByType(in type2 VARCHAR(50))
begin 
	select * from vehicles where vehicle_type=type2;
end//
delimiter ;

DELIMITER //
CREATE PROCEDURE GetVehiclesByMaxRate(IN max_rate DECIMAL(10,2))
BEGIN
    SELECT *
    FROM vehicles
    WHERE daily_rate <= max_rate;
END //
DELIMITER ;

delimiter //
create procedure UpdateDailyRateByVehicleID(in idd int,rate decimal)
begin
	update vehicles
    set daily_rate=rate
    where vehicle_id=idd;
end//
delimiter ;

delimiter //
create procedure ChangeVehicleStatus(in idd int,stat varchar(20))
begin
	update vehicles
    set available_status=stat
    where vehicle_id=idd;
end//
delimiter ;

delimiter //
create procedure IncreaseDailyRateBySuppy(in vid int,rate decimal)
begin 
	update vehicles
    set daily_rate=daily_rate+rate
    where vehicle_id=vid;
end//
delimiter ;

delimiter //
create procedure DeleteByVehicleID(in vid int)
begin
	delete from vehicles where vehicle_id=vid;
end//
delimiter ;

delimiter //
create procedure get_vehicles_between_rates(
    in min_rate decimal(10,2),
    in max_rate decimal(10,2)
)
begin
    select *
    from vehicles
    where daily_rate between min_rate and max_rate;
end //
delimiter ;

delimiter //
create procedure count_vehicles_by_type(in type_name varchar(50))
begin
    select count(*) as vehicle_count
    from vehicles
    where vehicle_type = type_name;
end //
delimiter ;

