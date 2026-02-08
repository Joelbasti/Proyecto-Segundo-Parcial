create table Reserva(
IDReserva INT PRIMARY KEY,
IDHuesped VARCHAR(10) NOT NULL,
IDHabitacion INT NOT NULL,
FechaIngreso DATE NOT NULL,
FechaSalida DATE NOT NULL,
NumeroNoches INT NOT NULL,
EstadoReserva VARCHAR(12) NOT NULL
)