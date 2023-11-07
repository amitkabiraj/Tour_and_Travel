from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, name, email, phone, is_admin=False, password=None):
        if not email:
            raise ValueError("User must have an email address.")

        user = self.model(
            name=name.title(),
            email=self.normalize_email(email),
            phone=phone,
            is_admin=is_admin,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, phone, password=None):
        # Check if a user with the given phone number already exists
        if self.filter(phone=phone).exists():
            raise ValueError("User with this phone number already exists.")

        user = self.create_user(
            name=name,
            email=email,
            phone=phone,
            is_admin=True,
            password=password,
        )
        user.is_superuser = True
        user.is_email_verified = True
        user.is_phone_verified = True
        user.save(using=self._db)
        return user

    def get_queryset(self):
        return super().get_queryset()
