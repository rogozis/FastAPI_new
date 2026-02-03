"""renew columns

Revision ID: 231a5d8e8ea5
Revises: 4a7e3c7bea5d
Create Date: 2026-02-03 04:33:24.139347

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '231a5d8e8ea5'
down_revision: Union[str, Sequence[str], None] = '4a7e3c7bea5d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
