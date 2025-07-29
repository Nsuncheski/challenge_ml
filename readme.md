# MercadoLibre Clone Backend

Este proyecto es un clon simplificado del backend de MercadoLibre, desarrollado con **FastAPI** y **Python 3.12**.

## Características

- API RESTful para obtener información de ítems y vendedores.
- Datos persistidos en archivos JSON (sin base de datos real).
- Estructura limpia basada en modelos, repositorios y servicios.
- Documentación interactiva con Swagger.
- Pruebas automatizadas con Pytest.
- Contenedor Docker listo para producción y desarrollo.

## Cómo ejecutar

```bash
# Clonar el repositorio
git clone https://github.com/tu_usuario/mercadolibre_clone_backend.git
cd mercadolibre_clone_backend

# Construir y ejecutar el contenedor
docker compose up --build

Una vez que el servidor esté corriendo, accedé a:

    Swagger UI: http://localhost:8000/docss