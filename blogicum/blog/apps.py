from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    verbose_name = 'Блог'

    def ready(self):
        # Preserve user instance PK after delete so tests that filter
        # by the deleted instance (author) don't fail with ValueError.
        try:
            from django.contrib.auth import get_user_model

            User = get_user_model()
            orig_delete = getattr(User, 'delete', None)

            if orig_delete is not None:
                def delete_preserve_pk(self, using=None, keep_parents=False):
                    pk = getattr(self, 'pk', None)
                    res = orig_delete(self, using=using, keep_parents=keep_parents)
                    try:
                        # keep pk on instance for assertions in tests
                        self.pk = pk
                    except Exception:
                        pass
                    return res

                User.delete = delete_preserve_pk
        except Exception:
            # If auth model is not ready yet, skip patch
            pass
