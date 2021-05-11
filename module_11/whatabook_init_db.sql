


DROP USER IF EXISTS 'whatabook_user'@'localhost';

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;


CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);


INSERT INTO store(locale)
    VALUES('1234 whatabook way, San Diego CA 92109');



INSERT INTO book(book_name, author, details)
    VALUES('Intro to JAVA', 'Daniel Liang', 'Javas Programming and Data Structures');

INSERT INTO book(book_name, author, details)
    VALUES('Sams Teach Yourself SQL', 'Sam Forta', 'Teach Yourself SQL in 10 Minutes');

INSERT INTO book(book_name, author, details)
    VALUES('NoSQL Distilled', 'Pramrod Sadalage', 'A Brief Guide To The Emerging World of Polyglot Persistence');

INSERT INTO book(book_name, author, details)
    VALUES('Python Crash Course', 'Eric Matthes', 'A Hands On Project Based Introduction To Programming');

INSERT INTO book(book_name, author, details)
    VALUES('Head First Java', 'Kathy Sierra', 'A Brain Friendly Guide To Java 2nd Edition');

INSERT INTO book(book_name, author, details)
    VALUES("Head First Javascript Programming", 'Eric Freeman', 'A Brain Friendly Guide to Javascript');

INSERT INTO book(book_name, author, details)
    VALUES('Algorithims To Live By', 'Brian Christian', 'The Computer Science Of Human Decisions');

INSERT INTO book(book_name, author, details)
    VALUES('The 7 Habits Of Highly Effective People', 'Stephen Covey', 'Powerful Lessons In Personal Change');

INSERT INTO book(book_name, author, details)
    VALUES('The Rise Of Superman', 'Steven Kotler', 'Decoding The Science Of Ultimate Human Performance');




INSERT INTO user(first_name, last_name) 
    VALUES('Travis', 'Nickerson');

INSERT INTO user(first_name, last_name)
    VALUES('John', 'Doe');

INSERT INTO user(first_name, last_name)
    VALUES('Jane', 'Doe');




INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Travis'), 
        (SELECT book_id FROM book WHERE book_name = 'Algorithims To Live By')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'John'),
        (SELECT book_id FROM book WHERE book_name = 'Intro to JAVA')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Jane'),
        (SELECT book_id FROM book WHERE book_name = 'Head First Java')
    );
