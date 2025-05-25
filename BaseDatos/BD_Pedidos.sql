-- Base de datos
-- --------------------------------------------------------

-- Crear el usuario (si no existe)
CREATE USER IF NOT EXISTS 'user_python'@'localhost' IDENTIFIED BY 'Pass2025**';

-- Otorgar permisos al usuario
GRANT CREATE, INSERT, UPDATE, DELETE, SELECT, FILE, EXECUTE 
ON *.* 
TO 'user_python'@'localhost' WITH GRANT OPTION;

-- Crear la base de datos 
CREATE DATABASE IF NOT EXISTS EnvioBD;

-- Usar la base de datos correcta
USE EnvioBD;


-- Estructura de tabla para la tabla `ciudades`

CREATE TABLE `ciudades` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `departamento_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ciudades`
--

INSERT INTO `ciudades` (`id`, `nombre`, `departamento_id`) VALUES
(1, 'Medellín', 1),
(2, 'Bogotá', 2),
(3, 'Cali', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `conductores`
--

CREATE TABLE `conductores` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `cedula` varchar(255) DEFAULT NULL,
  `telefono` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `conductores`
--

INSERT INTO `conductores` (`id`, `nombre`, `cedula`, `telefono`) VALUES
(1, 'Pedro Jiménez', '123456789', '3001234567'),
(2, 'Sofía Martínez', '987654321', '3107654321'),
(3, 'Rafael Mejía', '456789123', '3006789123');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamentos`
--

CREATE TABLE `departamentos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `departamentos`
--

INSERT INTO `departamentos` (`id`, `nombre`) VALUES
(1, 'Antioquia'),
(2, 'Cundinamarca'),
(3, 'Valle del Cauca');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estados`
--

CREATE TABLE `estados` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estados`
--

INSERT INTO `estados` (`id`, `nombre`) VALUES
(1, 'Pendiente'),
(2, 'En proceso'),
(3, 'Finalizado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `incidencias`
--

CREATE TABLE `incidencias` (
  `id` int(11) NOT NULL,
  `pedido_id` int(11) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `fecha` datetime DEFAULT current_timestamp(),
  `resuelta` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `incidencias`
--

INSERT INTO `incidencias` (`id`, `pedido_id`, `descripcion`, `fecha`, `resuelta`) VALUES
(1, 2, 'Paquete dañado durante el transporte', '2025-04-08 06:57:30', 0),
(2, 3, 'Dirección incorrecta, reprogramar entrega', '2025-04-08 06:57:30', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `metodos_pago`
--

CREATE TABLE `metodos_pago` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `metodos_pago`
--

INSERT INTO `metodos_pago` (`id`, `nombre`) VALUES
(1, 'Efectivo'),
(2, 'Tarjeta de crédito'),
(3, 'Transferencia bancaria');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagos`
--

CREATE TABLE `pagos` (
  `id` int(11) NOT NULL,
  `pedido_id` int(11) DEFAULT NULL,
  `metodo_pago_id` int(11) DEFAULT NULL,
  `valor` varchar(512) DEFAULT NULL,
  `fecha_pago` datetime DEFAULT current_timestamp(),
  `estado_pago` enum('pendiente','pagado','fallido') DEFAULT 'pendiente'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pagos`
--

INSERT INTO `pagos` (`id`, `pedido_id`, `metodo_pago_id`, `valor`, `fecha_pago`, `estado_pago`) VALUES
(1, 1, 1, '150000.00', '2025-04-08 06:57:30', 'pagado'),
(2, 2, 2, '250000.00', '2025-04-08 06:57:30', 'pendiente'),
(3, 3, 3, '350000.00', '2025-04-08 06:57:30', 'pagado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos`
--

CREATE TABLE `pedidos` (
  `id` int(11) NOT NULL,
  `codigo` varchar(50) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `destinatario` varchar(100) NOT NULL,
  `direccion_entrega` text NOT NULL,
  `ciudad_id` int(11) DEFAULT NULL,
  `ruta_id` int(11) DEFAULT NULL,
  `vehiculo_id` int(11) DEFAULT NULL,
  `conductor_id` int(11) DEFAULT NULL,
  `tipo_envio_id` int(11) DEFAULT NULL,
  `estado_actual` int(11) DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pedidos`
--

INSERT INTO `pedidos` (`id`, `codigo`, `usuario_id`, `destinatario`, `direccion_entrega`, `ciudad_id`, `ruta_id`, `vehiculo_id`, `conductor_id`, `tipo_envio_id`, `estado_actual`, `fecha_creacion`) VALUES
(1, 'PED001', 1, 'Luis Gómez', 'Calle 12 #34-56', 1, 1, 1, 1, 1, 1, '2025-04-08 06:57:30'),
(2, 'PED002', 2, 'Ana Torres', 'Carrera 7 #89-10', 2, 2, 2, 2, 2, 2, '2025-04-08 06:57:30'),
(3, 'PED003', 3, 'Carlos Suárez', 'Avenida 45 #67-89', 3, 3, 3, 3, 3, 3, '2025-04-08 06:57:30');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rutas`
--

CREATE TABLE `rutas` (
  `id` int(11) NOT NULL,
  `ciudad_origen_id` int(11) DEFAULT NULL,
  `ciudad_destino_id` int(11) DEFAULT NULL,
  `zona_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rutas`
--

INSERT INTO `rutas` (`id`, `ciudad_origen_id`, `ciudad_destino_id`, `zona_id`) VALUES
(1, 1, 2, 1),
(2, 2, 3, 2),
(3, 3, 1, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `seguimiento`
--

CREATE TABLE `seguimiento` (
  `id` int(11) NOT NULL,
  `pedido_id` int(11) NOT NULL,
  `estado_id` int(11) NOT NULL,
  `ubicacion` varchar(255) DEFAULT NULL,
  `comentario` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcado de datos para la tabla `seguimiento`
INSERT INTO `seguimiento` (`id`, `pedido_id`, `estado_id`, `ubicacion`, `comentario`) VALUES
(1, 1, 1, 'Bodega Medellín', 'Pedido empaquetado'),
(2, 2, 2, 'En tránsito hacia Bogotá', 'Retraso por tráfico'),
(3, 3, 3, 'Entregado', 'Sin inconvenientes');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_envio`
--

CREATE TABLE `tipo_envio` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipo_envio`
--

INSERT INTO `tipo_envio` (`id`, `nombre`) VALUES
(1, 'Normal'),
(2, 'Express'),
(3, 'Internacional');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `email` varchar(512) DEFAULT NULL,
  `telefono` varchar(512) DEFAULT NULL,
  `direccion` varchar(512) DEFAULT NULL,
  `rol` enum('cliente','operador','admin') DEFAULT 'cliente',
  `fecha_registro` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `email`, `telefono`, `direccion`, `rol`, `fecha_registro`) VALUES
(1, 'Juan Pérez', 'juan@example.com', '3001234567', 'Calle 1 #23-45', 'cliente', '2025-04-08 06:57:29'),
(2, 'María Gómez', 'maria@example.com', '3007654321', 'Carrera 8 #12-34', 'operador', '2025-04-08 06:57:29'),
(3, 'Carlos López', 'carlos@example.com', '3101234567', 'Avenida 5 #67-89', 'admin', '2025-04-08 06:57:29');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vehiculos`
--

CREATE TABLE `vehiculos` (
  `id` int(11) NOT NULL,
  `placa` varchar(512) NOT NULL,
  `tipo` varchar(50) DEFAULT NULL,
  `capacidad` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `vehiculos`
--

INSERT INTO `vehiculos` (`id`, `placa`, `tipo`, `capacidad`) VALUES
(1, 'ABC123', 'Camión', 5000.00),
(2, 'DEF456', 'Van', 1000.00),
(3, 'GHI789', 'Moto', 150.00);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `zonas`
--

CREATE TABLE `zonas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `zonas`
--

INSERT INTO `zonas` (`id`, `nombre`) VALUES
(1, 'Urbana'),
(2, 'Rural'),
(3, 'Especial');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `ciudades`
--
ALTER TABLE `ciudades`
  ADD PRIMARY KEY (`id`),
  ADD KEY `departamento_id` (`departamento_id`);

--
-- Indices de la tabla `conductores`
--
ALTER TABLE `conductores`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `cedula` (`cedula`);

--
-- Indices de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `estados`
--
ALTER TABLE `estados`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `incidencias`
--
ALTER TABLE `incidencias`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pedido_id` (`pedido_id`);

--
-- Indices de la tabla `metodos_pago`
--
ALTER TABLE `metodos_pago`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `pagos`
--
ALTER TABLE `pagos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pedido_id` (`pedido_id`),
  ADD KEY `metodo_pago_id` (`metodo_pago_id`);

--
-- Indices de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`),
  ADD KEY `usuario_id` (`usuario_id`),
  ADD KEY `ciudad_id` (`ciudad_id`),
  ADD KEY `ruta_id` (`ruta_id`),
  ADD KEY `vehiculo_id` (`vehiculo_id`),
  ADD KEY `conductor_id` (`conductor_id`),
  ADD KEY `tipo_envio_id` (`tipo_envio_id`),
  ADD KEY `estado_actual` (`estado_actual`);

--
-- Indices de la tabla `rutas`
--
ALTER TABLE `rutas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ciudad_origen_id` (`ciudad_origen_id`),
  ADD KEY `ciudad_destino_id` (`ciudad_destino_id`),
  ADD KEY `zona_id` (`zona_id`);

--
-- Indices de la tabla `seguimiento`
--
ALTER TABLE `seguimiento`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pedido_id` (`pedido_id`),
  ADD KEY `estado_id` (`estado_id`);

--
-- Indices de la tabla `tipo_envio`
--
ALTER TABLE `tipo_envio`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `placa` (`placa`);

--
-- Indices de la tabla `zonas`
--
ALTER TABLE `zonas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `ciudades`
--
ALTER TABLE `ciudades`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `conductores`
--
ALTER TABLE `conductores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `estados`
--
ALTER TABLE `estados`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `incidencias`
--
ALTER TABLE `incidencias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `metodos_pago`
--
ALTER TABLE `metodos_pago`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `pagos`
--
ALTER TABLE `pagos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `rutas`
--
ALTER TABLE `rutas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `seguimiento`
--
ALTER TABLE `seguimiento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `tipo_envio`
--
ALTER TABLE `tipo_envio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `zonas`
--
ALTER TABLE `zonas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `ciudades`
--
ALTER TABLE `ciudades`
  ADD CONSTRAINT `ciudades_ibfk_1` FOREIGN KEY (`departamento_id`) REFERENCES `departamentos` (`id`);

--
-- Filtros para la tabla `incidencias`
--
ALTER TABLE `incidencias`
  ADD CONSTRAINT `incidencias_ibfk_1` FOREIGN KEY (`pedido_id`) REFERENCES `pedidos` (`id`);

--
-- Filtros para la tabla `pagos`
--
ALTER TABLE `pagos`
  ADD CONSTRAINT `pagos_ibfk_1` FOREIGN KEY (`pedido_id`) REFERENCES `pedidos` (`id`),
  ADD CONSTRAINT `pagos_ibfk_2` FOREIGN KEY (`metodo_pago_id`) REFERENCES `metodos_pago` (`id`);

--
-- Filtros para la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD CONSTRAINT `pedidos_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`),
  ADD CONSTRAINT `pedidos_ibfk_2` FOREIGN KEY (`ciudad_id`) REFERENCES `ciudades` (`id`),
  ADD CONSTRAINT `pedidos_ibfk_3` FOREIGN KEY (`ruta_id`) REFERENCES `rutas` (`id`),
  ADD CONSTRAINT `pedidos_ibfk_4` FOREIGN KEY (`vehiculo_id`) REFERENCES `vehiculos` (`id`),
  ADD CONSTRAINT `pedidos_ibfk_5` FOREIGN KEY (`conductor_id`) REFERENCES `conductores` (`id`),
  ADD CONSTRAINT `pedidos_ibfk_6` FOREIGN KEY (`tipo_envio_id`) REFERENCES `tipo_envio` (`id`),
  ADD CONSTRAINT `pedidos_ibfk_7` FOREIGN KEY (`estado_actual`) REFERENCES `estados` (`id`);

--
-- Filtros para la tabla `rutas`
--
ALTER TABLE `rutas`
  ADD CONSTRAINT `rutas_ibfk_1` FOREIGN KEY (`ciudad_origen_id`) REFERENCES `ciudades` (`id`),
  ADD CONSTRAINT `rutas_ibfk_2` FOREIGN KEY (`ciudad_destino_id`) REFERENCES `ciudades` (`id`),
  ADD CONSTRAINT `rutas_ibfk_3` FOREIGN KEY (`zona_id`) REFERENCES `zonas` (`id`);

--
-- Filtros para la tabla `seguimiento`
--
ALTER TABLE `seguimiento`
  ADD CONSTRAINT `seguimiento_ibfk_1` FOREIGN KEY (`pedido_id`) REFERENCES `pedidos` (`id`),
  ADD CONSTRAINT `seguimiento_ibfk_2` FOREIGN KEY (`estado_id`) REFERENCES `estados` (`id`);
COMMIT;