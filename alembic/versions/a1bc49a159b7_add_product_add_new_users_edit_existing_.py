"""add product, add new users, edit existing user

Revision ID: a1bc49a159b7
Revises: 175c55a3cb7f
Create Date: 2026-02-03 03:03:24.826223

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1bc49a159b7'
down_revision: Union[str, Sequence[str], None] = '175c55a3cb7f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
