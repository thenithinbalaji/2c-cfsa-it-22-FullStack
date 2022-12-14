from django.db import migrations, models
class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(default="Title", max_length=200)),
                ("isbn", models.CharField(default="ISBN0000", max_length=35)),
                ("author", models.CharField(default="Author", max_length=100)),
                ("av_count", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("isbn", models.CharField(default="ISBN0000", max_length=35)),
                ("name", models.CharField(default="User name", max_length=200)),
                (
                    "mail_id",
                    models.CharField(default="example@example.com", max_length=50),
                ),
                ("phno", models.BigIntegerField(default=0)),
                ("resver_id", models.AutoField(primary_key=True, serialize=False)),
                ("status", models.BooleanField(default=True)),
            ],
        ),
    ]
