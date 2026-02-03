"""add default to quantity column of Cart table

Revision ID: 435186071c74
Revises: 1d84e31d14d2
Create Date: 2026-02-03 03:42:23.481414

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '435186071c74'
down_revision: Union[str, Sequence[str], None] = '1d84e31d14d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
