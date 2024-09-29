from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import FeeedbackMessage

class FeedbackMessageAdmin(ModelAdmin):
    model = FeeedbackMessage
    menu_label = "Feedback"
    menu_icon = "info-circle"
    base_url_path = "feedback_messages"
    menu_order = 500  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = (
        False  # or True to exclude pages of this type from Wagtail's explorer view
    )
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ['name', 'email', 'message',]
    
modeladmin_register(FeedbackMessageAdmin)