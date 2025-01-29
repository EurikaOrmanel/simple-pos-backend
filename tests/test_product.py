import pytest
from uuid import UUID
from decimal import Decimal
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product
from app.repositories.product import ProductRepository
from app.schemas.product import ProductInput

@pytest.mark.asyncio
async def test_add_product_with_valid_details(db_session: AsyncSession):
    """
    Test Case 1: Add a product with valid details
    """
    # Arrange
    product_repo = ProductRepository(db_session)
    product_data = ProductInput(
        name="Test Product",
        price=Decimal("10.99"),
        photo_url="https://example.com/test-product.jpg"
    )
    
    # Act
    product = Product(**product_data.model_dump())
    created_product = await product_repo.create(product)
    
    # Assert
    assert created_product is not None
    assert created_product.name == "Test Product"
    assert created_product.price == Decimal("10.99")
    assert created_product.photo_url == "https://example.com/test-product.jpg"
    assert isinstance(created_product.id, UUID)

@pytest.mark.asyncio
async def test_update_product_price(db_session: AsyncSession):
    """
    Test Case 2: Update the unit charges for a product
    """
    # Arrange
    product_repo = ProductRepository(db_session)
    
    # First create a product
    initial_product = Product(
        name="Test Product",
        price=Decimal("10.99"),
        photo_url="https://example.com/test-product.jpg"
    )
    created_product = await product_repo.create(initial_product)
    
    # Update data
    update_data = ProductUpdate(
        price=Decimal("15.99")
    )
    
    # Act
    updated_product = await product_repo.update(
        created_product.id,
        update_data.model_dump(exclude_unset=True)
    )
    
    # Assert
    assert updated_product is not None
    assert updated_product.price == Decimal("15.99")
    assert updated_product.name == "Test Product"  # Name should remain unchanged
    
    # Verify the update is reflected in the database
    retrieved_product = await product_repo.get_by_id(created_product.id)
    assert retrieved_product.price == Decimal("15.99")

@pytest.fixture
async def cleanup_products(db_session: AsyncSession):
    yield
    # Cleanup after tests
    await db_session.execute("DELETE FROM products")
    await db_session.commit() 