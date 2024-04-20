USE [MercadoCruz]
GO

/****** Object:  StoredProcedure [dbo].[SPGenerateProductCode]    Script Date: 20/04/2024 17:02:51 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SPGenerateProductCode] 
AS
BEGIN
    DECLARE @NextCode VARCHAR(50);

    -- Obtenha as três primeiras letras do nome do produto mais um prefixo 001
    DECLARE @Prefix VARCHAR(3);
    SET @Prefix = '000'; -- Inicialize o prefixo com '000' para o caso de não haver produtos

    SELECT TOP 1 @Prefix = LEFT(UPPER(Name), 3) FROM Products ORDER BY Id;

    -- Obtenha o próximo valor de ProductCode
    SELECT @NextCode = COALESCE(MAX(Product_Code), @Prefix + '000') FROM Products;

    -- Se o próximo código já estiver no formato correto, incremente o número sequencial
    IF LEFT(@NextCode, 3) = @Prefix
        SET @NextCode = RIGHT('000' + CAST(CAST(RIGHT(@NextCode, 3) AS INT) + 1 AS VARCHAR(50)), 3);
    ELSE
        SET @NextCode = @Prefix + '001'; -- Caso contrário, comece um novo sequencial

    -- Retorne o próximo código
    SELECT @NextCode AS NextCode;
END;
GO


