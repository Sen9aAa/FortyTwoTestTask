from floppyforms import ClearableFileInput
from django.utils.safestring import mark_safe

class ImageFieldWidget(ClearableFileInput):

    class Media:
        css = {
        'all':('css/fileinput.min.css',)
        }
        js =["js/fileinput.min.js"]
   
    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs)
        rendered_widget = super(ImageFieldWidget, self).render(name, value, final_attrs)

        return mark_safe("""
            <div id="kv-avatar-errors-1" class="center-block" style="width:800px;display:none"></div>
                <div class="kv-avatar center-block margin_block">
                <lable class = "form_class" for = 'id_photo'>Avatar</lable>
                <input id="id_photo" name="photo" type="file" class="file-loading">
            </div>
           """)

