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


class UserAnswerQuesInline(nested_admin.NestedStackedInline):
    model = UserAnswerQues
    extra = 1

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class UserPollInline(nested_admin.NestedStackedInline):

    model = UserPoll
    inlines = [UserAnswerQuesInline]
    max = 1

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(UserId)
class UserIdAdmin(nested_admin.NestedModelAdmin):
    model = UserId
    inlines = [UserPollInline]

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.unregister([User, Group])