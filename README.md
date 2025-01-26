# Proyecto: Formularios Flask

## Descripción del Proyecto
Este proyecto consta de dos formularios simples y funcionales desarrollados como parte de una evaluación técnica. Los formularios respetan los colores solicitados en el instructivo y cumplen con los requerimientos funcionales definidos. Además, las contraseñas se manejan de forma segura y censurada.

## Características Principales

1. **Menú Principal**: Desde aquí, se puede acceder a los dos formularios creados:
   - **Ejercicio 1**: Cálculo de compras.
   - **Ejercicio 2**: Inicio de sesión.

2. **Formulario de Cálculo de Compras**:
   - Permite ingresar el **nombre**, **edad** y la **cantidad de tarros de pintura a comprar**.
   - Calcula el total a pagar considerando:
     - Cada tarro de pintura tiene un valor de **$9000**.
     - Descuento del **15%** para personas entre **18 y 30 años** (inclusive).
     - Descuento del **25%** para personas mayores de **30 años**.
     - Personas menores de **18 años** no tienen descuento.
   - Muestra:
     - El nombre de la persona.
     - El total sin descuento.
     - El total con descuento si corresponde.

   **Ejemplo**: Si un usuario tiene **32 años** y compra tarros de pintura, se le aplica un descuento del **25%**.

3. **Formulario de Inicio de Sesión**:
   - Solicita **usuario** y **contraseña**.
   - Las contraseñas ingresadas se censuran para mayor seguridad.

## Detalles del Proyecto

- **Colores**: Se respetaron los colores magenta y verde indicados para los botones.
- **Estilo**: Diseñado con una interfaz limpia y amigable, utilizando colores y estilos modernos.
- **Censura de Contraseñas**: Se asegura que las contraseñas sean ocultadas al momento de ingresarlas, cumpliendo con las mejores prácticas de seguridad.

## Capturas de Pantalla

### Menú principal:
![Menú Principal](https://github.com/MNovacov/Formularios-Flask/blob/main/menu.png)


### Formulario de Cálculo de Compras:

![Formulario de Cálculo de Compras](https://github.com/MNovacov/Formularios-Flask/blob/main/calculo%20compras.png)

### Formulario de Inicio de Sesión:

![Formulario de Inicio de Sesión](https://github.com/MNovacov/Formularios-Flask/blob/main/inicio%20sesion.png)

## Requisitos

- **Python 3.x**.
- Framework usado: Flask.
- Dependencias: Asegúrate de instalar las dependencias necesarias desde el archivo `requirements.txt` si está incluido.

## Instrucciones para Ejecutar

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/MNovacov/Formularios-Flask
   ```

2. **Navegar al directorio del proyecto**:
   ```bash
   cd evaluacionpw
   ```

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar el proyecto**:
   ```bash
   python app.py
   ```

5. **Abrir el navegador** y acceder a `http://127.0.0.1:5000` para interactuar con los formularios.
