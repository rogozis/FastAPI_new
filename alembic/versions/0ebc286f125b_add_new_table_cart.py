"""add new table Cart

Revision ID: 0ebc286f125b
Revises: a1bc49a159b7
Create Date: 2026-02-03 03:37:26.740210

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ebc286f125b'
down_revision: Union[str, Sequence[str], None] = 'a1bc49a159b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
