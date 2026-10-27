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
