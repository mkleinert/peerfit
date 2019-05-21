
etl_upsert_queries = {
    'MBO_Reservations':'''INSERT OR IGNORE INTO  MBO_Reservations 
(member_id,studio_id,class_id,viewed_at,reserved_at,canceled_at,class_time_at,checked_in_at)
 select stg.member_id, s.id,c.id,stg.viewed_at,stg.reserved_at,stg.canceled_at,stg.class_time_at,stg.checked_in_at
	from MBO_Reservation_stg stg
	left outer join
	(select *  from 
	MBO_Reservations r1
	left outer join Studio s1 
	on r1.studio_id = s1.id
	left outer join Class c1 
	on r1.class_id = c1.id) r
	on stg.member_id=r.member_id and stg.studio_key = r.studio_key and stg.class_tag = r.class_tag
	and stg.class_time_at = r.class_time_at
	inner join Studio s 
	on stg.studio_key = s.studio_key
	inner join Class c 
	on stg.class_tag = c.class_tag
	where stg.member_id is not null
	;''',
    
    'Class':'''INSERT OR IGNORE INTO  Class
	(class_tag)
select DISTINCT class_tag from MBO_RESERVATION_stg
	where class_tag is not null;''',
    
    'Studio':'''INSERT OR IGNORE INTO  Studio
	(studio_key,studio_address_street,studio_address_city,studio_address_state,studio_address_zip)
select DISTINCT studio_key,studio_address_street,studio_address_city,studio_address_state,studio_address_zip
	from MBO_RESERVATION_stg
	where studio_key is not null;'''
        
        }
