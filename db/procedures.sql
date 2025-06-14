
DELIMITER //
CREATE PROCEDURE ReserveBook(IN userId INT, IN bookId INT)
BEGIN
    DECLARE available INT;

    SELECT total_copies - COUNT(*) INTO available
    FROM Books
    LEFT JOIN Reservations ON Books.id = Reservations.book_id
    WHERE Books.id = bookId AND Reservations.status = 'active';

    IF available > 0 THEN
        INSERT INTO Reservations (user_id, book_id, status)
        VALUES (userId, bookId, 'active');
    END IF;
END //
DELIMITER ;
