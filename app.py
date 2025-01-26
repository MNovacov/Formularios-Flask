from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para el ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    # Inicializar variables para resultados
    nombre = ''
    total_sin_descuento = 0
    total_con_descuento = 0
    error = None  # Variable para el mensaje de error

    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])

        # Validar que los valores sean lógicos
        if edad <= 0 or cantidad_tarros <= 0:
            error = "Por favor ingrese valores válidos."  # Mensaje de error
            return render_template('ejercicio1.html', error=error)

        # Calcular el total y el descuento
        precio_unitario = 9000
        total_sin_descuento = cantidad_tarros * precio_unitario

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento * (1 - descuento)

    return render_template(
        'ejercicio1.html',
        nombre=nombre,
        total_sin_descuento=total_sin_descuento,
        total_con_descuento=total_con_descuento,
        error=error
    )


# Ruta para el ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    usuarios = {'juan': 'admin', 'pepe': 'user'}
    mensaje = ''

    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']

        if usuario in usuarios and usuarios[usuario] == contraseña:
            if usuario == 'juan':
                mensaje = f'Bienvenido administrador {usuario}'
            else:
                mensaje = f'Bienvenido usuario {usuario}'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

    return render_template('ejercicio2.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)
