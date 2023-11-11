"""Init

Revision ID: 37a1875e928b
Revises: 
Create Date: 2023-11-11 01:19:52.434309

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '37a1875e928b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.alter_column('grades', 'grade',
                    existing_type=sa.INTEGER(),
                    nullable=False)
    op.alter_column('grades', 'grade_date',
                    existing_type=sa.DATE(),
                    nullable=True)
    op.drop_constraint('grades_student_id_fkey', 'grades', type_='foreignkey')
    op.drop_constraint('grades_subject_id_fkey', 'grades', type_='foreignkey')
    op.create_foreign_key(None, 'grades', 'students', ['student_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'grades', 'subjects', ['subject_id'], ['id'], ondelete='CASCADE')
    op.alter_column('groups', 'name',
                    existing_type=sa.VARCHAR(length=150),
                    type_=sa.String(length=20),
                    existing_nullable=False)
    op.alter_column('students', 'fullname',
                    existing_type=sa.VARCHAR(length=150),
                    type_=sa.String(length=120),
                    existing_nullable=False)
    op.drop_constraint('students_group_id_fkey', 'students', type_='foreignkey')
    op.create_foreign_key(None, 'students', 'groups', ['group_id'], ['id'], ondelete='CASCADE')
    op.alter_column('subjects', 'name',
                    existing_type=sa.VARCHAR(length=175),
                    type_=sa.String(length=120),
                    existing_nullable=False)
    op.drop_constraint('subjects_teacher_id_fkey', 'subjects', type_='foreignkey')
    op.create_foreign_key(None, 'subjects', 'teachers', ['teacher_id'], ['id'], ondelete='CASCADE')
    op.alter_column('teachers', 'fullname',
                    existing_type=sa.VARCHAR(length=150),
                    type_=sa.String(length=120),
                    existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('teachers', 'fullname',
                    existing_type=sa.String(length=120),
                    type_=sa.VARCHAR(length=150),
                    existing_nullable=False)
    op.drop_constraint(None, 'subjects', type_='foreignkey')
    op.create_foreign_key('subjects_teacher_id_fkey', 'subjects', 'teachers', ['teacher_id'], ['id'])
    op.alter_column('subjects', 'name',
                    existing_type=sa.String(length=120),
                    type_=sa.VARCHAR(length=175),
                    existing_nullable=False)
    op.drop_constraint(None, 'students', type_='foreignkey')
    op.create_foreign_key('students_group_id_fkey', 'students', 'groups', ['group_id'], ['id'])
    op.alter_column('students', 'fullname',
                    existing_type=sa.String(length=120),
                    type_=sa.VARCHAR(length=150),
                    existing_nullable=False)
    op.alter_column('groups', 'name',
                    existing_type=sa.String(length=20),
                    type_=sa.VARCHAR(length=150),
                    existing_nullable=False)
    op.drop_constraint(None, 'grades', type_='foreignkey')
    op.drop_constraint(None, 'grades', type_='foreignkey')
    op.create_foreign_key('grades_subject_id_fkey', 'grades', 'subjects', ['subject_id'], ['id'])
    op.create_foreign_key('grades_student_id_fkey', 'grades', 'students', ['student_id'], ['id'])
    op.alter_column('grades', 'grade_date',
                    existing_type=sa.DATE(),
                    nullable=False)
    op.alter_column('grades', 'grade',
                    existing_type=sa.INTEGER(),
                    nullable=True)
    op.create_table('users',
                    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
                    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
                    sa.Column('password', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
                    sa.Column('age', sa.SMALLINT(), autoincrement=False, nullable=True),
                    sa.Column('phone', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
                    sa.CheckConstraint('age > 18 AND age < 75', name='users_age_check'),
                    sa.PrimaryKeyConstraint('id', name='users_pkey')
                    )
    # ### end Alembic commands ###