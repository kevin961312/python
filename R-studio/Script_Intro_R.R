#Variables para asignación.
num1 <- 2
num2 <- 5
num2+num1
#Asignaciones y strings
vars1 <- "Hello"
vars2 <- "world!"
#concatenación de strings
paste(vars1,vars2)
#creacion de vectores
#vector entero
vect1 <- c(1,2,3,5,3,6)
#vector de numeros reales
vect2 <- c(2/5,0.1,3/4,5/6,0.2,0.22222)
#vector de cadenas
vectstr <- c("ferrari","lamborghini","BMW")
#algunos comandos para manejar datos de manera sencilla
#Número de filas
nrow(Bulnesia)
#Número de columnas
ncol(Bulnesia)
#Observar la estructura de la base de datos
str(Bulnesia)
#muestra solo la columna C4
Bulnesia$C4
#Muestra de el primer elemento de la columna 4
Bulnesia[1, 4]
#Muestra todos los elementos de la columna 4
Bulnesia[, 4]
#Recibe muestra todos los elementos del vector dado 
Bulnesia[, c(1, 2, 3)]
#Recibe muestra todos los elementos del vector y 
#muestra la columna con la palabra clave dada
Bulnesia[,c("species", "C1", "C2")]
#Tomar la columna y muestra los elementos con la condición dada
Bulnesia$C1[Bulnesia$C1 > 1]
Bulnesia$C3[Bulnesia$C3 >= 2]
#Dada la columna y dado la fila especial
Bulnesia$C1[8]
#Calcular media
mean(Bulnesia$C4)
#Calcular desviación estandar
sd(Bulnesia$C5)
#Calculo varianza
sd(Bulnesia$C2)
sd(Bulnesia$C2)**2
#covarianza
cor(Bulnesia$C5, Bulnesia$C6)
#Historgrama
hist(Bulnesia$C2, col="Red", main = "Bulnesia")
plot(Bulnesia$C2)
#Todos los tipos de barras en R con el comando plot
y <- Bulnesia$C5
types <- c("p", "l", "b", "c", "o", "h", "s", "S", "n")

par(mfrow = c(3, 3), cex = 0.6, mar = c(3, 3, 3, 3))
#mar : un vector numérico de longitud 4, que establece los tamaños de margen en el siguiente orden: 
#inferior, izquierda, superior y derecha. El valor predeterminado es c (5.1, 4.1, 4.1, 2.1)
for (type in types){
  plot(y, type = type, main = paste0("type = ", type))
}

