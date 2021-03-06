from sqlalchemy import Column, Integer, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.schema import UniqueConstraint

from objects.database_models import Base


class MutedTemplate(Base):
    __tablename__ = "muted_templates"

    id = Column(Integer, primary_key=True)
    alert_id = Column(BigInteger, nullable=False)
    template_id = Column(Integer, ForeignKey("templates.id", ondelete="CASCADE"), nullable=False)
    expires = Column(Integer, nullable=False)

    template_unique = UniqueConstraint(template_id)

    template = relationship("Template", back_populates="template_mute")

    def __repr__(self):
        return ("<MutedTemplate(id={0.id}, alert_id={0.id}, template={0.template}, "
                "expires={0.expires})>".format(self))
