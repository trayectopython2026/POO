-- 1 Ver los personajes las columnas y como estan guardadas
SELECT id, nombre, categoria_id, especie_id, planeta_id, descripcion, imagen
FROM personajes;

-- 2. Primera relacion : varios personajes pueden pertenecer a una categoria
SELECT p.nombre,c.nombre AS categoria
FROM personajes p
INNER JOIN categorias c
ON p.categoria_id = c.id 

-- 3. Relacionar las cuatro tablas para un obtener la ficha legible 

SELECT p.nombre,p.imagen, c.nombre AS categoria, e.nombre AS especie ,pl.nombre AS planeta
FROM personajes p
INNER JOIN categorias c 
ON p.categoria_id = c.id
INNER JOIN especies e 
ON p.especie_id = e.id
INNER JOIN planetas pl
ON p.planeta_id = pl.id

-- 4 - Filtrar personajes de una categoria 

SELECT p.nombre , c.nombre AS categoria
FROM personajes p
INNER JOIN categorias c
ON p.categoria_id = c.id
WHERE c.nombre = 'Jedi'

-- 5. Buscar por una parte del nombre
SELECT nombre
FROM personajes
WHERE nombre LIKE '%Yoda%'

-- 6. Contar personajes de cada categoria
SELECT c.nombre, COUNT(p.id) AS cantidad  
FROM personajes p
INNER JOIN categorias c
ON p.categoria_id = c.id
GROUP BY c.nombre

-- 6. Contar personajes de cada categoria
SELECT c.nombre, COUNT(p.id) AS cantidad  
FROM personajes p
RIGHT JOIN categorias c
ON p.categoria_id = c.id
GROUP BY c.nombre








