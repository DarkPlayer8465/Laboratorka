PRAGMA foreign_keys = ON;

CREATE TABLE "турниры" (
    "id"       INTEGER PRIMARY KEY,
    "название" TEXT NOT NULL,
    "спорт"    TEXT NOT NULL
);

CREATE TABLE "команды" (
    "id"               INTEGER PRIMARY KEY,
    "название_команды" TEXT NOT NULL,
    "турнир_id"        INTEGER NOT NULL,
    FOREIGN KEY ("турнир_id") REFERENCES "турниры" ("id")
);

CREATE TABLE "составы" (
    "id"         INTEGER PRIMARY KEY,
    "имя_игрока" TEXT NOT NULL,
    "позиция"    TEXT NOT NULL,
    "команда_id" INTEGER NOT NULL,
    FOREIGN KEY ("команда_id") REFERENCES "команды" ("id")
);

CREATE TABLE "авторизация" (
    "имя_пользователя" TEXT NOT NULL UNIQUE,
    "роль"             TEXT NOT NULL,
    "пароль"           TEXT NOT NULL
);

-- Тестовые данные
INSERT INTO "турниры" ("название", "спорт") VALUES
    ('Кубок России', 'футбол'),
    ('Чемпионат города', 'баскетбол');

INSERT INTO "команды" ("название_команды", "турнир_id") VALUES
    ('Динамо', 1),
    ('Спартак', 1),
    ('Урал', 2);

INSERT INTO "составы" ("имя_игрока", "позиция", "команда_id") VALUES
    ('Иван Петров', 'вратарь', 1),
    ('Алексей Смирнов', 'нападающий', 1),
    ('Дмитрий Орлов', 'защитник', 2),
    ('Сергей Волков', 'разыгрывающий', 3);

INSERT INTO "авторизация" ("имя_пользователя", "роль", "пароль") VALUES
    ('admin', 'администратор', 'хеш_пароля_1'),
    ('user1', 'пользователь', 'хеш_пароля_2');

-- Проверка: игроки с командами и турнирами
SELECT t."название" AS tournament, k."название_команды" AS team, s."имя_игрока" AS player, s."позиция" AS position
FROM "составы" s
JOIN "команды" k ON k."id" = s."команда_id"
JOIN "турниры" t ON t."id" = k."турнир_id";
