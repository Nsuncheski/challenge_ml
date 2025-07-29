# Documentation

## Design Choices

This project simulates a simplified version of a product detail page like MercadoLibre. It is built using:

- **FastAPI**: for modern, high-performance web APIs.
- **Pydantic**: for data validation and serialization.
- **Python typing**: with `Generic` and `TypeVar` to provide reusable repository logic.
- **JSON files**: as a lightweight and easy-to-test data source.
- **Docker**: for isolated and consistent development environments.

**Repository Pattern** was implemented to decouple the service logic from the data layer. This allows easy changes in data persistence in the future (e.g., migrating from JSON to a database) without affecting the business logic.

Each repository (e.g., `ItemRepository`, `UserRepository`, `SellerRepository`) inherits from a shared `BaseRepository` that loads data and optionally supports ID-based lookup.

Services such as `ItemService` orchestrate data fetching and transformation, returning Pydantic models to the API layer.

### Optional Methods

The `get_by_id()` method is optional for repositories that implement it, allowing flexibility in the base class.

```python
def get_by_id(self, id: str):
    """Implement if ID lookup is required."""
    pass

### Challenges Faced

The most challenging part was designing the data models and creating a robust BaseRepository to avoid duplicated code. It was important to make the repository both reusable and extendable, so specific methods like get_by_user_id() could be added only where needed without affecting the general structure.


### Improvements

    Add POST endpoints to create users/items (currently only GET is implemented).

    Implement a PurchaseService and purchase endpoint.

    Replace JSON persistence with a database (e.g., SQLite, PostgreSQL).

    Add filtering/sorting/query parameters for search endpoints.

    Extend tests to include failure scenarios and edge cases.s