"""add name column to Cart

Revision ID: 5c6a46f76924
Revises: ffac0355b198
Create Date: 2026-02-03 04:16:40.956849

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5c6a46f76924'
down_revision: Union[str, Sequence[str], None] = 'ffac0355b198'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
