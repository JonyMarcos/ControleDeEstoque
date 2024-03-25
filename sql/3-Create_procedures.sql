USE [MercadoCruz]
GO

/****** Object:  StoredProcedure [dbo].[SPGenerateProductCode]    Script Date: 25/03/2024 19:03:59 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SPGenerateProductCode] 
AS
BEGIN
    DECLARE @NextCode VARCHAR(50);

    -- Obtenha o pr�ximo valor de ProductCode
    SELECT @NextCode = COALESCE(MAX(Product_Code), '00000') FROM Products;

    -- Incremente o valor para o pr�ximo c�digo
    SET @NextCode = RIGHT('00000' + CAST(CAST(@NextCode AS INT) + 1 AS VARCHAR(50)), 5);

    -- Retorne o pr�ximo c�digo
    SELECT @NextCode AS NextCode;
END;
GO


