import pytest
from httpx import AsyncClient
from decimal import Decimal
from app.schemas.customer import CustomerInput
from app.schemas.product import ProductCreateInput, ProductUpdateInput
import pytest_asyncio


@pytest_asyncio.fixture
async def admin_token(async_client: AsyncClient) -> str:
    """Get admin authentication token"""
    login_data = {"email": "awworgaba@gmail.com", "password": "1234567890"}
    response = await async_client.post("/v1/admins/auth/login", json=login_data)
    print("Admin login response:", response.json())
    assert response.status_code == 200
    return response.json()["access_token"]


@pytest_asyncio.fixture
async def sales_token(async_client: AsyncClient) -> str:
    """Get sales person authentication token"""
    login_data = {"email": "awag@gmail.com", "password": "12345678"}
    response = await async_client.post("/v1/sales_persons/auth/login", json=login_data)
    assert response.status_code == 200
    return response.json()["access_token"]


@pytest.mark.asyncio
async def test_add_customer_during_order(async_client: AsyncClient, sales_token: str):
    """Test Case 1: Add a new customer dynamically during order placement."""
    # Create a new customer
    customer_data = {"name": "John Doe", "phone": "0241234567"}
    
    response = await async_client.post(
        "/v1/sales_persons/customers/",
        json=customer_data,
        headers={"Authorization": sales_token},
    )
    print("*"*405)
    print(response.json(),"*")
    assert response.status_code == 200
    customer = response.json()
    assert customer["name"] == customer_data["name"]
    assert customer["phone"] == customer_data["phone"]
    assert "id" in customer


@pytest.mark.asyncio
async def test_get_existing_customer(async_client: AsyncClient, sales_token: str):
    """Test Case 2: Use auto-suggestions to map an existing customer to an order."""
    # First create a customer
    customer_data = {"name": "Jane Doe", "phone": "0541234567"}
    create_response = await async_client.post(
        "/v1/sales_person/customers",
        json=customer_data,
        headers={"Authorization": sales_token},
    )
    assert create_response.status_code == 200
    
    # Now search for the customer by phone
    search_response = await async_client.get(
        f"/v1/sales_person/customers/search?phone={customer_data['phone']}",
        headers={"Authorization": sales_token},
    )
    assert search_response.status_code == 200
    customers = search_response.json()
    assert len(customers) > 0
    assert any(c["phone"] == customer_data["phone"] for c in customers)


@pytest.mark.asyncio
async def test_prevent_duplicate_customer(async_client: AsyncClient, sales_token: str):
    """Test Case 3: Handle duplicate entries for mobile numbers."""
    customer_data = {"name": "John Smith", "phone": "0551234567"}
    
    # Create first customer
    response1 = await async_client.post(
        "/v1/sales_person/customers",
        json=customer_data,
        headers={"Authorization": sales_token},
    )
    print("*"*405)
    print(response1.json(),"*")
    assert response1.status_code == 200
    
    # Try to create duplicate customer with same phone
    response2 = await async_client.post(
        "/v1/sales_person/customers",
        json=customer_data,
        headers={"Authorization": sales_token},
    )
    assert response2.status_code == 400  # Should fail with conflict error


@pytest.mark.asyncio
async def test_add_product_with_valid_details(
    async_client: AsyncClient, admin_token: str
):
    """Test Case 1: Add a product with valid details."""
    product_data = {
        "name": "Test Product",
        "price": 10.99,
        "image": "https://example.com/test-product.jpg",
    }
    
    response = await async_client.post(
        "/v1/admin/products",
        json=product_data,
        headers={"Authorization":admin_token},
    )
    print("*"*405)
    print(response.json(),"*")
    assert response.status_code == 200
    product = response.json()
    assert product["name"] == product_data["name"]
    assert float(product["price"]) == product_data["price"]
    assert product["image"] == product_data["image"]
    assert "id" in product


@pytest.mark.asyncio
async def test_update_product_price(async_client: AsyncClient, admin_token: str):
    """Test Case 2: Update the unit charges for a product."""
    # First create a product
    initial_product = {
        "name": "Test Product",
        "price": 10.99,
        "image": "https://example.com/test-product.jpg",
    }
    
    create_response = await async_client.post(
        "/v1/admin/products",
        json=initial_product,
        headers={"Authorization": admin_token},
    )
    assert create_response.status_code == 200
    product = create_response.json()
    print("*"*405)
    print(product,"*")
    
    # Update the price
    update_data = {"price": 15.99}
    
    update_response = await async_client.put(
        f"/v1/admin/products/{product['id']}",
        json=update_data,
        headers={"Authorization": admin_token},
    )
    print("*"*405)
    print(update_response.json(),"*")
    assert update_response.status_code == 200
    updated_product = update_response.json()
    assert float(updated_product["price"]) == update_data["price"]
