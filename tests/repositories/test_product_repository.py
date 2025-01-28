import pytest
from uuid import uuid4
from app.models.product import Product
from app.repositories.product import ProductRepository
from sqlalchemy.orm import Session
from datetime import datetime, timezone


@pytest.fixture
def product_repository(db_session: Session):
    return ProductRepository(db_session)


@pytest.fixture
def sample_product():
    return Product(
        id=uuid4(),
        name="Test Product",
        price=99.99,
        image="test-image.jpg",
        created_at=datetime.now(timezone.utc)
    )


class TestProductRepository:
    def test_create_product(self, product_repository: ProductRepository, sample_product: Product):
        # Act
        created_product = product_repository.create(sample_product)

        # Assert
        assert created_product.id is not None
        assert created_product.name == sample_product.name
        assert created_product.price == sample_product.price
        assert created_product.image == sample_product.image

    def test_get_product_by_id(self, product_repository: ProductRepository, sample_product: Product):
        # Arrange
        created_product = product_repository.create(sample_product)

        # Act
        retrieved_product = product_repository.get_by_id(created_product.id)

        # Assert
        assert retrieved_product is not None
        assert retrieved_product.id == created_product.id
        assert retrieved_product.name == created_product.name

    def test_get_all_products(self, product_repository: ProductRepository, sample_product: Product):
        # Arrange
        product_repository.create(sample_product)
        second_product = Product(
            id=uuid4(),
            name="Second Product",
            price=149.99,
            image="second-image.jpg",
            created_at=datetime.now(timezone.utc)
        )
        product_repository.create(second_product)

        # Act
        products = product_repository.get_all()

        # Assert
        assert len(products) >= 2

    def test_update_product(self, product_repository: ProductRepository, sample_product: Product):
        # Arrange
        created_product = product_repository.create(sample_product)
        new_name = "Updated Product Name"
        new_price = 199.99

        # Act
        created_product.name = new_name
        created_product.price = new_price
        updated_product = product_repository.update(created_product)

        # Assert
        assert updated_product.name == new_name
        assert updated_product.price == new_price

    def test_delete_product(self, product_repository: ProductRepository, sample_product: Product):
        # Arrange
        created_product = product_repository.create(sample_product)

        # Act
        product_repository.delete(created_product.id)

        # Assert
        deleted_product = product_repository.get_by_id(created_product.id)
        assert deleted_product is None 