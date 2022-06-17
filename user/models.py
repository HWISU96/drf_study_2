from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

# custom user model


class User(AbstractBaseUser):
    username = models.CharField("사용자 계정", max_length=50, unique=True)
    password = models.CharField("비밀번호", max_length=128)
    email = models.EmailField("이메일 주소", max_length=100)
    fullname = models.CharField("이름", max_length=20)
    join_date = models.DateField("가입일", auto_now_add=True)

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'

# 취미 : 운동


class Hobby(models.Model):
    name = models.CharField("취미 이름", max_length=20)

    def __str__(self):
        return self.name


# user detail info table
class UserProfile(models.Model):
    user = models.OneToOneField(
        User, verbose_name="유저", on_delete=models.CASCADE)
    introduction = models.TextField("자기소개", null=True, blank=True)
    birthday = models.DateField("생일")
    age = models.IntegerField("나이")
    hobby = models.ManyToManyField(Hobby, verbose_name="취미")

    def __str__(self):
        return f"{self.user.username} 님의 프로필입니다."

# user - user detail : 1:1
# 한 유저가 두 프로필을 가질 수는 없음

# 쿼리를 날려서 crud를 한다
