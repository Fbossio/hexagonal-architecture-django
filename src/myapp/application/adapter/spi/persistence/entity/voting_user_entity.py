from uuid import uuid4

from django.db import models

from myapp.application.domain.model.identifier.user_id import UserId
from myapp.application.domain.model.karma import Karma
from myapp.application.domain.model.voting_user import VotingUser


class VotingUserEntity(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    karma = models.IntegerField()

    class Meta:
        # in real application this should rather be a view
        db_table = 'user_data'

    def to_domain_model(self):
        return VotingUser(
            UserId(self.user_id),
            Karma(self.karma)
        )
