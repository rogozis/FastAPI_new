"""add product, add new users, edit existing user

Revision ID: 175c55a3cb7f
Revises: 58495ed49c6d
Create Date: 2026-02-03 02:38:11.411820

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '175c55a3cb7f'
down_revision: Union[str, Sequence[str], None] = '58495ed49c6d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
