CREATE DATABASE marcadorReuniaoDB;

USE marcadorReuniaoDB;

CREATE TABLE Usuarios (
	UsuarioId bigint NOT NULL AUTO_INCREMENT,
    Username varchar(25) UNIQUE NOT NULL,
    Senha text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
    primary key (UsuarioId)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE DadosPessoais (
	UsuarioId bigint,
    Nome varchar(50) NOT NULL,
    Email varchar(60) NOT NULL,
    TelCelular varchar(12) NOT NULL,
    Cargo varchar(35) NOT NULL,
    foreign key (UsuarioId) REFERENCES Usuarios(UsuarioId)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE SalaEncontro (
	SalaEncontroId bigint NOT NULL AUTO_INCREMENT,
    Nome text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
    TipoReuniao varchar(25) NOT NULL,
    Numero int,
    Link text,
    primary key (SalaEncontroId)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE Reunioes (
  ReuniaoId bigint NOT NULL AUTO_INCREMENT,
  Titulo text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  Pauta longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  DataInicio datetime NOT NULL,
  DataTermino datetime NOT NULL,
  Lembrete int NOT NULL,
  StatusReuniao varchar(20) NOT NULL,
  `HostId` bigint,
  SalaEncontroId bigint,
  foreign key (`HostId`) REFERENCES Usuarios(UsuarioId),
  foreign key (SalaEncontroId) REFERENCES SalaEncontro(SalaEncontroId),
  primary key (ReuniaoId)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE Convidado (
	UsuarioId bigint,
    ReuniaoId bigint,
    ConvidadoId bigint NOT NULL AUTO_INCREMENT,
    AceitaReuniao tinyint(1) NOT NULL,
    foreign key (UsuarioId) REFERENCES Usuarios(UsuarioId),
    foreign key (ReuniaoId) REFERENCES Reunioes(ReuniaoId),
    primary key (ConvidadoId)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;
