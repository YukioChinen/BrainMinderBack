"""create tables

Revision ID: 5c20420a85c8
Revises: a73ee53acd3a
Create Date: 2024-08-07 15:08:43.941461

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5c20420a85c8"
down_revision: Union[str, None] = "a73ee53acd3a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "divide_operations",
        sa.Column(
            "id",
            sa.UUID(),
            server_default=sa.text("iag.uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column("a", sa.Float(), nullable=False),
        sa.Column("b", sa.Float(), nullable=False),
        sa.Column("result", sa.Float(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column("deleted_at", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        schema="iag",
    )
    op.create_index(
        op.f("ix_iag_divide_operations_id"),
        "divide_operations",
        ["id"],
        unique=False,
        schema="iag",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_iag_divide_operations_id"),
        table_name="divide_operations",
        schema="iag",
    )
    op.drop_table("divide_operations", schema="iag")
    # ### end Alembic commands ###
