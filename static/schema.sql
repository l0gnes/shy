CREATE TABLE IF NOT EXISTS characters(
    userid BIGINT NOT NULL,
    hp INTEGER DEFAULT 0,
    stamina INTEGER DEFAULT 0,
    strength INTEGER DEFAULT 0,
    defense INTEGER DEFAULT 0,
    agility INTEGER DEFAULT 0,
    charisma INTEGER DEFAULT 0,
    gold INTEGER DEFAULT 0
);