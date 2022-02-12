import sqlalchemy as sa


METADATA = sa.MetaData()

CONTENT_TABLE = sa.Table(
    "content",
    METADATA,
    sa.Column("id", sa.Integer, primary_key=True, nullable=False),
    sa.Column("url", sa.String(1024), nullable=False, unique=True),
    sa.Column("body", sa.Text, nullable=True),
)
