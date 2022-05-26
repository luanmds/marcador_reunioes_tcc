CREATE DATABASE marcadorReuniaoDB;

USE marcadorReuniaoDB;

CREATE TABLE Usuarios (
	UsuarioId bigint NOT NULL AUTO_INCREMENT,
    Username varchar(25) UNIQUE NOT NULL,
    Senha text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
    primary key (UsuarioId)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE DadosPessoais (
    DadosPessoaisId bigint NOT NULL AUTO_INCREMENT,
	UsuarioId bigint,
    Nome varchar(50) NOT NULL,
    Email varchar(60) NOT NULL,
    TelCelular varchar(12) NOT NULL,
    Cargo varchar(35) NOT NULL,
    primary key (DadosPessoaisId),
    foreign key (UsuarioId) REFERENCES Usuarios(UsuarioId)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE SalaEncontro (
	SalaEncontroId bigint NOT NULL AUTO_INCREMENT,
    Nome text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
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

INSERT INTO Usuarios (UsuarioId, Username, Senha)
VALUES (1, 'luan.mello', '$2b$12$l7RCS3i9D43KbX5W48AmiOX.piAjr1ElJ4HY03o6PZ9eqyi7pHhRa'),
       (2, 'leticia.hora', '$2b$12$rNFFpceUQF/IudWf6R/1SeERLycLfh87Al7RwupxIZP5zHzNRmI0i'),
       (3, 'peter.monteiro', '$2b$12$zqx8u6dwwOEHT/lvBiZg3eyTo77spjEy2tOB5.jr4Ejn5hw0oooPu'),
       (4, 'artemis.ferreira', '$2b$12$l7RCS3i9D43KbX5W48AmiOX.piAjr1ElJ4HY03o6PZ9eqyi7pHhRa');

INSERT INTO DadosPessoais (DadosPessoaisId, UsuarioId, Nome, Email, TelCelular, Cargo)
VALUES (1, 1, 'Luan Mello da Silva', 'luan.mello@segurocorp.com', '21987654321', 'Analista de TI'),
       (2, 2, 'Leticia da Hora', 'leticia.hora@segurocorp.com', '21987654321', 'Desenvolvedor'),
       (3, 3, 'Peter Monteiro', 'peter.monteiro@segurocorp.com', '21987654321', 'Gerente de Projeto'),
       (4, 4, 'Ártemis Ferreira', 'artemis.ferreira@segurocorp.com', '21987654321', 'Recursos Humanos');
