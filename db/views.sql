
CREATE VIEW ActiveReservationsView AS
SELECT r.id, u.name AS user_name, b.title AS book_title, r.reserved_at
FROM Reservations r
JOIN Users u ON r.user_id = u.id
JOIN Books b ON r.book_id = b.id
WHERE r.status = 'active';
