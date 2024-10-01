"""oauth user model

Revision ID: 57d12fc9cab4
Revises: e5a65ecff2cd
Create Date: 2024-09-30 15:08:01.251008

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.engine.reflection import Inspector
from langflow.utils import migration


# revision identifiers, used by Alembic.
revision: str = '57d12fc9cab4'
down_revision: Union[str, None] = 'e5a65ecff2cd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    pass


def downgrade() -> None:
    conn = op.get_bind()
    pass
