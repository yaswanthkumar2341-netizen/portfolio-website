-- =====================================================================
-- Portfolio database schema (MySQL)
-- Stores messages submitted through the contact form on the portfolio.
-- This mirrors backend/contact/models.py — Django creates the same table
-- automatically when you run `python manage.py migrate` with MySQL
-- configured, but this file is here so you have the raw SQL too and can
-- run it directly in MySQL Workbench / the mysql CLI.
-- =====================================================================

CREATE DATABASE IF NOT EXISTS portfolio_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE portfolio_db;

CREATE TABLE IF NOT EXISTS contact_contactmessage (
  id            BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name          VARCHAR(100)      NOT NULL,
  email         VARCHAR(254)      NOT NULL,
  phone         VARCHAR(20)       DEFAULT '',
  subject       VARCHAR(200)      NOT NULL,
  message       TEXT              NOT NULL,
  created_at    DATETIME(6)       NOT NULL,
  is_read       TINYINT(1)        NOT NULL DEFAULT 0,

  INDEX idx_created_at (created_at),
  INDEX idx_email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Example queries -------------------------------------------------------

-- All messages, newest first
-- SELECT * FROM contact_contactmessage ORDER BY created_at DESC;

-- Unread messages only
-- SELECT * FROM contact_contactmessage WHERE is_read = 0 ORDER BY created_at DESC;

-- Mark a message as read
-- UPDATE contact_contactmessage SET is_read = 1 WHERE id = 1;

-- Sample insert (for testing without the API)
-- INSERT INTO contact_contactmessage (name, email, phone, subject, message, created_at, is_read)
-- VALUES ('Test User', 'test@example.com', '9999999999', 'Hello', 'Just testing the form.', NOW(6), 0);
