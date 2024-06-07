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

GO

/****** Object:  StoredProcedure [dbo].[SPAtualizarProduto]    Script Date: 07/06/2024 11:43:33 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[SPAtualizarProduto]
    @Product_Code NVARCHAR(50),
    @Description NVARCHAR(MAX) = NULL,
    @Price DECIMAL(18, 2) = NULL,
    @Quantity INT = NULL,
    @Category NVARCHAR(50) = NULL,
    @Supplier_ID INT = NULL
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE [MercadoCruz].[dbo].[Products]
    SET 
        [Description] = COALESCE(@Description, [Description]),
        Price = COALESCE(@Price, Price),
        Quantity = COALESCE(Quantity + @Quantity, Quantity), -- Adiciona a quantidade
        Category = COALESCE(@Category, Category),
        supplier_id = COALESCE(@Supplier_ID, Supplier_ID),
        Last_Updated = GETDATE()
    WHERE Product_Code = @Product_Code;

    IF @@ROWCOUNT = 0
    BEGIN
        RAISERROR ('Produto não encontrado', 16, 1);
    END
END
GO

