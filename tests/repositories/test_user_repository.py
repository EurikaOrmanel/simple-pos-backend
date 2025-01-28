import pytest
from uuid import uuid4
from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.user import UserRole
from sqlalchemy.orm import Session
from datetime import datetime, timezone


@pytest.fixture
def user_repository(db_session: Session):
    return UserRepository(db_session)


@pytest.fixture
def sample_user():
    return User(
        id=uuid4(),
        name="Test User",
        email="test@example.com",
        password="hashed_password",
        role=UserRole.USER,
        email_verified=False,
        created_at=datetime.now(timezone.utc)
    )


class TestUserRepository:
    def test_create_user(self, user_repository: UserRepository, sample_user: User):
        # Act
        created_user = user_repository.create(sample_user)

        # Assert
        assert created_user.id is not None
        assert created_user.name == sample_user.name
        assert created_user.email == sample_user.email
        assert created_user.role == UserRole.USER

    def test_get_user_by_id(self, user_repository: UserRepository, sample_user: User):
        # Arrange
        created_user = user_repository.create(sample_user)

        # Act
        retrieved_user = user_repository.get_by_id(created_user.id)

        # Assert
        assert retrieved_user is not None
        assert retrieved_user.id == created_user.id
        assert retrieved_user.name == created_user.name

    def test_get_user_by_email(self, user_repository: UserRepository, sample_user: User):
        # Arrange
        created_user = user_repository.create(sample_user)

        # Act
        retrieved_user = user_repository.get_by_email(created_user.email)

        # Assert
        assert retrieved_user is not None
        assert retrieved_user.email == created_user.email

    def test_get_all_users(self, user_repository: UserRepository, sample_user: User):
        # Arrange
        user_repository.create(sample_user)
        second_user = User(
            id=uuid4(),
            name="Second User",
            email="second@example.com",
            password="hashed_password",
            role=UserRole.USER,
            email_verified=False,
            created_at=datetime.now(timezone.utc)
        )
        user_repository.create(second_user)

        # Act
        users = user_repository.get_all()

        # Assert
        assert len(users) >= 2

    def test_update_user(self, user_repository: UserRepository, sample_user: User):
        # Arrange
        created_user = user_repository.create(sample_user)
        new_name = "Updated User Name"
        new_email = "updated@example.com"

        # Act
        created_user.name = new_name
        created_user.email = new_email
        updated_user = user_repository.update(created_user)

        # Assert
        assert updated_user.name == new_name
        assert updated_user.email == new_email

    def test_delete_user(self, user_repository: UserRepository, sample_user: User):
        # Arrange
        created_user = user_repository.create(sample_user)

        # Act
        user_repository.delete(created_user.id)

        # Assert
        deleted_user = user_repository.get_by_id(created_user.id)
        assert deleted_user is None

    def test_verify_email(self, user_repository: UserRepository, sample_user: User):
        # Arrange
        created_user = user_repository.create(sample_user)
        assert not created_user.email_verified

        # Act
        created_user.email_verified = True
        updated_user = user_repository.update(created_user)

        # Assert
        assert updated_user.email_verified 