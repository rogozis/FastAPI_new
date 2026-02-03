"""add new user

Revision ID: 58495ed49c6d
Revises: bb7dbd598d01
Create Date: 2026-02-03 02:23:12.464463

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '58495ed49c6d'
down_revision: Union[str, Sequence[str], None] = 'bb7dbd598d01'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
