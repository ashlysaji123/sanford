from django.contrib import admin

from votings.models import Voting, VotingItem

# Register your models here.
@admin.register(VotingItem)
class VotingItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'voting_startdate', 'voting_enddate']

@admin.register(Voting)
class VotingAdmin(admin.ModelAdmin):
    list_display = ['voting_item','voting', 'user']