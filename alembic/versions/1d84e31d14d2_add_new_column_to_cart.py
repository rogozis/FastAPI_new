"""add new column to Cart

Revision ID: 1d84e31d14d2
Revises: 0ebc286f125b
Create Date: 2026-02-03 03:41:20.404046

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d84e31d14d2'
down_revision: Union[str, Sequence[str], None] = '0ebc286f125b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
