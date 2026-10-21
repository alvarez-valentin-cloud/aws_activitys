-- Creación de la tabla de origen
CREATE TABLE IF NOT EXISTS clientes (
    cliente VARCHAR(10),
    edad INT,
    monto_compras NUMERIC(10, 2)
);

-- Inserción de los datos transaccionales
INSERT INTO clientes (cliente, edad, monto_compras) VALUES
('A', 20, 1200.0),
('B', 40, 50000.0),
('C', 60, 30000.0),
('D', 30, 15000.0);
