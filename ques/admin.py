from django.contrib import admin
import nested_admin
from .models import QuesChoices,UserId,UserPoll,UserAnswerQues
from django.contrib.auth.models import User, Group
from .models import Question,Poll

class QuesChoicesInline(nested_admin.NestedStackedInline):
    model = QuesChoices
    extra = 1


class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    inlines = [QuesChoicesInline]
    extra = 2


@admin.register(Poll)
class PollAdmin(nested_admin.NestedModelAdmin):
    model = Poll
    inlines = [QuestionInline]


class Persmission:
    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class UserAnswerQuesInline(Persmission,nested_admin.NestedStackedInline):
    model = UserAnswerQues
    extra = 1




class UserPollInline(Persmission,nested_admin.NestedStackedInline):

    model = UserPoll
    inlines = [UserAnswerQuesInline]
    max = 1



@admin.register(UserId)
class UserIdAdmin(Persmission,nested_admin.NestedModelAdmin):
    model = UserId
    inlines = [UserPollInline]




admin.site.unregister([User, Group])