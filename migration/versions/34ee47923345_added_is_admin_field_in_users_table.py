"""added is_admin field in users table

Revision ID: 34ee47923345
Revises: 109b56e84db5
Create Date: 2024-12-02 16:55:07.958676

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '34ee47923345'
down_revision: Union[str, None] = '109b56e84db5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'users',
        sa.Column(
            'is_admin',
            sa.Boolean(),
            nullable=False,
            server_default=sa.text('false')  # Set default value to False
        )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_admin')
    # ### end Alembic commands ###