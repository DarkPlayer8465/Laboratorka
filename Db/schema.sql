PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS "турниры" (
    "id"       INTEGER PRIMARY KEY,
    "название" TEXT NOT NULL,
    "спорт"    TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS "команды" (
    "id"               INTEGER PRIMARY KEY,
    "название_команды" TEXT NOT NULL,
    "турнир_id"        INTEGER NOT NULL,
    FOREIGN KEY ("турнир_id") REFERENCES "турниры" ("id")
);

CREATE TABLE IF NOT EXISTS "составы" (
    "id"         INTEGER PRIMARY KEY,
    "имя_игрока" TEXT NOT NULL,
    "позиция"    TEXT NOT NULL,
    "команда_id" INTEGER NOT NULL,
    FOREIGN KEY ("команда_id") REFERENCES "команды" ("id")
);

CREATE TABLE IF NOT EXISTS "авторизация" (
    "имя_пользователя" TEXT NOT NULL UNIQUE,
    "роль"             TEXT NOT NULL,
    "пароль"           TEXT NOT NULL
);
