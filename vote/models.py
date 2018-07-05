from django.db import models
from django.utils.translation import ugettext_lazy as _


VOTE_STATUS_CHICES = (
    (0, 'enabled'),
    (1, 'disabled'),
)

BOOL_CHOICES = (
    (0, 'True'),
    (1, 'False')
)


class Vote(models.Model):
    user_id = models.IntegerField(_('user_id'))
    name = models.CharField(_('name'), max_length=100)
    status = models.SmallIntegerField(_('status'), choices=VOTE_STATUS_CHICES, default=0)
    detail = models.TextField(_('detail'), blank=True)
    public = models.SmallIntegerField(_('public'), choices=BOOL_CHOICES, default=0)
    multi = models.SmallIntegerField(_('multi'), choices=BOOL_CHOICES, default=0)
    max = models.IntegerField(_('max'), default=1)
    min = models.IntegerField(_('min'), default=1)

    start_dt = models.DateTimeField(_('start_dt'))
    end_dt = models.DateTimeField(_('start_dt'))
    create_dt = models.DateTimeField(_('start_dt'), auto_now_add=True)
    update_dt = models.DateTimeField(_('end_dt'), auto_now=True)

    class Meta:
        db_table = 'flanb_vote'
        ordering = ('id',)
        verbose_name = _('vote')
        verbose_name_plural = _('votes')


class VoteOption(models.Model):
    vote_id = models.IntegerField(_('vote_id'))
    option = models.CharField(_('name'), max_length=100)
    count = models.IntegerField(_('count'), default=0)

    class Meta:
        db_table = 'flanb_vote_option'
        ordering = ('id',)
        verbose_name = _('vote_option')
        verbose_name_plural = _('vote_options')
